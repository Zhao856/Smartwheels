from softnet import Server
from softnet import get_local_ip
# Report the Pi's current IP so you always know what address to reach it on
# (useful when DHCP changes the address between boots).
print("Pi is listening on", get_local_ip(), "port 50007")

server = Server(50007)
server= Server(50007)

while True:
    dic = server.recieve()
    if dic != None:
        print(dic)
    
