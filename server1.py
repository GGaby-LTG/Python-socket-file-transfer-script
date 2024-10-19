
import socket 
import os
ad = r"E:\\"
if __name__ == '__main__': 
    # Defining Socket 
    host = '192.168.1.129'
    port = 8080
    totalclient = 1
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.bind((host, port)) 
    sock.listen(totalclient) 
    # Establishing Connections 
    connections = [] 
    print('Initiating clients') 
    for i in range(totalclient): 
        conn = sock.accept() 
        connections.append(conn) 
        print('Connected with client', i+1) 
  
    fileno = 0
    idx = 0
    while  True: 
        try:
            filename = conn[0].recv(1024).decode()
                # Reading file and sending data to server 
            try:
                 sizes = os.path.getsize(filename)
                 print(sizes)
                 size = sizes // 128 +1
                 if size ==0:
                    size = 1
                 print(size)
                 conn[0].send(str(size).encode())
                 file = open(filename, 'rb')
                 b = file.read(819600000)
                 if not b:
                        break
                 for ix in range(size):
                    conn[0].send(b)
                 print("done")
            except:
                print("upload failed")
        except:  
            conn = sock.accept() 
            connections.append(conn) 
            print('Connected with client', i+1) 