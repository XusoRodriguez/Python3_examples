import socket

# ===== [ SERVER ] ======================================

def Main():
    # We define two variables, a host and a port
    host = "127.0.0.1"
    port = 5000

    # we define a variable mySocket which 
    # is an instance of a Python socket 
    mySocket = socket.socket()
    mySocket.bind((host,port))

    # we call the listen method and pass 1 
    # to it so that it will perpetually listen 
    # till we close the connection 
    mySocket.listen(1)
    print("Waitting...")
    # we have two variables conn and addr which 
    # will hold the connection from client and 
    # the address of the client
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    # We run all this in a while true loop so 
    # unless the the connection is closed we 
    # run this and server’s keeps on listening 
    # when the data is received server transforms 
    # in into uppercase by calling upper method 
    # and sends the string back to client and we 
    # encode too as normal string will fail to 
    # transmit properly
    while True:
      data = conn.recv(1024).decode()
      if not data:
        break
      print ("from connected  user: " + str(data))
             
      data = str(data).upper()
      print ("sending: " + str(data))
      conn.send(data.encode())

    # When it ends the loop, we close the connection         
    conn.close()
     
if __name__ == '__main__':
    Main()