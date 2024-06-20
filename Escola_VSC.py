import mysql.connector   # Importando o MySQL para o VSC

class Aluno:    # Definição da classe Aluno
    def __init__(self, nome, idade, turma): # Método construtor da classe Aluno com três parâmetros: nome, idade e turma
        self.nome = nome    # Atributo self.nome recebe o valor do parâmetro nome
        self.idade = idade  # Atributo self.idade recebe o valor do parâmetro idade
        self.turma = turma  # Atributo self.turma recebe o valor do parâmetro turma

class EscolaDB:  # Definição da classe EscolaDB
    def __init__(self):  # Método construtor da classe EscolaDB
        self.conn = mysql.connector.connect(  # Estabelece a conexão com o banco de dados MySQL
            host="localhost",  # Endereço do servidor MySQL (neste caso, local)
            user="root",  # Nome de usuário para acessar o banco de dados
            password="he182555@",  # Senha do usuário para acessar o banco de dados
            database="escola"  # Nome do banco de dados que será utilizado
        )
        self.cursor = self.conn.cursor()  # Cria um cursor para executar comandos SQL

    def adicionar_aluno(self, aluno):
        sql = "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)"  # Define o comando SQL para inserir um aluno na tabela 'alunos'
        val = (aluno.nome, aluno.idade, aluno.turma)  # Obtém os valores do aluno a serem inseridos
        self.cursor.execute(sql, val)  # Executa o comando SQL com os valores fornecidos
        self.conn.commit()  # Confirma a transação, efetivando a inserção no banco de dados

    def mostrar_alunos(self):
        self.cursor.execute("SELECT * FROM alunos")  # Executa uma consulta SQL para selecionar todos os alunos da tabela 'alunos'
        alunos = self.cursor.fetchall()  # Obtém todos os resultados da consulta SQL
        for aluno in alunos:  # Itera sobre cada registro retornado pela consulta
            print(aluno)  # Imprime cada aluno encontrado na consulta

    def fechar_conexao(self):
        self.cursor.close()  # Fecha o cursor, liberando os recursos associados
        self.conn.close()  # Fecha a conexão com o banco de dados, encerrando a sessão de comunicação

def menu():
    print("1. Adicionar Aluno")  # Imprime a opção para adicionar um aluno
    print("2. Mostrar Alunos")  # Imprime a opção para mostrar todos os alunos cadastrados
    print("3. Sair")  # Imprime a opção para sair do programa

if __name__ == "__main__":
    escola_db = EscolaDB()  # Instancia um objeto EscolaDB para interagir com o banco de dados

    while True:  # Loop infinito para exibir o menu até que o usuário escolha sair
        menu()  # Exibe as opções do menu para o usuário
        escolha = input("Escolha uma opção (1 a 3): ")  # Solicita que o usuário escolha uma opção

        if escolha == "1":  # Se a escolha do usuário for "1"
            nome = input("Nome do aluno: ")  # Solicita o nome do aluno ao usuário
            idade = int(input("Idade do aluno: "))  # Solicita a idade do aluno ao usuário (convertido para inteiro)
            turma = input("Turma do aluno: ")  # Solicita a turma do aluno ao usuário
            aluno = Aluno(nome, idade, turma)  # Cria um objeto Aluno com os dados fornecidos
            escola_db.adicionar_aluno(aluno)  # Chama o método para adicionar o aluno ao banco de dados
            print("Aluno adicionado com sucesso.")  # Informa ao usuário que o aluno foi adicionado com sucesso

        elif escolha == "2":  # Se a escolha do usuário for "2"
            print("Lista de alunos:")  # Exibe a mensagem "Lista de alunos:"
            escola_db.mostrar_alunos()  # Chama o método para mostrar todos os alunos cadastrados no banco de dados

        elif escolha == "3":  # Se a escolha do usuário for "3"
            print("Saindo...")  # Informa ao usuário que está saindo do programa
            escola_db.fechar_conexao()  # Chama o método para fechar a conexão com o banco de dados
            break  # Sai do loop infinito, encerrando o programa

        else:  # Se a escolha do usuário não for válida (não é "1", "2" ou "3")
            print("Opção inválida. Por favor, escolha uma opção válida.")  # Informa ao usuário que a opção escolhida não é válida
