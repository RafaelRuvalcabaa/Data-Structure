from collections import deque 

cola = deque()

cola.append("A")
cola.append("B")
cola.append("C")
cola.append("D")


print(f"Cola actual: {cola} ")

cola.popleft()

print(f"Cola actual: {cola} ")

