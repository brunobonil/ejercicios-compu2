import socket
import argparse
from calculadora import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str)
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args() 

    SERVER = args.host
    PORT = args.port

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER, PORT))
    server.listen()
  

    while True:
        conn, address = server.accept()
        command = conn.recv(2048).decode('utf-8').split('|')
        
        op = eval(command[0])
        n = float(command[1])
        m = float(command[2])

        solve = op.delay(n,m)

        resultado = solve.get(timeout=3)

        conn.send(bytes(resultado))
        conn.close()

