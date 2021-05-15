import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

sock.send(b'ready')
while True:

    mes = input(': ')


    sock.send(bytes(mes))
    data = sock.recv(1024)
    print(data)
    if mes == '0': break


sock.close()




