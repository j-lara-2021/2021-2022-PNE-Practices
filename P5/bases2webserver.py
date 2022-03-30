import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the clinet
        route = self.path
        if route == "/":
            # This new contents are written in HTML language
            body = open("html/index.html", "r").read()
        elif route == "/favicon.ico":
            body = open("html/index.html", "r").read()
        else:
            try:
                filename = route.replace("/", "").split(".")[0]
                try:
                    body = open("html/" + filename + ".html", "r").read()

                except FileNotFoundError:
                    body = open("html/error.html", "r").read()
            except IndexError:
                body = open("html/error.html", "r").read()

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(body.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()