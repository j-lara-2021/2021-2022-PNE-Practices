import http.client
import json
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
    #print the received data
    print(f"Gene: MIR633 \nDescription: {data1['desc']}\nBases: {data1['seq']}")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

