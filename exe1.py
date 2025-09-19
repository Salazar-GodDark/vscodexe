contagem_pares = 0
contagem_impares = 0

for _ in range(10):
    numero = int(input("Digite um número:  "))
    if numero % 2 == 0:
        contagem_pares += 1
    else:
       contagem_impares += 1

print(f"Total pares: {contagem_pares}")
print(f"Total impares: {contagem_impares}")