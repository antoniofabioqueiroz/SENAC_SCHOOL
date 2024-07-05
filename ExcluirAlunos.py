def exclusao_aluno():
    aluno = [["" for _ in range(5)] for _ in range(16)]
    vet = [[0 for _ in range(5)] for _ in range(16)]
    
    while True:
        print("Escolha um aluno para excluir:")
        for i in range(1, 16):
            if aluno[i][0] != "":
                print(f"{i} {aluno[i][0]}")
        
        t = input("Digite o índice do aluno a ser excluído (1 a 15): ")
        
        try:
            indice_aluno = int(t)
            
            if 1 <= indice_aluno <= 15:
                for i in range(1, 6):
                    if i <= 3:
                        aluno[indice_aluno][i-1] = ""
                    vet[indice_aluno][i-1] = 0
                j = 0
                for i in range(1, 16):
                    if aluno[i][0] != "":
                        j += 1
                
                for i in range(indice_aluno, j):
                    for i1 in range(5):
                        if i1 <= 2:
                            aluno[i][i1] = aluno[i+1][i1]
                        vet[i][i1] = vet[i+1][i1]
                    
                    if i == j:
                        for i1 in range(5):
                            if i1 <= 2:
                                aluno[j+1][i1] = ""
                            vet[j+1][i1] = 0
                
                print("Aluno excluído com sucesso!")
                break
            else:
                print("Índice inválido. Digite um número entre 1 e 15.")
        
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
