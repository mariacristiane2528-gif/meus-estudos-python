nome = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Frequêcia (%): "))
media = (nota1 + nota2) / 2
print()
print("=====BOLETIM DO ALUNO=====")
print("Nome:", nome)
print("Média:", media)
print("Frequêcia:", frequencia)
if frequencia < 75:
    print("Situação: Reprovado por falta")
elif media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")