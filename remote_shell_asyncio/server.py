from asyncio.runners import run
import subprocess
import asyncio


PORT = 8080
SERVER = 'localhost'


async def manejo_conexion(lector, escritor):
    conn = True
    while conn:
        connection = await manejo_cliente(lector, escritor)


async def manejo_cliente(lector, escritor):
    print(f'Nueva conexión')
    
    command = await lector.read(1024)
    if command == 'exit':
        return None
        
    out = subprocess.run(command.split(), capture_output=True)
    if out.returncode != 0:
        escritor.write(bytes((f'\n[ERROR]\n{out.stderr.decode("utf-8")}'), 'utf-8'))
        await escritor.drain()
    else:
        escritor.write(bytes((f'\n[OK]\n{out.stdout.decode("utf-8")}'), 'utf-8'))
        await escritor.drain()

    return lector


async def main():
    
    server = await asyncio.start_server(manejo_conexion, SERVER, PORT)
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())