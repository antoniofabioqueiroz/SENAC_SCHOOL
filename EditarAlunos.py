from Erros import ErroNota, ErroAluno
from Notas import notas
from Limpa import LimpaTela


def editaon_noute (aluno, vet, op): 
    entidade=()
    i=int(0)
    modificador=str()
    teste=bool ()
    LimpaTela()
    print ("Indique o indice do aluno que deseja modificar a nota: ")
    print()
    print("Indice  |   Nome")
    print("--------+-------------")
    while  i < 15: 
        if aluno[i][0] != "":
            print ("  {:3}   | {} ".format(i+1, aluno[i][0]))
        i = i+1 
    print ()
    print (" indice:", end='')
    entidade = ErroAluno(input(), aluno)-1
    print("Notas de ",aluno[entidade][0])
    print ("")
    i= 0
    while i <=  3:
        print ("Nota ", i+1, " cadastrada: ", vet[entidade][i])
        print("Nota ",i+1,": ", end='')
        modificador=input()
        vet[entidade][i] = ErroNota(modificador, i+1)
        i += 1
    vet[entidade][4] = notas(vet[entidade][ 0], vet[entidade][ 2], vet[entidade][ 3], vet[entidade][ 1])
    print("Notas alteradas com sucesso! :D")
    modificador=input()
    return vet


def valit_alun_cad(entrada,aluno, vet, op): #OK.
    x = int(0)
    y = int(0)
    ver = int(0)
    erro = False
    i = 1
    while x < 15:
        if x != entrada:
            y = 0
            while y < 3:
                if aluno [x][y] == aluno [entrada] [y]:
                    ver = ver +1
                y += 1
        x += 1
        if ver == 3 :
            erro = True
        else:
            ver = 0
    if erro == True:
        print (" aluno já existente, cadastro não realizado ")
        aluno [entrada][1] = ""
        aluno [entrada][2] = ""
        aluno [entrada][0] = ""
    else:
        print ("aluno cadastro com sucesso")
