from EditarAlunos import valit_alun_cad
from Erros import ErroGeral, ErroIdade
from Limpa import LimpaTela


def add_alunos(aluno, vet, op):
    a = 0
    continua = 's'
    while a <= 14:
        if aluno[a][0] == "":
            i = a
            a = 15
        else:
            a += 1
            i = a
    a = 0 
    if i <= 14:
        while continua != "n" and i <= 14:
            print()
            while a <= 14:
                if aluno[a][0] == "":
                    i = a
                    a = 15
                else:
                    a += 1
            a = 0
            if aluno[14][0] == "":
                LimpaTela()
                for l in range(0, 3): 
                    if l == 0:
                        caracteristica = "NOME"
                    elif l == 1:
                        caracteristica = "IDADE"
                    elif l == 2:
                        caracteristica = "ENDEREÇO"                 
                    print("Digite o {} do {}° aluno:".format(caracteristica, i+1))
                    aluno[i][l] = input(" -")
                    if l == 1:
                        aluno[i][l] = ErroIdade(aluno[i][l]) 
                    while aluno[i][l] == "":
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("! {} não identificado, por favor digite novamente!".format(caracteristica))
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        aluno[i][l] = input(" -")                 
                valit_alun_cad(i, aluno, vet, op)
                print()
                print("Quer cadastrar outro aluno?")
                print("[s/n]")
                continua = input(" -").lower()
                continua = ErroGeral(continua, "sn", ["s para sim", "n para não"])
            else:
                i += 1
    if i >= 14 and continua == "s":
        print("\nCapacidade máxima de alunos alcançada.")
        print("Pressione 'Enter' para prosseguir.")
        input("\n")
    return aluno
