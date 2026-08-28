import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"
UPSTREAM = os.environ.get("UPSTREAM", "https://romastefale.github.io/TONcard").rstrip("/")
PORT = int(os.environ.get("PORT", "8080"))


def read_local_index():
    if INDEX.is_file():
        return INDEX.read_bytes()
    return None


def fetch_upstream(path: str):
    target = UPSTREAM + ("/" if path == "/" else path)
    req = Request(target, headers={"User-Agent": "TONcard-Proxy/1.1"})
    with urlopen(req, timeout=30) as response:
        return response.status, response.headers.get("Content-Type", "text/html; charset=utf-8"), response.read()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0] or "/"

        if path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        if path in ("/", "/index.html", "/TONcard", "/TONcard/"):
            body = read_local_index()
            if body is not None:
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

        try:
            status, content_type, body = fetch_upstream("/" if path in ("/", "/TONcard", "/TONcard/") else path)
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except HTTPError as exc:
            self.send_response(exc.code)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"HTTP {exc.code}".encode())
        except (URLError, TimeoutError, OSError) as exc:
            self.send_response(502)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"Upstream error: {exc}".encode())

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Listening on 0.0.0.0:{PORT}", flush=True)
    print(f"Local index: {INDEX if INDEX.is_file() else 'missing'}", flush=True)
    print(f"Upstream fallback: {UPSTREAM}", flush=True)
    server.serve_forever()
