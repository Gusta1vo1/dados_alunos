import json

def salvar_dados(dados):
    with open('alunos.json', 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_dados():
    try:
        with open('alunos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def adicionar_aluno(dados):
    nome = input("Nome: ")
    data_nasc = input("Data de Nascimento (dd/mm/aaaa): ")
    email = input("E-mail: ")
    fone = input("Telefone: ")
    endereco = input("Endereço: ")
    
    dados[nome] = {
        'data_nasc': data_nasc,
        'email': email,
        'fone': fone,
        'endereco': endereco
    }
    salvar_dados(dados)
    print("Aluno adicionado com sucesso!")

def listar_aluno(dados):
    nome = input("Digite o nome do aluno: ")
    if nome in dados:
        aluno = dados[nome]
        print(f"Nome: {nome}")
        print(f"Data de Nascimento: {aluno['data_nasc']}")
        print(f"E-mail: {aluno['email']}")
        print(f"Telefone: {aluno['fone']}")
        print(f"Endereço: {aluno['endereco']}")
    else:
        print("Aluno não encontrado!")

def listar_todos_alunos(dados):
    if dados:
        for nome, aluno in dados.items():
            print(f"\nNome: {nome}")
            print(f"Data de Nascimento: {aluno['data_nasc']}")
            print(f"E-mail: {aluno['email']}")
            print(f"Telefone: {aluno['fone']}")
            print(f"Endereço: {aluno['endereco']}")
    else:
        print("Nenhum aluno cadastrado!")

def alterar_endereco(dados):
    nome = input("Digite o nome do aluno: ")
    if nome in dados:
        novo_endereco = input("Digite o novo endereço: ")
        dados[nome]['endereco'] = novo_endereco
        salvar_dados(dados)
        print("Endereço atualizado com sucesso!")
    else:
        print("Aluno não encontrado!")

def menu():
    dados = carregar_dados()

    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Listar aluno")
        print("3. Listar todos os alunos")
        print("4. Alterar endereço do aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_aluno(dados)
        elif opcao == '2':
            listar_aluno(dados)
        elif opcao == '3':
            listar_todos_alunos(dados)
        elif opcao == '4':
            alterar_endereco(dados)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
