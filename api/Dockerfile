FROM --platform=linux/amd64 python:3.11.2-bullseye

WORKDIR /src

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python - && \
    cd /usr/local/bin && \
    ln -s $POETRY_HOME/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app.py /src

CMD ["python", "app.py"]
