import json
import http.client

SERVER = "localhost:8080"
PARAMS = "json=on"

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", "/listSpecies?limit=10&" + PARAMS)
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(data1)
except ConnectionRefusedError:
    print("Error, unable to connect to the server")