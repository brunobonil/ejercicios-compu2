import socket
import argparse
import os
import datetime
import pickle

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 8080

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((SERVER, PORT))

def enviar():
    while True:
        mensaje = input("Ingrese el comando: ")
        if mensaje == 'exit':
            print('Se ha finalizado la conexión')
            cliente.send(pickle.dumps(mensaje))
            cliente.close()
            break
        cliente.send(pickle.dumps(mensaje))
        output = cliente.recv(2048).decode('utf-8')
        print(output)
        if args.log:
            fd = os.open(args.log, os.O_RDWR | os.O_CREAT)
            os.write(fd, pickle.dumps(output))
            fecha = str(datetime.datetime.today())
            os.write(fd, pickle.dumps(fecha))


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log', type=str, help='Crea un archivo donde se almacenará el log de la sesión')
args = parser.parse_args()
enviar()
