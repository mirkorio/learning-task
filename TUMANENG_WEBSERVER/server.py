# - server.py
# - certificate.pem
# - key.pem
# - html_files/
#     - index.html
#     - about.html
#     - contact.html



import http.server
import ssl
import os

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'html_files/index.html'
        elif self.path == '/resume':
            self.path = 'html_files/resume.html'
        elif self.path == '/blogs':
            self.path = 'html_files/blogs.html'
        elif self.path == '/services':
            self.path = 'html_files/services.html'
        elif self.path == '/contact':
            self.path = 'html_files/contact.html'
        elif self.path.endswith('.css'):
            self.path = 'styles' + self.path
        elif self.path.endswith('.js'):
            self.path = 'script' + self.path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


httpd = http.server.HTTPServer(('localhost', 8443), SimpleHTTPRequestHandler)
# Paths to the PEM certificate and private key
server_cert = "tumaneng.com-2024-04-30.crt"
server_key = "tumaneng.com-2024-04-30.key"

# Generate SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=server_cert, keyfile=server_key)

# Wrap the HTTP server with SSL/TLS
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print("Serving HTTPS on port 8443...")
httpd.serve_forever()
