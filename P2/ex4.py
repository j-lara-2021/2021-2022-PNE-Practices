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

genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for i in range(0,len(genes)):
    filename = genes[i]
    i = Seq()
    print("To Server:")
    termcolor.cprint(f"Sending {filename} to the server...", "blue")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(f"Sending {filename} to the server..."))
    msg = s.recv(2048)
    print("From Server:")
    termcolor.cprint(msg.decode("utf-8"), "green")
    print("To Server:")
    termcolor.cprint(i.seq_read_fasta(filename), "cyan")
