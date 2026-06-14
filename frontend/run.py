import http.server
import socketserver
import os, functools


# Define the port you want to use
PORT = 5090 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Use SimpleHTTPRequestHandler to serve files from the current directory
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=SCRIPT_DIR)

if __name__ == "__main__":
    # The allow_reuse_address guarantees we can reuse the port immediately
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}\nCTRL + Click on this link: [http://localhost:{PORT}/]...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by user.")