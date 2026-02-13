def imprimir(n):
    if n == 0:
        return 
    print(n)
    imprimir(n-1)


imprimir(4)
