#!/bin/bash
set -e
export PORT="${PORT:-3000}"

# 1. Start Node Server in background
echo "Starting TONcard Node.js server on 0.0.0.0:${PORT}..."
node server.js &
NODE_PID=$!

trap 'kill "$NODE_PID" 2>/dev/null || true' EXIT INT TERM

# 2. Run ADNL Reverse Proxy
if [ -d "./reverse-proxy" ]; then
    echo "Checking for tonutils-reverse-proxy binary..."
    if [ ! -f ./tonutils-reverse-proxy ]; then
        echo "Downloading tonutils-reverse-proxy..."
        ARCH=$(uname -m)
        if [ "$ARCH" = "aarch64" ]; then
            PROXY_BIN="tonutils-reverse-proxy-linux-arm64"
            echo "Detected ARM64 architecture (Termux/Mobile)..."
        else
            PROXY_BIN="tonutils-reverse-proxy-linux-amd64"
            echo "Detected AMD64 architecture..."
        fi
        wget -q -O ./tonutils-reverse-proxy "https://github.com/tonutils/reverse-proxy/releases/download/v0.6.0/${PROXY_BIN}"
        chmod +x ./tonutils-reverse-proxy
    fi
    echo "Starting TON reverse proxy..."
    cd ./reverse-proxy
    # The proxy will use config.json in the reverse-proxy folder and proxy to 127.0.0.1:3000
    exec ../tonutils-reverse-proxy --domain romastefale.ton
else
    echo "No reverse-proxy folder found, serving HTTP only."
fi

wait "$NODE_PID"
