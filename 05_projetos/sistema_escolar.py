print("=================================================================")
print("                     SISTEMA ESCOLAR")
print("=================================================================")

escola = input("Escola: ")
professor =  input("Professor: ")
turma = input("Turma: ")
turno = input("Turno: ")
disciplina = input("Disciplina: ")
ano = input("Ano letivo: ")
contador  = 0 
aprovados = 0
recuperacao = 0
reprovados = 0
reprovados_falta = 0
continuar = "S"
while continuar == "S":
    nome = input("Aluno: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    nota4 = float(input("Quarta nota: "))
    frequencia = float(input("Frequência do aluno: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("=============================================================")
    print("BOLETIM DO ALUNO")
    print("=============================================================")
    print("Escola:", escola)
    print("Professor:", professor)
    print("Turma:", turma)
    print("Turno:", turno)
    print("Disciplina:", disciplina)
    print("Ano letivo:", ano)
    print("Aluno:", nome)
    print("Média:", media)
    print("Frequência:", frequencia, "%")
    if frequencia < 75:
        print("Reprovado por falta.")
        reprovados_falta = reprovados_falta + 1
    elif media >= 7:
        print("Aprovado.")
        aprovados = aprovados + 1
    elif media >= 5:
        print("Recuperação.")
        recuperacao = recuperacao + 1
    else:
        print("Reprovado.")
        reprovados = reprovados + 1
    contador = contador + 1
    continuar = input("Você deseja cadastrar outro aluno?  (S/N)").upper()
print("Quantidade de alunos cadastrado:", contador)
print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovado:", reprovados)
print("Reprovado por falta", reprovados_falta)
