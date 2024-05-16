FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD cd src/app/ && gunicorn -b 0.0.0.0:8000 main:app