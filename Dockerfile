FROM python:3.11-slim

# Install system dependencies BEFORE Python packages
RUN apt-get update && apt-get install -y ffmpeg nodejs npm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "yt2radarr.py"]
