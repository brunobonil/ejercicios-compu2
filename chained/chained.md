# Función 'primera'

async def primera(n: int) -> str:
    i = random.randint(0, 10)
    print(f"primera({n}) esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-A"
    print(f"Retornando primera({n}) == {result}.")
    return result

# Es un corrutina que recibe un parámetro 'n' (int) y devuelve un string

# Función segunda
