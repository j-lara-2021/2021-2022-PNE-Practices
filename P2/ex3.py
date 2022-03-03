from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8000

# -- Create a client object
c = Client(IP, PORT)

print(c)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
termcolor.cprint(f"Response: {response}", "magenta")
