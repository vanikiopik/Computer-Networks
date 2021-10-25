import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)  # Set the protocol parameters to socket
server_address = ("localhost", 10000)  # Local address of the server
sock.bind(server_address)  # Set socket with  address
sock.listen(10)  # Maximum incoming requests, that can be processed
print("Server starting")


def Connect():
    connection, address = sock.accept()
    try:
        print("Connected to: ", address)
        while True:
            First_number = int(CheckForNumbers(connection.recv(1024).decode()))  # Getting info from the client
            Second_number = int(CheckForNumbers(connection.recv(1024).decode()))  # And check for the right input

            if First_number == 0 and Second_number == 0:  # Check for useless parameters
                connection.send(bytes("Error input", encoding='UTF-8'))
                pass
            else:
                data = str(DoFactorial(int(First_number), int(Second_number)))  # Make calc. and return at str format
                connection.send(bytes(data, encoding='UTF-8'))  # Send the processed data to the client
                pass
    except:
        print("User disconnected")
        connection.close()


def CheckForNumbers(m):  # Check the parameters for correct input
    if m.isdigit():
        return str(m)
    else:
        return 0


def DoFactorial(m, n):  # Makes m! + n!
    return math.factorial(m) + math.factorial(n)


while True:
    Connect()  # Starting the program
