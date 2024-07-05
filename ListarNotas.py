from Limpa import LimpaTela


def RelNota(aluno, vet, op):
    LimpaTela()
    for i in range(0, 15):
        if aluno[i][0] != "":
            print()
            print("Aluno: ", aluno[i][0])
            for l in range(0, 4):
                print(l+1, "° Nota: {:.2f}".format(vet[i][l]))
            print("Média:   {:.2f}".format(vet[i][4]))
    print("Para sair pressione 'Enter'.")
    i = input()
 
