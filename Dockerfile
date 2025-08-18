FROM python:3.11-slim

WORKDIR /api

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "stockapi.wspi:application", "--bind", "0.0.0.0:8000"]