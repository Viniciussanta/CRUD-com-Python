import mysql.connector


class Vendas:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="crudbd"
        )
        self.cursor = self.conexao.cursor()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conexao.close()

    def __enter__(self):
       return self

    def criar(self, nome_produto, valor):
        comando = f'insert into vendas(nome_produto,valor) values ( %s, %s)'
        self.cursor.execute(comando, (nome_produto, valor))
        self.conexao.commit()

    def ler(self):
        comando = f'select * from vendas'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def atualizar(self, idVendas, novo_valor):
        comando = f'update vendas set valor = %s where idVendas = %s '
        self.cursor.execute(comando, (novo_valor, idVendas,))
        self.conexao.commit()

    def deletar(self, idVendas):
        comando = f'delete from vendas where idVendas = %s'
        self.cursor.execute(comando, (idVendas,))
        self.conexao.commit()


with Vendas() as vendas:
    while True:
        opcao = int(input(f'''
     1-adicionar produto
     2-visualizar produto
     3-atualizar valor
     4-deletar produto
     5-sair'''))

        if opcao == 1:
            produto = input('Digite o nome do produto: ')
            valor_produto = float(input('Digite o valor do produto: '))
            vendas.criar(produto, valor_produto)
        elif opcao == 2:
            print(vendas.ler())
        elif opcao == 3:
            idvendas = int(input('Digite o id do produto:'))
            novovalor = float(input('Digite o novo valor do produto: '))
            vendas.atualizar(idvendas, novovalor)
        elif opcao == 4:
            idvenda = int(input('Digite o ID do produto que vai ser excluido'))
            vendas.deletar(idvenda)
        else:
            break
