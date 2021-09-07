import socket
import argparse
import os


def tcp():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((args.address, args.port))
    while True:
        data = os.read(0, 4096)
        data = data.decode('utf-8')
        cliente.send(data.encode('utf-8'))
        if data == '':
            cliente.close()
            break

def udp():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = os.read(0, 4096)
        cliente.sendto(data, (args.address, args.port))
        if data == b'':
            cliente.close()
            break


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', type=str)
parser.add_argument('-p', '--port', type=int)
parser.add_argument('-t', '--transporte', type=str)
args = parser.parse_args()

if args.transporte == 'tcp':
    tcp()
elif args.transporte == 'udp':
    udp()