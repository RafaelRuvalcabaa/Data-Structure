from collections import deque 


turnos = deque(["Rafa", "Luis", "Mario"])

while turnos: 
    persona = turnos.popleft()
    print(f"Atendiendo a: {persona}...")



from collections import deque

# Cola inicial de turnos
turnos = deque(["Ana", "Luis", "Pedro", "Sofía"])

print("Sistema de turnos iniciado\n")

while turnos:
    actual = turnos[0]  # ver quién sigue (sin sacarlo aún)
    input(f"Atendiendo a {actual}. Presiona Enter cuando termines...")

    turnos.popleft()  # eliminar al que ya fue atendido
    print("Turno finalizado.\n")

print("No hay más personas en la cola.")
