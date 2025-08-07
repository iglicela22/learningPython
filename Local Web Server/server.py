from http.server import SimpleHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8000

server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Serving HTTP on {host}:{port}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server.")
    server.server_close()
