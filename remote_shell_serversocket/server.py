import socketserver, subprocess, pickle, argparse


PORT = 8080
SERVER = 'localhost'


class MyRequestHandler(socketserver.BaseRequestHandler):

        def handle(self):
           # print(f'Nueva conexión: {self.client_address}')
            while True:
                data = self.request.recv(2048)
                command = pickle.loads(data)
                if command == 'exit':
                    server.close()
                    break
                out = subprocess.run(command.split(), capture_output=True)
                if out.returncode != 0:
                    error = out.stderr.decode('utf-8')
                    self.request.send(pickle.dumps(f'\n[ERROR]\n{error}'))
                else:
                    msg = out.stdout.decode('utf-8')
                    self.request.send(pickle.dumps(f'\n[OK]\n{msg}'))

class Process(socketserver.ForkingMixIn, socketserver.TCPServer): pass


class Threads(socketserver.ThreadingMixIn, socketserver.TCPServer): pass


if __name__ == '__main__':
        
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=str, required=True)
    args = parser.parse_args()

    print("*SERVIDOR INICIALIZADO*")

    if args.mode == 'p':
        server = Process((SERVER, PORT), MyRequestHandler)

        with server:
            server.serve_forever()

    if args.mode == 't':
        server = Threads((SERVER, PORT), MyRequestHandler)

        with server:
            server.serve_forever()
