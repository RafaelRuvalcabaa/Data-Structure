grafo = {
    "A": ["B", "C", "D"],
    "B": ["E", "F", "A"],
    "C": ["G", "H"],
    "D": ["I", "J"],
    "E": ["K", "L"],
    "F": ["L", "M"],
    "G": ["N"],
    "H": ["N", "O"],
    "I": ["P"],
    "J": ["P", "Q"],
    "K": ["R"],
    "L": ["R", "S"],
    "M": ["S"],
    "N": ["T"],
    "O": ["T", "U"],
    "P": ["V"],
    "Q": ["V", "W"],
    "R": ["X"],
    "S": ["X", "Y"],
    "T": ["Z"],
    "U": ["Z"],
    "V": [],
    "W": [],
    "X": [],
    "Y": [],
    "Z": [],
}


def dfs(grafo, nodo, visitado):
    if nodo in visitado: 
        return 
    print(nodo)
    visitado.append(nodo)

    for vecino in grafo[nodo]:
        dfs(grafo, vecino, visitado)


visitado = []
dfs(grafo, "A", visitado)
