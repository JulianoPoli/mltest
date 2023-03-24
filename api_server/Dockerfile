FROM python:slim

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

EXPOSE 1235

ENTRYPOINT [ "python", "api_server.py" ]