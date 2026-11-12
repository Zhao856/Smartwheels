import threading
import json
import socket
import queue
import time
from socket import socket

def get_local_ip():
    """Return this machine's current LAN IPv4 address.

    Run it on the Pi to find out what IP address it is currently using
    (e.g. when DHCP hands it a new one). Falls back to "127.0.0.1" if no
    network route can be found.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No data is actually sent; this only picks the interface that
        # would route to the internet, i.e. the one on your LAN.
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


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

