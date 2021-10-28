import socket
import argparse
import os
import datetime


PORT = 8080
SERVER = 'localhost'

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((SERVER, PORT))

def enviar():
    while True:
        mensaje = input("Ingrese el comando: ")
        if mensaje == 'exit':
            print('Se ha finalizado la conexión')
            cliente.send(mensaje.encode('utf-8'))
            cliente.close()
            break
        cliente.send(mensaje.encode('utf-8'))
        output = cliente.recv(2048).decode('utf-8')
        print(output)
        if args.log:
            fd = os.open(args.log, os.O_RDWR | os.O_CREAT)
            os.write(fd, output.encode('utf-8'))
            fecha = str(datetime.datetime.today())
            os.write(fd, fecha.encode('utf-8'))


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log', type=str, help='Crea un archivo donde se almacenará el log de la sesión')
args = parser.parse_args()
enviar()
