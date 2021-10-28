## Función "primera"

Es una corrutina que recibe un parámetro 'n' (int) y devuelve un string

```
async def primera(n: int) -> str:
    i = random.randint(0, 10)
    print(f"primera({n}) esperando {i}s.")
    await asyncio.sleep(i)     #Duerme la corrutina tantos segundos como indique 'i' 
    result = f"result{n}-A"
    print(f"Retornando primera({n}) == {result}.")
    return result
```

## Función "segunda"

Es una corrutina que recibe 2 parámetros 'n' (int) y arg (str) y devuelve un string
```
async def segunda(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"segunda{n, arg} esperando {i}s.")
    await asyncio.sleep(i)      #Duerme la corrutina tantos segundos como indique 'i' 
    result = f"result{n}-B => {arg}"
    print(f"Retornando segunda{n, arg} => {result}.")
    return result
```

## Función "chain"

Es una corrutina que recibe un parámetro 'n' y al final imprime el resultado de la función
primera() y segunda() concatenados
```
async def chain(n: int) -> None:
    start = time.perf_counter()
    print("Lanzando primera")
    prim = await primera(n)         #Llama a la función primera()
    print("Lanzando Segunda")
    segu = await segunda(n, prim)       #Llama a la función segunda()
    end = time.perf_counter() - start
    print(f"-->Encadenado result{n} => {segu} (tomó {end:0.2f} s).")
```

## Función "main"

