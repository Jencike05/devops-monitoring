FROM python:3.10-slim

WORKDIR /app

COPY monitor.py monitor.py

RUN pip install psutil

CMD ["python", "monitor.py"]
