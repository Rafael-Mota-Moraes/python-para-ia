for repetir in range(1, 5):
    print(repetir)

senha_correta = "1234"

while True:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Entra no sistema")
        break