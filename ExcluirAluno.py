from Erros import ErroAluno, ErroGeral
from Limpa import LimpaTela


def excluirAluno(aluno, vet, op)->list[list[str],list[float]]:
    LimpaTela()
    i = 0
    print ("Indique o aluno a excluir:\n")
    print("Indice  |   Nome")
    print("--------+-------------")
    while  i < 15: 
        if aluno[i][0] != "":
            print ("  {:3}   | {} ".format(i+1, aluno[i][0]))
        i = i+1 
    print ("\nIndice:", end='')
    indice = ErroAluno(input(), aluno)-1
    print("\n Confirme sua ação, realmente deseja\nexcluir {}?".format(aluno[indice][0]),
          "Todas as suas informações serão apagadas do sistema.")
    i = ErroGeral(input("[s/n]").lower(), "sn", ["s para sim", "n para não"])
    if i == "s":
        aluno[indice] = ["", "", ""]
        vet[indice] = [0, 0, 0, 0, 0]
        for x in aluno[indice:15]:
            if x[0] != "" and aluno.index(x) < 14:
                i = aluno.index(x)
                inter = aluno[i]
                aluno[i] = aluno[i+1]
                aluno[i+1] = inter
        print("Aluno excluído com sucesso.")
    else:
        print("Exclusão cancelada.")
    print("para prosseguir pressione 'Enter'")
    i = input("")
    return [aluno, vet]

    
