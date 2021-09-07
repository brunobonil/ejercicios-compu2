import socket
import argparse
import os

SERVER = '0.0.0.0'


def tcp():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER, args.port))
    server.listen()
    conn, addr = server.accept()

    print(f'Nueva conexión TCP: {addr}')
    while True:
        data = conn.recv(2048)
        if data == b'':
            conn.close()
            break
        os.write(fd, data)

def udp():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((SERVER, args.port))

    print(f'Nueva conexión UDP')
    while True:
        data, addr = server.recvfrom(2048)
        if data == b'':
            server.close()
            break
        os.write(fd, data)
    

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int)
parser.add_argument('-t', '--transporte', type=str)
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

fd = os.open(args.file, os.O_RDWR | os.O_CREAT)
if args.transporte == 'tcp':
    tcp()
elif args.transporte == 'udp':
    udp()

