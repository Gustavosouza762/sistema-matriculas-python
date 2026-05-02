#cria uma lista vazia
alunos = []
#cria uma lista com três strings dos cursos
cursos = ["Python", "Java", "Web"]

#cria uma função
def cadastrar_aluno():
    #cria uma string para o usuário digitar o nome
    nome = input("Nome do aluno: ")
    #cria uma string para a idade 
    idade = input("Idade: ")

    #verifica se o nome não é falso
    if not nome:
        #informa o erro ao usuário
        print("Nome inválido")
        #função encerrada
        return
    
    #verifica se todos os carcteres são número
    if not idade.isdigit():
        #informa o erro ao usuário
        print("Idade inválida")
        #função encerrada
        return
    
    #adiciona um novo item a lista como:nome, idade e curso
    alunos.append({
        "nome": nome,
        "idade": int(idade),
        "curso": None
    })

    #mensagem que o aluno foi cadastrado
    print("Aluno cadastrado")

#cria uma função 
def matricular_aluno():
    #cria uma string para matricular o aluno
    nome = input("Nome do aluno: ")

    #percorre todos os alunos da lista
    for aluno in alunos:
        #cria uma condição verificando o nome do aluno na lista com o digitado
        if aluno["nome"] == nome:
            #mostra os cursos disponíveis 
            print("Cursos disponíveis:")
            #enúmera a lista em números pares
            for i, curso in enumerate(cursos):
                #mostra os cursos enumerados
                print(i, "-", curso)

            #o usuário digita um número do curso
            escolha = input("Escolha o curso: ")

            #valida a escolha do usuário
            if not escolha.isdigit():
                #mensagem caso a opção seja inválida
                print("Opção inválida")
                #função encerrada
                return
            
            #converte a escolha em inteiro
            escolha = int(escolha)

            #válida a quantidade de cursos
            if escolha >= len(cursos):
                #mensagem caso o curso seja inválido
                print("Curso inválido")
                #encerra a função
                return

            #atribui o curso
            aluno["curso"] = cursos[escolha]
            #mensagem validando o aluno
            print("Aluno matriculado")
            #função encerrada
            return
        
    #mensagem que o aluno não foi encontrado
    print("Aluno não encontrado")


#cria uma função para listar os alunos
def listar_aluno():
    
    #verifica se não existe nenhum aluno
    if not alunos:
        #mensagem que nenhum aluno cadastrado
        print("Nenhum aluno cadastrado")
        #função encerrada
        return

    #percorre a lista
    for aluno in alunos:
        #perador ternário
        curso = aluno["curso"] if aluno["curso"] else "Sem curso"
        #mensagem do aluno com curso
        print(aluno["nome"], "-", curso)

#define a função main como loop inifinito
def main():
    while True:
        #mensagem para o aluno cadastrar
        print("\n1 - Cadastrar")
        #mensagem para matricular
        print("2 - Matricular")
        #mensagem para listar
        print("3 - Listar")
        #mensagem para listar
        print("4 - Sair")

        #armazena a resposta na variável
        op = input("Escolha: ")

        #se o usuário digita 1, chama cadastrar o aluno        
        if op == "1":
            cadastrar_aluno()
        #se o usuário digita 2, chama matricular o aluno            
        elif op == "2":
            matricular_aluno()
        #se o usuário digita 3, chama listar o aluno      
        elif op == "3":
            listar_aluno()
        #quebra o loop     
        elif op == "4":
            break

        #mensagem caso o usuário não digite nenhuma opção
        else:
            print("Opção inválida")

#executa a função main
main()
