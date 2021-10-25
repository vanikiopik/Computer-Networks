import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_address = ("localhost", 10000)


def ConnectToServer():
    try:
        message = input("Enter the word: ")
        sock.sendto(bytes(message, encoding='UTF-8'), server_address)
        data, address = sock.recvfrom(1024)
        print("Was found: ", data.decode(), " letters in word 'Windows'")
    except:
        print("Server closed")
        exit()


def Start():
    while True:
        ConnectToServer()


Start()
