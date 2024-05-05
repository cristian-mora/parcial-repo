from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

# Definir la función para conectar a la base de datos y obtener los productos
def obtener_productos():
    conexion = sqlite3.connect('web2.sqlite3')
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = [dict(producto) for producto in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return productos

# Ruta para la página principal
@app.route('/')
def ruta_raiz():
    productos = obtener_productos()
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
    productos = obtener_productos()  # Obtener la lista de productos
    for producto in productos:
        if pid == producto['id']:
            return render_template('producto.html', producto=producto)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)