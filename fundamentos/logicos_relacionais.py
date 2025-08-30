# total_porcoes = int(input("Quantidade de porções: "))
# porcoes_por_dia = int(input("Quantas porções por dia: "))

# dias = total_porcoes / porcoes_por_dia

# print(f"Vai durar {dias:.0f} dias")

num1 = 10
num2 = 10

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)


print("##########")
idade = int(input('Qual é a sua idade? '))
sabe_dirigir = True
verificador = idade >= 18

if sabe_dirigir and verificador:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
