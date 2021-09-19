import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.connect(("localhost", 10000))  # Connect to local server


while True:
    try:
        First_number = input("Enter the first number: ")
        Second_number = input("Enter the second number: ")
        sock.send(bytes(First_number, encoding='UTF-8'))  # Send data to server
        sock.send(bytes(Second_number, encoding='UTF-8'))
        data = sock.recv(1024).decode()  # Receive processed data from server
        print("Server respond: ", data)
    except ConnectionResetError:  # Closing the connection if server shut down
        print("Server shut down the connection")
        sock.close()  # Closing the socket
        break  # Stop the program
