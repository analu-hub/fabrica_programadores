numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

pares = [num for num in numeros if num % 2 == 0]

print("Números pares:", pares)