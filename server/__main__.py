import socket
import encrypt

key = ""
def Command(command):
    command = command.lower
    if command != "":
        return encrypt.encrypt_data('Connected to server',key)

def Main():
    host = '' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        decrypt_data = encrypt.decrypt_data(data,key)
        print("Message from: " + str(addr))
        print("From connected user: " + decrypt_data)
        s.sendto(Command(decrypt_data),addr)
    s.close()

if __name__=='__main__':
    Main()