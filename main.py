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

        # Evita duplicar /TONcard
        if path == "/":
            url = UPSTREAM + "/"
        else:
            url = UPSTREAM + path

        try:
            req = Request(
                url,
                headers={
                    "User-Agent": "TON-Site-Proxy/1.0"
                }
            )

            with urlopen(req, timeout=30) as response:
                body = response.read()

                self.send_response(response.status)

                content_type = response.headers.get(
                    "Content-Type",
                    "application/octet-stream"
                )

                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()

                self.wfile.write(body)

        except HTTPError as e:
            self.send_response(e.code)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(
                f"Upstream HTTP error: {e.code}".encode()
            )

        except (URLError, TimeoutError, Exception) as e:
            self.send_response(502)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(
                f"Upstream error: {e}".encode()
            )

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)

print(f"Listening on 0.0.0.0:{PORT}", flush=True)
print(f"Upstream: {UPSTREAM}", flush=True)

server.serve_forever()
