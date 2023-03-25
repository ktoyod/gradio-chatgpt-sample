import json
import os
from urllib import parse, request

import gradio as gr


API_HOST = os.getenv("API_HOST", "http://localhost")
API_PORT = os.getenv("API_PORT", "8080")


def greet():
    req = request.Request(f"{API_HOST}:{API_PORT}")
    with request.urlopen(req) as res:
        data = json.loads(res.read().decode("utf-8"))
    return f"Hello {data['message']}! (at {data['time']})"


def chatgpt(message: str):
    req_data = json.dumps({"message": message}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = request.Request(
        f"{API_HOST}:{API_PORT}/chatgpt",
        data=req_data,
        headers=headers,
    )
    with request.urlopen(req) as res:
        res_data = json.loads(res.read().decode("utf-8"))
    return res_data["answer"]


if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("# This is a gradio demo with FastAPI!")

        gr.Markdown("## Let's request to FastAPI!")
        out = gr.Textbox(label="Response")
        button = gr.Button("FastAPI!")
        button.click(greet, outputs=out)

        gr.Markdown("## Let's talk with ChatGPT!")
        with gr.Row():
            inp = gr.Textbox(placeholder="日本の首都は？", label="質問")
            out = gr.Textbox(label="回答")
        btn = gr.Button("Run")
        btn.click(fn=chatgpt, inputs=inp, outputs=out)

    demo.launch(server_name="0.0.0.0", server_port=80)
