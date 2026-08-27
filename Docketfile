```dockerfile
FROM golang:1.26-bookworm AS builder

WORKDIR /src

RUN git clone https://github.com/tonutils/reverse-proxy.git .

RUN make build


FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /src/build/tonutils-reverse-proxy /app/tonutils-reverse-proxy

COPY main.py /app/main.py
COPY start.sh /app/start.sh

RUN chmod +x /app/tonutils-reverse-proxy /app/start.sh

CMD ["/app/start.sh"]
```
