from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Estabelecer conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="AV2_ViniciusLopes4"  # Nome do banco de dados que criamos anteriormente
)

# Inicializar a aplicação Flask
app = Flask(__name__)

# Cursor que permite executar comandos SQL no banco de dados.
cursor = mydb.cursor()

# Função para executar comandos SQL
def exec_sql_cmd(cmd):
    cursor.execute(cmd)
    mydb.commit()

@app.route('/')
def index():
    return render_template('index.html')


# Rota para listar usuários
@app.route('/listar_usuarios', methods=['GET', 'POST'])
def listar_usuarios():
    cursor.execute("SELECT * FROM USERS")
    usuarios = cursor.fetchall()
    return render_template('listar_usuarios.html', usuarios=usuarios)

# Rota para adicionar usuário

@app.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        country = request.form['country']
        id_console = request.form['id_console']
        exec_sql_cmd(f"INSERT INTO USERS (id, name, country, id_console) VALUES ({id}, '{name}', '{country}', {id_console})")
        return redirect(url_for('listar_usuarios'))
    return render_template('adicionar_usuario.html')

# Rota para deletar usuário
@app.route('/deletar_usuario/<int:id>')
def deletar_usuario(id):
    exec_sql_cmd(f"DELETE FROM USERS WHERE id={id}")
    return redirect(url_for('listar_usuarios'))
@app.route('/listar_videogames', methods=['GET', 'POST'])
def listar_videogames():
    cursor.execute("SELECT * FROM VIDEOGAMES")
    videogames = cursor.fetchall()  # Renomeie a variável para videogames
    return render_template('listar_videogames.html', games=videogames)  # Altere o nome da variável para games
@app.route('/adicionar_videogame', methods=['GET', 'POST'])
def adicionar_videogame():
    if request.method == 'POST':
        id_console = request.form['id_console']
        name = request.form['name']
        id_company = request.form['id_company']
        release_date = request.form['release_date']
        exec_sql_cmd(f"INSERT INTO VIDEOGAMES (id_console, name, id_company, release_date) VALUES ({id_console}, '{name}', {id_company}, '{release_date} 00:00:00') ")
        return redirect(url_for('listar_videogames'))
    return render_template('adicionar_videogame.html')
@app.route('/deletar_videogame/<int:id_console>')
def deletar_videogame(id_console):
    exec_sql_cmd(f"DELETE FROM VIDEOGAMES WHERE id_console={id_console}")
    return redirect(url_for('listar_videogames'))

@app.route('/listar_jogos', methods=['GET', 'POST'])
def listar_jogos():
    cursor.execute("SELECT * FROM GAMES")
    game = cursor.fetchall()
    return render_template('listar_jogos.html', game=game)

@app.route('/adicionar_jogo', methods=['GET', 'POST'])
def adicionar_jogo():
    if request.method == 'POST':
        id_game = request.form['id_game']
        title = request.form['title']
        genre = request.form['genre']
        release_date = request.form['release_date']
        id_console = request.form['id_console']
        exec_sql_cmd(f"INSERT INTO GAMES (id_game, title, genre, release_date, id_console) VALUES ({id_game}, '{title}', '{genre}', '{release_date} 00:00:00', {id_console} )")
        return redirect(url_for('listar_jogos'))
    return render_template('adicionar_jogo.html')
@app.route('/deletar_jogo/<int:id_game>')
def deletar_jogo(id_game):
    exec_sql_cmd(f"DELETE FROM GAMES WHERE id_game={id_game}")
    return redirect(url_for('listar_jogos'))

@app.route('/listar_empresas', methods=['GET', 'POST'])
def listar_empresas():
    cursor.execute("SELECT * FROM COMPANY")
    empresas = cursor.fetchall()
    print(empresas)  # Adicione esta linha para verificar os dados recuperados
    return render_template('listar_empresas.html', empresas=empresas)

@app.route('/adicionar_empresa', methods=['GET', 'POST'])
def adicionar_empresa():
    if request.method == 'POST':
        id_company = request.form['id_company']
        name = request.form['name']
        country = request.form['country']
        exec_sql_cmd(f"INSERT INTO COMPANY (id_company, name, country) VALUES ({id_company}, '{name}', '{country}' )")
        return redirect(url_for('listar_empresas'))
    return render_template('adicionar_empresa.html')
@app.route('/deletar_empresa/<int:id_company>')
def deletar_empresa(id_company):
    exec_sql_cmd(f"DELETE FROM COMPANY WHERE id_company={id_company}")
    return redirect(url_for('listar_empresas'))

if __name__ == '__main__':
    app.run(debug=True)
