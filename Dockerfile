FROM python:3.8

WORKDIR /app

COPY weather.py .

RUN pip install requests

CMD [ "python", "main.py" ]