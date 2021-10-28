import socket
import subprocess
import asyncio


PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

async def manejo_cliente(conn, address):
    print(f'Nueva conexión: {address}')
    while True:
        command = conn.recv(2048).decode('utf-8')
        if command == 'exit':
            server.close()
            break
        out = subprocess.run(command.split(), capture_output=True)
        if out.returncode != 0:
            conn.send(bytes((f'\n[ERROR]\n{out.stderr.decode("utf-8")}'), 'utf-8'))
        else:
            conn.send(bytes((f'\n[OK]\n{out.stdout.decode("utf-8")}'), 'utf-8'))


def start():
    server.listen()
    while True:
        conn, address = server.accept()

async def main():
        PORT = 8080
        SERVER = socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':

    print("*SERVIDOR INICIALIZADO*")
    asyncio.run(main())

