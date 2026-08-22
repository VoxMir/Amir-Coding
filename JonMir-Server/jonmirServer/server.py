import json
from http.server import HTTPServer, BaseHTTPRequestHandler

correct_username = "jonmir"
correct_password = "admin"

access_token = "Admin123"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def end_headers(self):
        # Inject the allow all origins header
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)

            email = data.get("email")
            pwd = data.get("password")

            if email == correct_username and pwd == correct_password:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                response = {
                    "success": True,
                    "access_token": access_token
                }
            else:
                self.send_response(401)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                response = {
                    "success": False,
                    "message": "Invalid username or password"
                }

        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response = {
                "success": False,
                "message": "Invalid JSON"
            }

        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_GET(self):
        # Send a 200 OK response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Write the HTML content to the page
        response = "<html><body><h1>Hello from Python!</h1></body></html>"
        self.wfile.write(bytes(response, "utf-8"))


# Configure and run the server
server_address = ('10.86.219.171', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server running on http://10.86.219.171:8000")
httpd.serve_forever()