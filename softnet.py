import threading
import json
import socket
import queue
import time
class Client:
    def __init__(self,HOST:str,PORT:int):
        self.HOST = HOST
        self.PORT = PORT
        self.que = queue.Queue()
        self.t = threading.Thread(target = self.__send)
        self.t.daemon = True
        self.t.start()


    def __send(self):
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.HOST, self.PORT))
                    while True:
                        message = self.que.get()
                        if message is None:
                            pass
                        json_data =json.dumps(message)
                        s.sendall(json_data.encode("utf-8"))
            except:
                print("could be connection issue")
                time.sleep(1)

    def send(self, message:dict):
        self.que.put(message)

    
    

class Server:
    def __init__(self,PORT,HOST=''):
        self.HOST = HOST
        self.PORT = PORT
        self.que = queue.Queue()
        self.t = threading.Thread(target = self.__receive)
        self.t.daemon = True
        self.t.start()
        




    def __receive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    try:
                        message = json.loads(data.decode("utf-8"))
                        print(message)
                        self.que.put(message)
                    except json.JSONDecodeError:
                        print("Invalid json")

    def recieve(self):
        return self.que.get()

    
