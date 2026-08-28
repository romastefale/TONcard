FROM python:3.13-slim

WORKDIR /app

COPY main.py index.html ./

ENV PORT=8080
EXPOSE 8080

CMD ["python", "main.py"]
