grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}
### Creas la funcion que acepta tres valores escenciales que es el grafo que vamos a recorrer, el nodo en el que estamos, que en un principio es donde iniciamos a recorrer y por ultimo visitado que si ya lo visitaste lo metes a la pila
def dfs(grafo, nodo, visitados): 
    # Esto en un principio si ya esta visitado ya lo retornas
    if nodo in visitados:
        return
    # En un principio cuando inicia el programa imprime en donde empezaste, eso en su primer vuelta 
    print(nodo)
    # Va a meter a visitados el nodo que anteriormente acaba de imprimir
    visitados.add(nodo)

    # Aqui lo que hace es cin el for avanzar de vecino pero en el nodo que esta examinando, por ejemplo si esta analizando el nodo "A" y los vecinos son "B", en el nodo del grafo avanza al siguente
    for vecino in grafo[nodo]:
        # Aqui lo que hace es hacer lo mismo que arriba pero con el siguente vecino del nodo.
        dfs(grafo, vecino, visitados)



visitados = set()

dfs(grafo,"A", visitados)