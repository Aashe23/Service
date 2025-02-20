FROM python:3.9-slim

WORKDIR /app

COPY frontend.py /app/
RUN pip install --no-cache-dir flask requests
CMD ["python", "frontend.py"]