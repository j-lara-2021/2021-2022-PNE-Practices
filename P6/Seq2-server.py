import http.server
import socketserver
import seq_functions as seq
import termcolor
PORT = 4876
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
sequences = ["ATGAGCGAGGTTATA", "GGGATCGAGAGCTAGC", "ATGCTAGGGACCCC", "TAGCTAGTCAGCCCGGGTT", "GGGTTACTTATCAC"]
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        route = self.path
        if route == "/":
            body = open("html/form-1.html", "r").read()
        elif route == "/favicon.ico":
            body = open("html/form-1.html", "r").read()
        else:
            try:
                filename = route.split("=")
                method = filename[-1].strip("/").upper()
                if method == "PING":
                    body = seq.ping(method)
                elif method == "GET":
                    body =  seq.get(filename,method,sequences)
                elif method == "GENE":
                    body = seq.gene(filename)
                elif method == "INFO" or method == "COMP" or method == "REV":
                    body = seq.operate(method,filename)
                else:
                    body = open("html/error.html", "r").read()
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