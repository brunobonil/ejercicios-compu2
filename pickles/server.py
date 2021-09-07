import socket
import threading
import subprocess
import pickle

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def manejo_cliente(conn, address):
    print(f'Nueva conexión: {address}')
    while True:
        command = pickle.loads(conn.recv(2048))
        if command == 'exit':
            server.close()
            break
        out = subprocess.run(command.split(), capture_output=True)
        if out.returncode != 0:
            conn.send(pickle.dumps((f'\n[ERROR]\n{pickle.loads(out.stderr)}')))
        else:
            conn.send(pickle.dumps(f'\n[OK]\n{pickle.loads(out.stdout)}'))


def start():
    server.listen()
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=manejo_cliente, args=(conn, address))
        thread.start()

print("*SERVIDOR INICIALIZADO*")
start()

