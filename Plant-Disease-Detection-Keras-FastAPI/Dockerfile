FROM python:3.8.13-slim-buster

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  python3-opencv \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools 
    
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD CMD uvicorn app:app --reload --host 0.0.0.0 --port 8000
