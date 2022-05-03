import http.client
import json
import socketserver
import utilities as u
import http.server
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
ARGUMENT = "?content-type=application/json"
SERVER = 'rest.ensembl.org'
PORT = 8080


socketserver.TCPServer.allow_reuse_address = True

# Connect with the server
conn = http.client.HTTPConnection(SERVER)


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Message to send back to the clinet
        try:
            url = urlparse(self.path)
            path = url.path
            arguments = parse_qs(url.query)

            if self.path == "/":
                contents = u.read_html_file("index.html").render()
            elif path == "/listSpecies":
                n_species = arguments["number_species"]  # check what happens if input empty !!!
                dict_answer = u.make_ensmbl_request("/info/species", ARGUMENT)  # + "&" + "species=homo_sapiens"
                list_species = dict_answer["species"]
                list_species = list_species[0:int(n_species)]
                content = u.read_html_file("html/listSpecies.html").render(context={"species": list_species})

            else:
                contents = open("html/error.html", "r").read()

            # Generating the response message
            self.send_response(200)  # -- Status line: OK!

            # Define the content-type header:
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(contents.encode())
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

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
