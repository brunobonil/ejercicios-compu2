import socket, argparse


FORMAT = 'utf-8'
HOST = str(socket.gethostbyname(socket.gethostname()))


def send():
    stage = 0
    while True:
        if stage == 0:
            name = 'hello|' +  str(input("Nombre: "))
            cliente.send(name.encode(FORMAT))

            resp = cliente.recv(512).decode(FORMAT)
            if resp != "200":
                print(resp + ': Comando válido, pero fuera de secuencia.')
            else:
                stage += 1
                print('200: OK')

        if stage == 1:
            email = 'email|' + str(input("Correo electrónico: "))
            cliente.send(email.encode(FORMAT))

            resp = cliente.recv(512).decode(FORMAT)
            if resp != "200":
                print(resp + ': Comando válido, pero fuera de secuencia.')
            else:
                stage += 1
                print('200: OK')

        if stage == 2:
            key = 'key|' + str(input("Ingrese clave: "))
            cliente.send(key.encode(FORMAT))

            resp = cliente.recv(512).decode(FORMAT)
            if resp != "200":
                print(resp + ': Clave errónea.')
            else:
                stage += 1
                print('200: OK')

        if stage == 3:
            fin = str(input("Ingrese el comando para abandonar la sesión: "))
            cliente.send(fin.encode(FORMAT))
            
            resp = cliente.recv(512).decode(FORMAT)
            if resp != "200":
                print(resp + ': Comando inválido.')
            else:
                stage += 1
                print('200: OK')
                cliente.close()
                break


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--host', type=str, default=HOST)
parser.add_argument('-p', '--port', type=int, required=True)
args = parser.parse_args()

address = (args.host, args.port)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(address)
send()