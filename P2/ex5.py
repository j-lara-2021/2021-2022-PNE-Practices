from Client0 import Client
from Seq1 import Seq
import termcolor
import socket
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8000

# -- Create a client object
c = Client(IP, PORT)

print(c)
m = Seq()
m.seq_read_fasta("FRAT1")
x = 0
n = 1
c.talk(f"Sending FRAT1 Gene to the server, in fragments of 10 bases...")
print(f"Gene FRAT1: {m.strbases}")
while x < 50:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(f"Fragment {n} {m.strbases[x: x + 10]}"))
    termcolor.cprint(f"Fragment {n}: {m.strbases[x: x + 10]} ")
    msg = s.recv(2048)
    x += 10
    n += 1