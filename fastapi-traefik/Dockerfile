# Dockerfile
FROM python:3.11.1-slim

WORKDIR /app

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN apt-get install -y libpq-dev python3-dev

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY . /app/

ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--port", "8080", "--host", "0.0.0.0"]
