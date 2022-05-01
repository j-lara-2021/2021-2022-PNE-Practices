import http.client
import json
from Seq1 import Seq
def base_perc(d):
    p = {"A": 0, "C": 0, "G": 0, "T": 0}
    total = sum(d.values())
    for k, v in d.items():
        p[k] = v * 100 / total
    return p
def convert_message(d, p):
    message = ""
    for k, v in d.items():
        message += k + ": " + str(v) + " (" + str(round(p[k], 2)) + "%)" + "\n"
    return message


id_dict = {"FRAT1": " ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
          "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
           "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
           "ANK2": "ENSG00000145362"}


#PORT = 4876 not needed
SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/ENSG00000207552"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print(f"SERVER: {SERVER}\n")
print(f"URL: {URL}\n")


# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS) #We do not need to put the server
    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    seq = Seq(data1['seq'])
    dic = seq.count_bases()
    perc = base_perc(dic)
    info = convert_message(dic, perc)
    for gene, v in id_dict.items():
        print(f"Gene: {gene} \nDescription: {data1['desc']} "
              f"\nLength: {seq.len()}\n{info}Most frequent base: {seq.most_common_base()}")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()