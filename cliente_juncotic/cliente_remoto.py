import socket, argparse

# hello|<nombre>
# email|<correo_electronico>
# key|<clave_hardodeada>
# exit
FORMAT = 'utf-8'
HOST = str(socket.gethostbyname(socket.gethostname()))

# 200: OK
# 400: Comando válido, pero fuera de secuencia.
# 500: Comando inválido.
# 404: Clave errónea.
# 405: Cadena nula.

def send():
    while True:
        name = 'hello|' +  str(input("Nombre: "))
        cliente.send(name.encode(FORMAT))

        resp = cliente.recv(512).decode(FORMAT)
        if resp != "200":
            print(resp + ': Comando válido, pero fuera de secuencia.')
        else:
            print('200: OK')

        email = 'email|' + str(input("Correo electrónico: "))
        cliente.send(email.encode(FORMAT))

        resp = cliente.recv(512).decode(FORMAT)
        if resp != "200":
            print(resp + ': Comando válido, pero fuera de secuencia.')
        else:
            print('200: OK')
           
        key = 'key|' + str(input("Ingrese clave: "))
        cliente.send(key.encode(FORMAT))

        resp = cliente.recv(512).decode(FORMAT)
        if resp != "200":
            print(resp + ': Clave errónea.')
        else:
            print('200: OK')

        fin = str(input("Ingrese el comando para abandonar la sesión: "))
        cliente.send(fin.encode(FORMAT))
        
        resp = cliente.recv(512).decode(FORMAT)
        if resp != "200":
            print(resp + ': Comando inválido.')
        else:
            print('200: OK')
            break


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--host', type=str, default=HOST)
parser.add_argument('-p', '--port', type=int, required=True)
args = parser.parse_args()

address = (args.host, args.port)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(address)
send()