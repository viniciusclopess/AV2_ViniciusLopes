import mysql.connector

#Estabelecer conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='root'
)

#Cursor que permite executar comandos SQL no banco de dados.
cursor = mydb.cursor()

#Essa função executa o comando SQL fornecido usando o cursor especificado.
exec_sql_cmd = lambda cmd, cursor: cursor.execute(cmd)

#Criar Database
criar_database = lambda dbname, cursor: exec_sql_cmd(f"CREATE DATABASE {dbname};", cursor)

#Deletar Database
deletar_database = lambda dbname, cursor: exec_sql_cmd(f"DROP DATABASE {dbname};", cursor)

#Usar database
usar_database = lambda dbname, cursor: exec_sql_cmd(f"USE {dbname};", cursor)

#Criar tabela
criar_tabela = lambda table, attrs, cursor: exec_sql_cmd(f"CREATE TABLE {table} ({attrs});", cursor)

#Deletar tabela
deletar_tabela = lambda table, cursor: exec_sql_cmd(f"DROP TABLE {table};", cursor)

#Inserir dados em uma tabela
inserir_dados = lambda table, attrs, values, cursor: exec_sql_cmd(f"INSERT INTO {table} ({attrs}) VALUES ({values});", cursor)

#Remover dados de uma tabela
deletar_dados = lambda table, condition, cursor: exec_sql_cmd(f"DELETE FROM {table} WHERE {condition};", cursor)

#Fazer uma consulta na tabela selecionada
selecionar_condicao = lambda attrs, table, wherecond, cursor: exec_sql_cmd(f"SELECT {attrs} FROM {table} WHERE {wherecond};", cursor)

#OBJETIVO DA QUESTÃO 4
gerar_inner_join = lambda: exec_sql_cmd("SELECT * FROM GAMES INNER JOIN VIDEOGAMES ON GAMES.id_game = VIDEOGAMES.id_console INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company", cursor)

#Função lambda para gerar o comando SELECT nos atributos envolvidos
gerar_select = lambda atributos: exec_sql_cmd(f"SELECT {', '.join(atributos)} FROM GAMES INNER JOIN VIDEOGAMES ON GAMES.id_game = VIDEOGAMES.id_console INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company", cursor)

#Exemplo de uso:
usar_database('AV2_ViniciusLopes', cursor)
consulta = gerar_select(['GAMES.title', 'VIDEOGAMES.name', 'COMPANY.name'])