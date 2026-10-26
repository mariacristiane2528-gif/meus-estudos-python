nome = input("Qual o nome do aluno? ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2 
if media >= 7:
    print("Nome", nome)
    print("Média", media)
    print("Situação: Aprovado")
elif media >= 5:
    print("Nome", nome)
    print("Média", media)
    print("Situação: Recuperação")
else:
    print("Nome", nome)
    print("Média", media)
    print("Situação: Reprovado")