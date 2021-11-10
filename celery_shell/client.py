import socket
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str)
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-o', '--operacion', type=str, choices=['suma', 'resta', 'mult', 'div', 'pot'])
    parser.add_argument('-n', type=float)
    parser.add_argument('-m', type=float)

    args = parser.parse_args()  

    SERVER = args.host
    PORT = args.port
    OPERACION = args.operacion
    N = args.n
    M = args.m

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((SERVER, PORT))

    datos = bytes(f'{OPERACION}|{N}|{M}', 'utf-8')

    cliente.send(datos)
    output = cliente.recv(2048).decode('utf-8')
    print(output)
