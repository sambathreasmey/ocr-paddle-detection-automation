FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# ✅ Install required system libs (FIX HERE)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --prefer-binary -r requirements.txt

COPY . .

CMD ["python", "ocr_script.py", "txn.jpeg"]