FROM debian:bookworm-slim

WORKDIR /app

COPY . .

RUN chmod +x ./build/tonutils-reverse-proxy

CMD ["./build/tonutils-reverse-proxy"]
