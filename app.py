from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/aluno/<nome>')
def aluno(nome):
    return f'<h1>Aluno</h1><p>{nome}</p><p>FATEC Jahu - Gestão da Tecnologia da Informação</p><a href="/">Voltar ao início</a>'

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():

    if request.method == 'POST':
        nome = request.form['nome']
        nro1 = float(request.form['nro1'])
        nro2 = float(request.form['nro2'])

        soma = nro1 + nro2
        sub = nro1 - nro2
        mult = nro1 * nro2
        div = nro1 / nro2

        return redirect(url_for('exibir_resultado', 
                                nome = nome, 
                                soma = soma, 
                                sub = sub, 
                                mult = mult, 
                                div = div))

    return render_template('formulario.html')

@app.route('/exibir')
def exibir_resultado():
    nome = request.args.get('nome')
    soma = request.args.get('soma')
    sub = request.args.get('sub')
    mult = request.args.get('mult')
    div = request.args.get('div')

    return render_template('exibir.html', 
                            nome = nome, 
                            soma = soma, 
                            sub = sub, 
                            mult = mult, 
                            div = div)

if __name__ == '__main__':
    app.run(debug=True)
