pesos = []
dias = [] 


while True:
    peso = float(input("Informe o peso registrado (ou -1 para encerrar): "))
    if peso == -1:
        break
    dia = int(input("Informe o dia correspondente: "))
    pesos.append(peso)
    dias.append(dia)

print("\nRegistros de Peso:")
for i in range(len(pesos)):
    print(f"Dia {dias[i]}: Peso = {pesos[i]} kg", end=" ")
    if i > 0:
        taxa = (pesos[i] - pesos[i-1]) / (dias[i] - dias[i-1])
        if taxa > 0:
            print(f"Taxa de Crescimento = {taxa:.2f} kg/dia")
        elif taxa < 0:
            print(f"Taxa de Declínio = {abs(taxa):.2f} kg/dia")
        else:
            print("Taxa de Crescimento = 0 kg/dia")
