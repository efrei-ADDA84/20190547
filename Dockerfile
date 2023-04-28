FROM python:3.8



WORKDIR /app



COPY main.py .


RUN pip install requests
RUN pip install fastapi
RUN pip install uvicorn



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]