import http.client
import json
import http.server
from pathlib import Path
import jinja2 as j

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

def read_html_file(filename):
    contents = Path("./html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
class Seq:
    def __init__(self, strbases = "NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

    def count_base_dict(self):
        base_dict = {}
        A = self.strbases.count("A")
        T = self.strbases.count("T")
        C = self.strbases.count("C")
        G = self.strbases.count("G")
        if self.strbases != "ERROR" and self.strbases != "NULL":
            base_dict["A"] = A
            base_dict["C"] = C
            base_dict["T"] = T
            base_dict["G"] = G
        else:
            pass
        return base_dict

    def base_perc(dict):
        perc_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        total = sum(dict.values())
        for k, v in dict.items():
            perc_dict[k] = str(round(v * 100 / total, 2)) + "%"

        return perc_dict ,total