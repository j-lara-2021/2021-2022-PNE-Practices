from client0 import Client
import termcolor
import socket
print(f"-----| Practice 3, Exercise 7 |------")
IP = "127.0.0.1"
PORT = 6123
c = Client(IP, PORT)
print("* Testing PING...")
c.talk("PING")
print("* Testing GET...")
for i in range(0,4):
    c.talk(f"GET {i}")
get0 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
cmds = ["INFO", "COMP", "REV", "GENE"]
genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
m = 0
for l in cmds:
    print(f"* Testing {cmds[m]}...")
    m += 1
    if l == "GENE":
        for g in genes:
            c.talk(f"{l} {g}")
    else:
       c.talk(f"\n{l} {get0}")




