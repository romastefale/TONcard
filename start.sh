#!/bin/sh
set -e

PORT="${PORT:-8080}"
export PORT

echo "Starting TONcard static/proxy server on 0.0.0.0:${PORT}..."
python /app/main.py &
PYTHON_PID=$!

trap 'kill "$PYTHON_PID" 2>/dev/null || true' EXIT INT TERM

if [ -x /app/tonutils-reverse-proxy ]; then
  echo "Starting TON reverse proxy..."
  exec /app/tonutils-reverse-proxy --domain romastefale.ton
fi

echo "tonutils-reverse-proxy not found; serving HTTP only"
wait "$PYTHON_PID"
