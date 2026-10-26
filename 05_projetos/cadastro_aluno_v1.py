contador = 0
continuar = "S"
while continuar == "S":
    nome = input("Qual o nome do aluno? ")
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    nota3 = float(input("Qual a terceira nota? "))
    nota4 = float(input("Qual a quarta nota? "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(" Aluno:", nome)
    print("media:", media)
    if media >= 7:
        print("Aprovado!")
    elif media >=5:
        print("Recuperação.")
    else:
        print("Reprovadp.") 
    contador = contador + 1
    continuar = input("Deseja cadrastar outro aluno? (S/N): ").upper()
print("Foram cadastrados", contador, "alunos.")