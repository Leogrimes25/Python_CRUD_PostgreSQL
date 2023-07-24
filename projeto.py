import warnings
import psycopg2
import sys
import pandas as pd
import matplotlib.pyplot as plt

conexao = psycopg2.connect(
    host="localhost",
    database="FastControl",
    port=5432,
    user='postgres',
    password='vinicius')
cursor = conexao.cursor()

while True:
    def Menu_Principal():
        print('')
        print('** MENU **')
        print('Escolha uma das opções abaixo:')
        print('1- Operação Administrativa.')
        print('2- Operações com Cliente.')
        print('3- Operações com Produto.')
        print('4- Operações com Transações.')
        print('5- Gerar Gráfico de Barra')
        print('6- Gerar Gráfico Linha')
        escolha = int(input('Escolha:'))
        if escolha == 1:
            return Menu_Administrador()
        if escolha == 2:
            return Menu_Cliente()
        if escolha == 3:
            return Menu_Produto()
        if escolha == 4:
            return Menu_Transacao()
        if escolha == 5:
            return Gerar_Grafico_Barra()
        if escolha == 6:
            return Gerar_Grafico_Linha()


    def Menu_Administrador():
        print('** MENU **')
        print('Escolha uma das opções:')
        print("1- Cadastrar Administrador")
        print('2- Vizualizar dados de Administrador ')
        print('3- Atualizar dados de Administrador')
        print('4- Deletar Administrador')
        print('5- Encerrar Sistema')
        escolha = int(input('Escolha:'))
        if escolha == 1:
            return CadastrarAdmin()
        if escolha == 2:
            return VizualizarTabela()
        if escolha == 3:
            return AtualizarAdmin()
        if escolha == 4:
            return Deletar_Admin()
        if escolha == 5:
            return sys.exit()


    def CadastrarAdmin():
        print('Vamos inserir os dados !')
        dadocpf_admin = str(input('Informe o CPF:'))
        dadosenha_admin = str(input('Informe a senha:'))
        cursor.execute(f''' INSERT INTO Administrador(cpf,senha)
         VALUES('{dadocpf_admin}','{dadosenha_admin}')''')
        print('Dados Inseridos!')


    def VizualizarTabela():
        cursor.execute(''' SELECT * FROM Administrador''')
        vizualizacao = cursor.fetchall()
        for row in vizualizacao:
            print('CPF do Administrador: {}'.format(row[0]))
            print('Senha do Administrador: {}'.format(row[1]))


    def AtualizarAdmin():
        cpf = str(input('Informe o CPF de administrador:'))
        senhaupdate = str(input('Informe a nova senha para Administrador:'))
        cursor.execute(f''' UPDATE Administrador
        SET senha='{senhaupdate}'
        WHERE cpf ='{cpf}' ''')
        print('Senha alterada com sucesso')


    def Deletar_Admin():
        numerodelete = int(input('Quantos administradores gostaria de deletar?'))
        for i in range(numerodelete):
            dadocodigoadmin = str(input('Informe o cpf do administrador respectivo:'))
            cursor.execute(f''' DELETE FROM Administrador
        WHERE cpf = '{dadocodigoadmin}' ''')
            print('Deletado com sucesso!')


    def Menu_Cliente():
        print('** MENU **')
        print('Escolha uma das opções:')
        print('1-Cadastrar Cliente.')
        print('2- Visualizar Dados de Clientes.')
        print('3- Atualizar dados de Cliente.')
        print('4- Deletar dados de Cliente')
        print('5- Encerrar Sistema')
        escolha = int(input('Escolha:'))
        if escolha == 1:
            return Cadastrar_Cliente()
        if escolha == 2:
            return Visualizar_Cliente()
        if escolha == 3:
            return AtualizarCliente()
        if escolha == 4:
            return Deletar_Cliente()
        if escolha == 5:
            return sys.exit()


    def Cadastrar_Cliente():
        print('Vamos inserir os dados de cliente na tabela!')
        numerocadastro = int(input('Quantos Clientes gostaria de cadastrar?'))
        for i in range(numerocadastro):
            dadocpf = str(input('Informe o CPF do Cliente:'))
            dadonome = str(input('Informe o Nome do Cliente:'))
            dadoemail = str(input('Informe o email do Cliente:'))
            dadoddd = int(input('Informe o DDD do Cliente:'))
            dadonumero = str(input('Informe o número do Cliente:'))
            cursor.execute(f''' INSERT INTO Cliente(cpf,nome,email,ddd,numero)
            VALUES('{dadocpf}','{dadonome}','{dadoemail}','{dadoddd}','{dadonumero}')''')
            print('Dados Inseridos Com Sucesso!')


    def Visualizar_Cliente():
        cursor.execute(''' SELECT * FROM Cliente''')
        vizualizacao = cursor.fetchall()
        for row in vizualizacao:
            print('Codigo Cliente: {}'.format(row[0]))
            print('CPF: {}'.format(row[1]))
            print('Nome: {}'.format(row[2]))
            print('Email: {}'.format(row[3]))
            print('DDD: {}'.format(row[4]))
            print('Número: {}'.format(row[5]))
            print('CPFAdministrador : {}'.format(row[6]))
            print('')


    def AtualizarCliente():
        numeroatualizacao = int(input('Quantos Clientes Gostaria de Atualizar?'))
        for i in range(numeroatualizacao):
            codigo_cliente = str(input('Informe o código do cliente que sofrerá alteração de dados:'))
            print('Escolha uma das opções para atualizar.')
            print('1-Atualizar Número.')
            print('2- Atualizar DDD.')
            print('3- Atualizar Email.')
            escolha_uptade = int(input('Escolha:'))
            if escolha_uptade == 1:
                numerouptade = str(input('Informe o novo número:'))
                cursor.execute(f''' UPDATE Cliente
       SET numero= '{numerouptade}'
       WHERE codigo_cliente='{codigo_cliente}' ''')
            if escolha_uptade == 2:
                    dddupdate = str(input('Informe o novo DDD:'))
                    cursor.execute(f''' UPDATE Cliente
        SET ddd='{dddupdate}'
        WHERE codigo_cliente='{codigo_cliente}' ''')
            if escolha_uptade == 3:
                    emailupdate = str(input('Informe o novo email:'))
                    cursor.execute(f''' UPDATE Cliente
            SET email='{emailupdate}'
            WHERE codigo_cliente='{codigo_cliente}' ''')
                    print('Dados Alterados')


    def Deletar_Cliente():
        numerodelete = int(input('Quantos Clientes Gostaria de Deletar?'))
        for i in range(numerodelete):
            dadocodigocliente = str(input('Informe o código do cliente respectivo:'))
            cursor.execute(f''' DELETE FROM Cliente
        WHERE codigo_cliente = '{dadocodigocliente}' ''')
            print('Deletado com sucesso!')


    def Menu_Produto():
        print('** MENU **')
        print('Escolha uma das opções abaixo:')
        print('1 - Cadastrar Produto.')
        print('2 - Visualizar tabela de produtos.')
        print('3- Deletar Produto.')
        print('4- Atualizar dados de Produto')
        print('5 Encerrar Sistema')
        escolha = int(input('Escolha:'))
        if escolha == 1:
            return Cadastrar_Produto()
        if escolha == 2:
            return Visualizar_Produto()
        if escolha == 3:
            return Deletar_Produto()
        if escolha == 4:
            return Atualizar_Produto()
        if escolha == 5:
            return sys.exit()


    def Cadastrar_Produto():
        print('Vamos inserir os dados de produto!')
        numerocadastro = int(input('Quantos produtos gostaria de cadastrar?'))
        for i in range(numerocadastro):
            categoria_produto = str(input('Informe a categoria do produto:'))
            modelo_produto = str(input('Informe o modelo do produto:'))
            preco_produto = float(input('Informe o preço do produto:'))
            cursor.execute(f''' INSERT INTO Produto(categoria,modelo,preco)
                    VALUES('{categoria_produto}','{modelo_produto}','{preco_produto}')''')
            print('Dados Inseridos Com Sucesso')


    def Visualizar_Produto():
        cursor.execute(''' SELECT * FROM Produto''')
        vizualizacao = cursor.fetchall()
        for row in vizualizacao:
            print('')
            print('Codigo Produto: {}'.format(row[0]))
            print('Categoria: {}'.format(row[1]))
            print('Modelo: {}'.format(row[2]))
            print('Preço: {}'.format(row[3]))
            print('CPFAdministrador :{}'.format(row[4]))
            print('')


    def Atualizar_Produto():
        numeroatualizacao = int(input('Quantos produtos gostaria de atualizar?'))
        for i in range(numeroatualizacao):
            codigo_produto = str(input('Informe o código do produto que sofrerá alteração de dados:'))
            print('Escolha uma das opções:')
            print('1-Alterar Preço')
            print('2-Alterar Modelo')
            print('3-Alterar Categoria')
            escolhaupdate = int(input('Escolha:'))
            if escolhaupdate == 1:
                precoupdate = float(input('Informe o novo preço:'))
                cursor.execute(f''' UPDATE Produto
         SET preco='{precoupdate}'
         WHERE codigo_produto='{codigo_produto}' ''')
            if escolhaupdate == 2:
                modeloupdate = str(input('Informe o novo modelo:'))
                cursor.execute(f''' UPDATE Produto
         SET modelo='{modeloupdate}'
         WHERE codigo_produto='{codigo_produto}' ''')
            if escolhaupdate == 3:
                categoriaupdate = str(input('Informe a nova categoria:'))
                cursor.execute(f''' UPDATE Produto
         SET categoria='{categoriaupdate}'
         WHERE codigo_produto='{codigo_produto}' ''')
            print('Dados Alterados')


    def Deletar_Produto():
        numerodelete = int(input('Quantos produtos gostaria de deletar?'))
        for i in range(numerodelete):
            codigo_produto = str(input('Informe o código do produto respectivo:'))
            cursor.execute(f'''DELETE FROM Produto
        WHERE codigo_produto = '{codigo_produto}' ''')
            print('Deletado com sucesso!')


    def Menu_Transacao():
        print('')
        print('** MENU **')
        print('Escolha uma das opções abaixo:')
        print('1- Cadastrar Transação.')
        print('2- Visualizar dados de transações.')
        print('3- Atualizar dados de Transação.')
        print('4- Deletar alguma transação')
        print('5 Encerrar Sistema')
        escolha = int(input('Escolha:'))
        if escolha == 1:
            return Cadastrar_Transacao()
        if escolha == 2:
            return Vizualizar_Transacao()
        if escolha == 3:
            return Atualizar_Transacao()
        if escolha == 4:
            return Deletar_Transacao()
        if escolha == 5:
            return sys.exit()


    def Cadastrar_Transacao():
        print('Vamos inserir os dados de transação!')
        numerotransacao = int(input('Quantas transações gostaria de cadastrar?'))
        for i in range(numerotransacao):
            dadoquantidade = int(input('Informe a quantidade:'))
            dadodata = str(input('Informe a data da transação:'))
            dadototal = float(input('Informe o total:'))
            dadocpf_admin = str(input('Informe o CPF de Administrador:'))
            dadoproduto = str(input('Informe o código do produto que foi vendido:'))
            dadocliente = str(input('Informe o código do cliente que comprou o produto:'))
            cursor.execute(f''' INSERT INTO Transacao(quantidade,data_transacao,total,cpf_admin,codigo_produto,
            codigo_cliente) VALUES('{dadoquantidade}','{dadodata}','{dadototal}','{dadocpf_admin}','{dadoproduto}',
        '{dadocliente}')''')
        print('Dados inseridos com sucesso !')


    def Vizualizar_Transacao():
        cursor.execute(''' SELECT * FROM Transacao ''')
        vizualicao = cursor.fetchall()
        for row in vizualicao:
            print('Codigo da Transação: {} '.format(row[0]))
            print('Quantidade: {}'.format(row[1]))
            print('Data da transação: {}'.format(row[2]))
            print('Total: {}'.format(row[3]))
            print('CPF Administrador : {}'.format(row[4]))
            print('Codigo Produto : {}'.format(row[5]))
            print('Código Cliente : {}'.format(row[6]))
            print('')


    def Atualizar_Transacao():
        numeroatualizacao = int(input('Quantas atualizações gostaria de realizar?'))
        for i in range(numeroatualizacao):
            codigo_transacao = str(input('Informe o código da transação respcetiva:'))
            print('Escolha uma das opções para atualizar')
            print('1-Atualizar quantidade.')
            print('2-Atualizar Total.')
            escolha_update = int(input('Escolha:'))
            if escolha_update == 1:
                quantidadepdate = int(input('Informe a nova quantidade:'))
                cursor.execute(f''' UPDATE Transacao
            SET quantidade='{quantidadepdate}'
            WHERE codigo_transacao='{codigo_transacao}' ''')
            if escolha_update == 2:
                totalupdate = float(input('Informe o novo total:'))
                cursor.execute(f''' UPDATE Transacao
            SET total='{totalupdate}'
            WHERE codigo_transacao='{codigo_transacao}' ''')
            print('Dados Atualizados!')


    def Deletar_Transacao():
        numerodelete = int(input('Quantas transações gostaria de deletar?'))
        for i in range(numerodelete):
            codigo_transacao = str(input('Informe o código da respectiva transação:'))
            cursor.execute(f'''DELETE FROM Transacao
        WHERE codigo_transacao = '{codigo_transacao}' ''')
            print('Deletado com sucesso!')


    def Gerar_Grafico_Barra():
        df = pd.read_sql(f'''SELECT data_transacao, Total FROM Transacao''', conexao)
        df.plot(kind="bar", x='data_transacao', y='total')
        plt.show()


    def Gerar_Grafico_Linha():
        df = pd.read_sql(f'''SELECT data_transacao, Total FROM Transacao''', conexao)
        df.plot(kind='line', x='data_transacao', y='total')
        plt.show()


    warnings.filterwarnings('ignore')
    Menu_Principal()
    conexao.commit()