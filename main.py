import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UPSTREAM = "https://romastefale.github.io/TONcard"
PORT = int(os.environ.get("PORT", "8080"))


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        path = self.path or "/"
        target = UPSTREAM.rstrip("/") + ("/" if path == "/" else path)

        try:
            req = Request(
                target,
                headers={"User-Agent": "TONcard-Proxy/1.0"}
            )

            with urlopen(req, timeout=30) as response:
                body = response.read()

                self.send_response(response.status)
                self.send_header(
                    "Content-Type",
                    response.headers.get(
                        "Content-Type",
                        "application/octet-stream"
                    )
                )
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        except HTTPError as e:
            self.send_response(e.code)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"HTTP {e.code}".encode())

        except (URLError, TimeoutError, Exception) as e:
            self.send_response(502)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Upstream error: {e}".encode())

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)

print(f"Listening on 0.0.0.0:{PORT}", flush=True)
print(f"Upstream: {UPSTREAM}", flush=True)

server.serve_forever()
