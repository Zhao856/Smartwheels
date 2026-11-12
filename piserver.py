from softnet import Server

server= Server(50007)

while True:
    dic = server.recieve()
    if dic != None:
        print(dic)
    
