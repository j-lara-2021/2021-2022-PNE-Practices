import http.server
import socketserver
import seq_functions as seq
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["ATGAGCGAGGTTATA", "GGGATCGAGAGCTAGC", "ATGCTAGGGACCCC", "TAGCTAGTCAGCCCGGGTT", "GGGTTACTTATCAC"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 4876
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        route = self.path
        if path == "/":
            contents = read_html_file("index.html")\
                .render(context={"n_sequences": len(LIST_SEQUENCES), "genes": LIST_GENES})
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context={"n_sequence": n_sequence, "sequence": sequence})
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = Path("./genes/" + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html") \
                .render(context={"gene_name": gene_name, "sequence": sequence})
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html") .render(context={"operation": operation, "sequence": sequence[::-1])
            elif

                """when you pass info opertaion string to html write <br> instead of \n or embed them in a <p>"""



        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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