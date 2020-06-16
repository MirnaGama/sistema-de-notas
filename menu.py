from sistema_notas import ScoreSystem

s = ScoreSystem()
value = 0
print("== SISTEMA DE NOTAS ==")

while(value != "4"):
    print("\n1) Inserir informações de aluno")
    print("2) Calcular média de aluno")
    print("3) Ler arquivo de notas")
    print("4) Sair\n")
    value = input()

    if (value == "1"):
        name = input("Nome do aluno(a): ")
        score1 = input("Nota da 1ª Prova: ")
        score2 = input("Nota da 2ª Prova: ")
        score3 = input("Nota da 3ª Prova: ")
        s.update(name, score1, score2, score3)

        print("\nArquivo atualizado com sucesso. Confira abaixo: ")
        s.read()
    elif (value == "2"):
        student = input("Digite o nome do aluno: ")
        print("Média: {0:.2f}\n".format(s.giveAverage(student)))
    elif (value == "3"):
        print("\nArquivo de Notas:")
        s.read()
    elif (value == "4"):
        print("Saindo . . .")
    else:
        print("Digite uma opção válida")