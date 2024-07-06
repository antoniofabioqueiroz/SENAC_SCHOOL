from AdicionarAlunos import add_alunos
from ListarAlunos import listar_aluno
from CadastroNota import somanota
from ListarNotas import RelNota
from EditarAlunos import editaon_noute
from ExcluirAluno import excluirAluno
from Erros import ErroGeral
from Limpa import LimpaTela


def menu(op, vet, aluno): #OK.
    LimpaTela()
    print(" ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ‖   ❖   ‖  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")
    print("                        BEM-VINDO AO SENAC\n ")
    print(" ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ‖   ❖   ‖  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("")
    print("Seja bem vindo ao sistema de Cadastro de ALUNOS\n.")
    print(" e um prazer em lhe atende vc da melhor forma")
    print(" ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")
    print("agora para onde você deseja ir?\n")
    print(" 1 - Para fazer seu cadastro digite\n ")
    print(" 2 - Para caso quiser ver relatório do aluno digite\n ")
    print(" 3 - Para caso quiser fazer cadastro de notas\n")
    print(" 4 - Para caso queira ver o relatório de notas\n")
    print(" 5 - Para modificar Nota \n  ")
    print(" 6 - Excluir um aluno\n   ")
    print(" 7 - Para Sair do Sistema \n   ")
    print(" ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ‖   ❖   ‖  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯/n")
    print("OPÇÃO: ", end='')
    op = input()
    op = ErroGeral (op, "1234567", ["1 -Cad aluno.","2 -Relatório de alunos.","3 -Cadastro de notas.","4 -Relatório de notas.","5 -Mudar notas.","6 -Excluir alunos","7 -Sair."])
    match op:
        case "1":
            aluno = add_alunos(aluno, vet, op)
        case "2":
            listar_aluno(aluno,vet, op)
        case "3":
           vet = somanota(aluno, vet, op)
        case "4":
            RelNota(aluno, vet, op)
        case "5":
            vet = editaon_noute(aluno, vet, op)
        case "6":
            data = excluirAluno(aluno, vet, op)
            vet = data[1]
            aluno = data[0]
    return [op, aluno, vet]
