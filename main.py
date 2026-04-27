# =========================================
# SISTEMA DE GERENCIAMENTO DE ALUNOS
# Projeto para prática de lógica de programação com Python
# =========================================

lista_alunos = []


def adicionar_aluno():
    print("\n--- CADASTRAR ALUNO ---")
    
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))

    while True:
        nota = float(input("Nota do aluno (0 a 10): "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")

    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Nota": nota
    }

    lista_alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
    print("-" * 30)


def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")

    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado.")
        print("-" * 30)
        return

    for aluno in lista_alunos:
        print(f"Nome : {aluno['Nome']}")
        print(f"Idade: {aluno['Idade']}")
        print(f"Nota : {aluno['Nota']}")
        print("-" * 30)


def buscar_aluno():
    print("\n--- BUSCAR ALUNO ---")

    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado para busca.")
        print("-" * 30)
        return

    nome_procurado = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in lista_alunos:
        if aluno["Nome"].lower() == nome_procurado.lower():
            print("\nAluno encontrado!")
            print(f"Nome : {aluno['Nome']}")
            print(f"Idade: {aluno['Idade']}")
            print(f"Nota : {aluno['Nota']}")
            print("-" * 30)
            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")
        print("-" * 30)


def remover_aluno():
    print("\n--- REMOVER ALUNO ---")

    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado para remover.")
        print("-" * 30)
        return

    nome = input("Digite o nome do aluno que deseja remover: ")
    removido = False

    for aluno in lista_alunos:
        if aluno["Nome"].lower() == nome.lower():
            lista_alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            print("-" * 30)
            removido = True
            break

    if not removido:
        print("Aluno não encontrado.")
        print("-" * 30)


def media_geral():
    print("\n--- MÉDIA GERAL ---")

    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado.")
        print("-" * 30)
        return

    soma = 0

    for aluno in lista_alunos:
        soma += aluno["Nota"]

    media = soma / len(lista_alunos)

    print(f"Média geral das notas: {media:.2f}")
    print("-" * 30)


while True:
    print("\n========== MENU ==========")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Remover aluno")
    print("5. Mostrar média geral")
    print("6. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números válidos.")
        continue

    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            buscar_aluno()
        case 4:
            remover_aluno()
        case 5:
            media_geral()
        case 6:
            print("Encerrando sistema...")
            break
        case _:
            print("Opção inválida. Tente novamente.")