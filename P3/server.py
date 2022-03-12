import socket
import termcolor
sequences = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configure the Server's IP and PORT
PORT = 6123
IP = "0.0.0.0"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ Server configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for clients....")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode().replace("\n", "").strip().upper()

        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        if cmd != "PING":
            arg = splitted_command[1]
        termcolor.cprint(f"{cmd}", "green")
        if cmd == "PING":
            response = "OK!\n"
            print(response)

        elif cmd == "GET":
            arg = int(arg)
            response = f"GET {arg}: " + sequences[arg]
            print(response)

        elif cmd == "INFO":
            print(f"New sequence created! \n")
            d = {"A": 0, "C": 0, "G": 0, "T": 0, "A%": 0, "C%": 0,"G%": 0, "T%": 0 }
            for b in arg:
                d[b] += 1
                d[b + "%"] = round((d[b] / len(arg) * 100),2)
            response = f"Sequence: {arg}\nTotal length: {len(arg)}\n A: {d['A']} ({d['A%']} %)\n C: {d['C']} ({d['C%']} %)\n G: {d['G']} ({d['G%']} %)\n T: {d['T']} ({d['T%']} %)\n"
            print(response)

        elif cmd == "COMP":
            response = arg.replace('C', 'g').replace("G", "c").replace("A", "t").replace("T", "a").upper()
            print(f"New sequence created! \n"
            f"COMP {response}")
        elif cmd == "REV":
            response = arg[::-1]
            print(f"New sequence created! \n"
                  f"REV {response}")
        elif cmd == "GENE":
            f = open("./sequences/" + arg + ".txt", "r").read()
            gene = f[f.find("\n"):].replace("\n", "")
            response = f"GENE {arg}\n {gene}"
            print(f"NULL Seq created \n"
                  f"{response}")
        else:

            # -- Send a response message to the client
            response = "This command is not available in the server.\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()