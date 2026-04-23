from flask import Flask, render_template, request, redirect

app = Flask(__name__)

listaprodutos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=listaprodutos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    data_hora = request.form['dataHora']
    novo = {
        'id': len(listaprodutos) + 1,
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade,
        'dataHora': data_hora,
    }
    listaprodutos.append(novo)
    return render_template('index.html', produtos=listaprodutos)

@app.route('/buscar', methods=['POST'])
def buscar():
    id_str = request.form.get('id')
    if not id_str:
        return redirect('/')
    try:
        id_busca = int(id_str)
    except ValueError:
        return redirect('/')
    result = [p for p in listaprodutos if p['id'] == id_busca]
    return render_template('index.html', produtos=result)


@app.route('/excluir', methods=['POST'])
def excluir():
    id_str = request.form.get('id')
    if not id_str:
        return redirect('/')
    try:
        id_excluir = int(id_str)
    except ValueError:
        return redirect('/')
    
    for p in listaprodutos: 
        if p['id'] == id_excluir:
            listaprodutos.remove(p)
            break
    
    return render_template('index.html', produtos=listaprodutos)

@app.route('/editar', methods=['POST'])
def editar():
    id_str = request.form.get('id')
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    data_hora = request.form['dataHora']
    if not id_str:
        return redirect('/')
    try:
        id_int = int(id_str)
    except ValueError:
        return redirect('/')
    
    for p in listaprodutos:
        if p['id'] == id_int:
            p['nome'] = nome if nome else p['nome']
            p['preco'] = preco if preco else p['preco']
            p['quantidade'] = quantidade if quantidade else p['quantidade']
            p['dataHora'] = data_hora if data_hora else p['dataHora']
            break
    return render_template('index.html', produtos=listaprodutos)

if __name__ == '__main__':
    app.run(debug=True)
