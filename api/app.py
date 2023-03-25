from datetime import datetime
import os

from fastapi import FastAPI
import openai
from pydantic import BaseModel
import uvicorn


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

app = FastAPI()


class ChatGPTInput(BaseModel):
    message: str


@app.get("/")
def read_root():
    now = datetime.now()
    return {"message": "FastAPI", "time": now.strftime("%Y-%m-%d %H:%M:%S")}


@app.post("/chatgpt")
def read_item(chatgpt_input: ChatGPTInput):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは学校の先生です。"},
            {"role": "user", "content": chatgpt_input.message},
        ]
    )
    return {"answer": res["choices"][0]["message"]["content"]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
