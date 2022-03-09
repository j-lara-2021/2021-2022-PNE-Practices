import socket
import termcolor
sequences = ["AAATTATATTAGGCCC", "AGGCTACTATATGGA", "AAGGGCACGGCGAGCGAG", "AGCTTAGTGTAGTAGATGATAG", "AGGGGAGGAGAGGAGTA"]
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
        msg = msg_raw.decode().replace("\n", "").strip()
        termcolor.cprint(f"{msg} command!", "green")
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]

        if cmd == "PING":
            response = "OK!\n"
            print(response)
        elif cmd == "GET":
            arg = int(splitted_command[1])
            response = sequences[arg]
        elif cmd == "INFO":
            arg = splitted_command[1]
            print(f"sequence: {arg}")
            d = {"A": 0, "C": 0, "G": 0, "T": 0, "A%": 0, "C%": 0,"G%": 0, "T%": 0 }
            for b in arg:
                d[b] += 1
                d[b + "%"] = d[b] / len(arg) * 100
            response = f" A: {d['A']} ({d['A%']} %)\n C: {d['C']} ({d['C%']} %)\n G: {d['G']} ({d['G%']} %)\n T: {d['T']} ({d['T%']} %)\n"
            print(f"Total length: {len(arg)}")
            print(response)
        else:

            # -- Send a response message to the client
            response = "This command is not available in the server.\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()