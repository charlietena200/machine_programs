#Given x,y,z and n integers. Print a list of all posible combinations that doesnt sum=n
x=1
y=2
z=2
n=3

valoresi = [i for i in range(x + 1)]
valoresj = [j for j in range(y + 1)]
valoresk = [k for k in range(z + 1)]

lista2 = []

for i1 in range(x + 1):
    for i2 in range(y + 1):
        for i3 in range(z + 1):
            lista2.append([i1, i2, i3])

print(lista2)

lista = [[i, j, k] for i in valoresi for j in valoresj for k in valoresk if (i + j + k) != n]

# lista.insert(0,[0,0,0])

print(lista)