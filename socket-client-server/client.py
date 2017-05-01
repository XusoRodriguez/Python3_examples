import socket

# ===== [ CLIENT ] ======================================

def Main():
    # We define two variables, a host and a port
    host = '127.0.0.1'
    port = 5000

    # we define a variable mySocket which 
    # is an instance of a Python socket    
    mySocket = socket.socket()
    mySocket.connect((host,port))
         
    message = input(" -> ")

    # while the character typed is not “q” 
    # we keep running the loop and send the 
    # message by encoding it and when we received 
    # the processed data we decode it and print    
    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
                 
        print ('Received from server: ' + data)
                 
        message = input(" -> ")

    # When it ends the loop, we close the connection             
    mySocket.close()
 
if __name__ == '__main__':
    Main()