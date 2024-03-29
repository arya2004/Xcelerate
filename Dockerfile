FROM python:3.7-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y



RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]