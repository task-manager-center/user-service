FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

RUN echo hello

RUN pytest -s -vvv

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:88", "--workers", "4", "--worker-class", "aiohttp.GunicornWebWorker"]
