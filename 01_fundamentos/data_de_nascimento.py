from datetime import datetime
data = input("Data de nascimento dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)
hoje = datetime.now()
idade = hoje.year - ano
if (hoje.month, hoje.day) < (mes, dia):
    idade -= 1
if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade.")
else:
    print(f"Você tem {idade} anos e émenor de iadae. ")