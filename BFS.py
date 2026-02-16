grafo = {
    "A": ["B", "C", "F", "P"],
    "B": ["P", "H", "A", "O"],
    "C": ["A"],
    "D": [],
    "T": [],
    "F": [],
    "P": [],
    "H": [],
    "O": []
}

from collections import deque

def bfs(grafo, inicio):
    visitado = []
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()

        if nodo not in visitado:
            print(nodo)
            visitado.append(nodo)

            for vecino in grafo[nodo]:
                cola.append(vecino)


bfs(grafo, "A")