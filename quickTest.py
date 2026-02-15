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




def dfs(grafo, initialNodo, visitado):
    if initialNodo in visitado:
        return 
    
    print(initialNodo)

    visitado.add(initialNodo)

    for  vecino in grafo[initialNodo]:
        dfs(grafo, vecino, visitado)


visitado = set()  
dfs(grafo, "A", visitado)