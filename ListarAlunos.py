from Limpa import LimpaTela


def listar_aluno(aluno, vet, op):
    i = 0
    l = 0
    LimpaTela()
    for i in range(0, 15):
        if aluno[i][0] != "":
            print("========================")
            print("{:<10}".format("Nome: "), aluno[i][0])
            print("{:<10}".format("Endereço: "), aluno[i][2])
            print("{:<10}".format("Idade: "), aluno[i][1])
            print("========================")
    print("Para prosseguir pressione 'Enter'.")
    l=input()
