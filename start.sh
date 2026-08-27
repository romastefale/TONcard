```bash
#!/bin/sh

set -e

echo "Starting TONcard upstream..."

python /app/main.py &
PYTHON_PID=$!

echo "Starting TON reverse proxy with ADNL tunnel..."

exec /app/tonutils-reverse-proxy --enable-tunnel
```
