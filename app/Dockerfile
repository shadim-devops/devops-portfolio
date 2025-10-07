
# syntax=docker/dockerfile:1

FROM python:3.12-slim AS base
WORKDIR /app

# Install prod deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py ./

EXPOSE 8000
CMD ["python", "app.py"]
