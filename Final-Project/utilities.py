import http.client
import json
import socketserver
import http.server
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
ARGUMENT = "?content-type=application/json"
def make_ensmbl_request(url,params):
    SERVER = 'rest.ensembl.org'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url + params)  # We do not need to put the server
    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    return json.loads(data1)


"""url = urlparse(self.path)
path = url.path
arguments = parse_qs(url.query)
if path == "/listSpecies":
    n_species = arguments["number_species"]#check what happens if input empty !!!
    dict_answer = make_ensmbl_request("/info/species", ARGUMENT) #+ "&" + "species=homo_sapiens"
    list_species = dict_answer["species"]
    list_species = list_species[0:int(n_species)]
    content = read_html_file("html/" + filename + ".html").render(context = {"species": list_species})"""



def read_html_file(filename):
    contents = Path("./html/" + filename).read_text()
    contents = j.Template(contents)
    return contents