import http.server
import socketserver
import ssl

# Specify the certificate and key file
certfile = "server.pem"

# Define the port for your HTTPS server
port = 443

Handler = http.server.SimpleHTTPRequestHandler

# Create an HTTP server with SSL support
httpd = socketserver.TCPServer(("0.0.0.0", port), Handler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, server_side=True)

print(f"Serving on port {port}...")

# Start the server
httpd.serve_forever()

