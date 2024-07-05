def ErroIdade(idade: str)->str: #OK.
    z = int()
    while z != len(idade):
        numero = "0123456789"
        for x in range(0, len(idade)):
            if idade[x] in numero:
                z += 1
        if z < len(idade):
            print("\nIdade inválida, informe outra.")
            idade = input("Idade: ")
            z = 0
    return idade


def ErroNota(nota: str, n: int)->float:
    numero, erro = "0123456789.", True
    while erro == True:
        if  nota.find(".") == nota.rfind("."):
            if not (float(nota) < 0 or float(nota) > 10):
                erro = False
            else: 
                erro = True
            for x in range(0, len(nota)):
                if not (nota[x] in numero):
                    erro = True
        else:
            erro = True
        if erro == True:
            print("\nNota inserida inválida, informe outra.")
            nota = input("Nota {}: ".format(n))
    return float("{:.2f}".format(float(nota)))


def ErroGeral(analise: str, opcoes: list, dominio: list)->str: #OK.
    while not (analise in opcoes) or analise == "":
        print("\nOpção inválida, insira outra.")
        for x in range(0, len(dominio)):
            print(dominio[x])
        analise = input(" -")
    return str(analise)
	

def ErroAluno(indice: str, aluno:list)->int:
    while 1 != 2:
        ok = 0
        for x in indice:
            if x in "01234567890":
                ok += 1
        if ok == len(indice):
            if int(indice) <= len(aluno) and int(indice) > 0 and aluno[int(indice)-1][0] != "":
                return int(indice)
            else:
                ok = 0
                print("\nValor inserido inválido, insira outro.")
                print("Indice  |   Nome")
                print("--------+-------------")
                while  ok < 15: 
                    if aluno[ok][0] != "":
                        print ("  {:3}   | {} ".format(ok+1, aluno[ok][0]))
                    ok += 1 
                indice = input("Indice: ")
