import random

class miError(Exception):
    pass

def tirarException():
    raise miError("Se saltó la cadena")

quieroTirarException = True
sorteo = random.uniform(0, 100)
print(f"sorteo vale: {sorteo:.2f}")
if sorteo > 50:
    quieroTirarException = False

if quieroTirarException:
    try:
        tirarException()
    except miError as e:
        print(f"Error: {e}")
        print("El programa sigue funcionando")
else:
    print("No hubo errores")


print("El programa terminó")
