import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = "10.122.247.13"
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()
        # self.p = self.connect()
    
    # def getP(self):
    #     return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return
            # return pickle.loads(self.client.recv(8048))
        except Exception as e:
            print(f"Connection error: {e}")
            return None
    
    def send(self, data):
        try:
            import sys
            print(sys.getsizeof(data))
            self.client.sendall(pickle.dumps(data))
            return pickle.loads(self.client.recv(20000))
        except socket.error as e:
            print(e)

    # def receive(self):
    #     try:
    #         self.client.connect(self.addr)
    #         return pickle.loads(self.client.recv(2048))
    #     except Exception as e:
    #         print(f"Connection error: {e}")
    #         return None