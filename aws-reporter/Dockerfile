FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Security — create non-root user
RUN useradd -m appuser
USER appuser

CMD ["python3", "app.py"]
