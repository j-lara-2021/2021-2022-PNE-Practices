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
for i in genes:
    m = Seq()
    m.seq_read_fasta(i)

    print("To Server:", end = " ")
    termcolor.cprint(f"Sending {i} to the server...", "blue")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(f"Sending {i} to the server..."))
    msg = s.recv(2048)
    c.talk(m.strbases)
    print("From Server:", end = " ")
    termcolor.cprint(msg.decode("utf-8"), "red")
    print("To Server:", end = " ")
    termcolor.cprint(m, "cyan")
    print("From Server:")
    termcolor.cprint(msg.decode("utf-8"), "green")
