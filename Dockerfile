FROM python:3.10-slim

WORKDIR /app

COPY monitor.py .

RUN pip install flask psutil

CMD ["python", "monitor.py"]
