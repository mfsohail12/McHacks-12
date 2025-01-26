import socket
import pickle
import json

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
            json_data = json.dumps(data).encode('utf-8')
            self.client.send(json_data)

            # print(self.client.recv(4096))
            # return json.loads(self.client.recv(4096).decode('utf-8'))
        except socket.error as e:
            print(e)

    # def receive(self):
    #     try:
    #         self.client.connect(self.addr)
    #         return pickle.loads(self.client.recv(2048))
    #     except Exception as e:
    #         print(f"Connection error: {e}")
    #         return None