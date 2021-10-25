import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_address = ("localhost", 10000)
sock.bind(server_address)


def Task(msg):  # Find the same letters and return their range
    const_word = "WINDOWS"
    msg = DeleteSameLetters(msg)
    n = 0  # Counter of duplicates
    for i in msg:
        if i in const_word:
            n += 1
    return n


def DeleteSameLetters(string):  # Delete duplicates form string
    result = []
    for i in string:
        if i not in result:
            result.append(chr(i))
    return ''.join(result)


def Work():
    print("Server working")
    while True:
        try:
            message, address = sock.recvfrom(1024)
            print(address, ": connected")
            print("Server got message: ", message.decode())
            Value = str(Task(message.upper()))
            sock.sendto(bytes(Value, encoding='UTF-8'), address)
        except:
            print("User disconnected")


Work()
