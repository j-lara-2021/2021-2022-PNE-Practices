import http.server
import socketserver
import termcolor
PORT = 4876
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        route = self.path
        sequences = ["ATGAGCGAGGTTATA", "GGGATCGAGAGCTAGC", "ATGCTAGGGACCCC", "TAGCTAGTCAGCCCGGGTT", "GGGTTACTTATCAC"]
        if route == "/":
            body = open("html/form-1.html", "r").read()
        elif route == "/favicon.ico":
            body = open("html/form-1.html", "r").read()
        else:
            try:
                filename = route.split("=")
                if len(filename) == 1:
                    body = open("html/form-1.html", "r").read()
                else:
                    seq_num = filename[1].split("&")[1]
                    filename = str(filename[-1]).strip("/")

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