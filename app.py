from flask import Flask, render_template, request
from ListaDeCompras import ListaDeCompras

app = Flask(__name__)

lista_compras = ListaDeCompras()

@app.route('/')
def index():
    return render_template('index.html', itens=lista_compras.itens)

@app.route('/adicionar', methods=['POST'])
def adicionar_item():
    item = request.form['item']
    lista_compras.adicionar_item(item)
    return index()

@app.route('/remover', methods=['POST'])
def remover_item():
    item = request.form['item']
    lista_compras.remover_item(item)
    return index()

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 591104f85c6d654aca134809b3210b041ea06369
