FROM python:3.9.12

WORKDIR /
COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p "tmp"
