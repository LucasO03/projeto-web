from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return '''
        <h1>Sobre o Sistema</h1>
        <p>Este sistema foi desenvolvido na disciplina Programação para Internet</p>
        <a href="/">Voltar ao início</a>
        '''

@app.route('/contato')
def contato():
    return '''
        <h1>Contato</h1>
        <p>Professor: Ronan Adriel Zenatti</p>
        <p>FATEC Jahu - Gestão da Tecnologia da Informação</p>
        <a href="/">Voltar ao início</a>
    '''

@app.route('/aluno/<nome>')
def aluno(nome):
    return f'<h1>Aluno</h1><p>{nome}</p><p>FATEC Jahu - Gestão da Tecnologia da Informação</p><a href="/">Voltar ao início</a>'

if __name__ == '__main__':
    app.run(debug=True)
