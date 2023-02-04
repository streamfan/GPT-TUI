FROM python:3.10

RUN mkdir /app 

COPY pyproject.toml /app 
COPY main.py /app
COPY chat.css /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN curl -fsSL https://get.pulumi.com | sh

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD ["python", "main.py"]