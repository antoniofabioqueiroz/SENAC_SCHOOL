from Erros import ErroGeral, ErroNota
from Limpa import LimpaTela
from Notas import notas


def somanota(aluno, vet, op):
    indice, continua = 0, "s"
    while indice < 15 and continua == "s":
        if vet[indice][0] is None and aluno[indice][0] != "":
            LimpaTela()
            print("Cadastro de notas de {}".format(aluno[indice][0]))
            for x in range(0, 4):
                vet[indice][x] = ErroNota(input("{}° Nota: ".format(x+1)), x+1)
            vet[indice][4] = notas(vet[indice][1], vet[indice][2], vet[indice][3], vet[indice][0])
            print("Notas cadastradas com sucesso!\nDeseja cadastrar a nota de outro aluno(a)?")
            continua = ErroGeral(input("[s/n]"), "sn", ["s para sim", "n para não"])
            if continua == "s":
                indice += 1
            else:
                indice = 15
        else:
            if continua == "s" and indice < 15:
                indice += 1
            else:
                continua = "n"
                print("Cadastro finalizado.")
    l = input("Para sair pressione 'Enter'")
    return vet
