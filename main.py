n = 1000
pares = [i for i in range(1, n + 1) if i % 2 == 0]

print("Números pares hasta", n, ":")
print(pares)
print("Cantidad de pares:", len(pares))

for i in range(n):
    if i % 2 == 0:
        print("%i es par"%i)
    else:
        print("%i es impar"%i)
    print("done")
    