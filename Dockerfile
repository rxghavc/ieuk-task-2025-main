FROM python:3.11-slim
WORKDIR /app
COPY analyze_log.py ./
COPY sample-log.log ./
ENTRYPOINT ["python", "analyze_log.py"]