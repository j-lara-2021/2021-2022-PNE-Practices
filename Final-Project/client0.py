import socket
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return(f"Connection to SERVER at {self.ip}, PORT: {self.port}")

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        arguments = s.recv(2048).decode("utf-8")
        return arguments

    def talk(self,msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")
        print(response)
        # Close the socket
        s.close()

        # Return the response
        return response

