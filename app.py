from flask import Flask

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return '''
        <h1>Sistema de gestão</h1>
        <p>Bem-vindo ao sistema.</p>
        <a href="/sobre">Sobre</a>
        <a href="/contato">Contato</a>
    '''

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

if __name__ == '__main__':
    app.run(debug=True)
