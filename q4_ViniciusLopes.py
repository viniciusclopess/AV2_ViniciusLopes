import mysql.connector

# Estabelecer conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='root'
)

# Cursor que permite executar comandos SQL no banco de dados.
cursor = mydb.cursor()

# Essa função executa o comando SQL fornecido usando o cursor especificado.
exec_sql_cmd = lambda cmd, cursor: cursor.execute(cmd)

# Criar Database
criar_database = lambda dbname, cursor: exec_sql_cmd(f"CREATE DATABASE {dbname};", cursor)

# Deletar Database
deletar_database = lambda dbname, cursor: exec_sql_cmd(f"DROP DATABASE {dbname};", cursor)

# Usar database
usar_database = lambda dbname, cursor: exec_sql_cmd(f"USE {dbname};", cursor)

# Criar tabela
criar_tabela = lambda table, attrs, cursor: exec_sql_cmd(f"CREATE TABLE {table} ({attrs});", cursor)

# Deletar tabela
deletar_tabela = lambda table, cursor: exec_sql_cmd(f"DROP TABLE {table};", cursor)

# Inserir dados em uma tabela
inserir_dados = lambda table, attrs, values, cursor: exec_sql_cmd(f"INSERT INTO {table} ({attrs}) VALUES ({values});", cursor)

# Remover dados de uma tabela
deletar_dados = lambda table, condition, cursor: exec_sql_cmd(f"DELETE FROM {table} WHERE {condition};", cursor)

# Fazer uma consulta na tabela selecionada
selecionar_condicao = lambda attrs, table, wherecond, cursor: exec_sql_cmd(f"SELECT {attrs} FROM {table} WHERE {wherecond};", cursor)

# Objetivo da questão 3
#criar_database('AV2_ViniciusLopes4', cursor)
usar_database("AV2_ViniciusLopes4", cursor)
# criar_tabela("USERS", 'id INT, name VARCHAR(255), country VARCHAR(255), id_console INT', cursor)
# criar_tabela("VIDEOGAMES", 'id_console INT, name VARCHAR(255), id_company INT, release_date DATETIME', cursor)
# criar_tabela("GAMES", "id_game INT, title VARCHAR(255), genre VARCHAR(255), release_date DATETIME, id_console INT", cursor)
# criar_tabela("COMPANY", "id_company INT, name VARCHAR(255), country VARCHAR(75)", cursor)
# # Inserir dados na tabela USERS
# inserir_dados("USERS", "id, name, country, id_console", "1, 'Vinicius', 'Brasil', 1", cursor)
# inserir_dados("USERS", "id, name, country, id_console", "2, 'Maria', 'EUA', 2", cursor)
#
# # Inserir dados na tabela VIDEOGAMES
# inserir_dados("VIDEOGAMES", "id_console, name, id_company, release_date", "1, 'PlayStation 5', 1, '2020-11-12'", cursor)
# inserir_dados("VIDEOGAMES", "id_console, name, id_company, release_date", "2, 'Xbox Series X', 2, '2020-11-10'", cursor)
#
# # Inserir dados na tabela GAMES
# inserir_dados("GAMES", "id_game, title, genre, release_date, id_console", "1, 'Spider-Man: Miles Morales', 'Ação/Aventura', '2020-11-12', 1", cursor)
# inserir_dados("GAMES", "id_game, title, genre, release_date, id_console", "2, 'Halo Infinite', 'Tiro em Primeira Pessoa', '2020-11-10', 2", cursor)
#
# # Inserir dados na tabela COMPANY
# inserir_dados("COMPANY", "id_company, name, country", "1, 'Sony', 'Japão'", cursor)
# inserir_dados("COMPANY", "id_company, name, country", "2, 'Microsoft', 'EUA'", cursor)
# mydb.commit()

#Função lambda para gerar o INNER JOIN entre as tabelas
generate_inner_join = lambda: f"""
SELECT GAMES.title, GAMES.genre, GAMES.release_date, COMPANY.name AS company_name
FROM GAMES
INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company;
"""

# Função lambda para gerar o comando SELECT com os atributos envolvidos
generate_select_query = lambda attributes: f"""
SELECT {', '.join(attributes)}
FROM GAMES
INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company;
"""

# Exemplo de uso:
join_query = generate_inner_join()
print("Código SQL para o INNER JOIN:")
print(join_query)

# Atributos que queremos selecionar na consulta
attributes = ["GAMES.title", "GAMES.genre", "COMPANY.name AS company_name"]
select_query = generate_select_query(attributes)
print("\nComando SELECT com os atributos especificados:")
print(select_query)