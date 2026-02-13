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



def dfs(grafo, nodoState, visitado):
    if nodoState in visitado: 
        return

    print(nodoState)

    visitado.add(nodoState)

    for vecino in grafo[nodoState]:
        dfs(grafo, vecino, visitado) 


visitado = set()
dfs(grafo, "A", visitado)