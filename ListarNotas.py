from Limpa import LimpaTela


def RelNota(aluno, vet, op):
    LimpaTela()
    for i in range(0, 15):
        if aluno[i][0] != "":
            print()
            print("Aluno: ", aluno[i][0])
            for l in range(0, 4):
                if vet[i][l] is not None:
                    print(l+1, "° Nota: {:.2f}".format(vet[i][l]))
                else:
                    print(l+1, "º Nota: {}".format("Nota não cadastrada"))
            if vet[i][4] is not None:
                print("Média:   {:.2f}".format(vet[i][4]))
            else:
                print("Média:   {}".format("Notas não cadastradas."))
    print("Para sair pressione 'Enter'.")
    i = input()
 
