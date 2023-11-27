"""
Este es el programa principal para levantar la pagina web con Flask
La liga del tutorial es: https://youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&si=g2NF73W2qRxZjcPp

En este programa se revisa el concepto de enviar GET y POST 

Se debe crear la carpeta "templates" en el mismo directorio donde esta el file .py
"""

# Se importan librerias
from flask import Flask
# Se usan para hacer un redirect al usuario cuando entra a una pagina no autorizada
from flask import redirect, url_for
# Se usa para poder correr nuestros archivos html, css, js
from flask import render_template
# Se usa para poder validar los metodos POST y GET
from flask import request

# Se crea la instancia de la aplicacion
app = Flask(__name__)

# *********************************** Seccion de Funciones - Rutas de la Web *************************
# Se crean las funciones decoradas que sirven como rutas para las paginas web

# Ruta Home
@app.route("/")
def home():
    return render_template("get_post.html")

# Ruta para probar desplegar el login FORM
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("usuario", usr=user))
    else:
        return render_template("login.html")

# Ruta para enviar el nombre del usuario
# Se usa esta ruta para mandar la info desde la form con el boton submit
@app.route("/<usr>")
def usuario(usr):
    return f"<h1> Hola Usuario: -->  {usr} </h1>"


# ******************************* Secion para Correr la aplicacion **********************************
# Se levanta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
            


