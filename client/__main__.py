import socket
import sys
import encrypt

key = ""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

def Main():
    try:

        host = ip #Client ip
        port = 4005
        

        server = ('192.168.4.200', 4000)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
        
        message = input("-> ")
        while message != 'q':
            cryptmsg = encrypt.encrypt_data(message,key)
            s.sendto(cryptmsg, server)
            data, addr = s.recvfrom(1024)
            data = encrypt.decrypt_data(data,key)
            print("Received from server: " + data)
            message = input("-> ")
    except EOFError as error:
        exit()
    s.close()

if __name__=='__main__':
    Main()

