"""
Este es el programa principal para levantar la pagina web con Flask
La liga del tutorial es: https://youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&si=g2NF73W2qRxZjcPp

En este programa se revisa el concepto de templates para poder correr nuestros propios programas html, css, js

Se debe crear la carpeta "templates" en el mismo directorio donde esta el file .py
"""

# Se importan librerias
from flask import Flask
# Se usan para hacer un redirect al usuario cuando entra a una pagina no autorizada
from flask import redirect, url_for
# Se usa para poder correr nuestros archivos html, css, js
from flask import render_template

# Se crea la instancia de la aplicacion
app = Flask(__name__)

# Variables Globales
user_valid = True

# *********************************** Seccion de Funciones - Rutas de la Web *************************
# Se crean las funciones decoradas que sirven como rutas para las paginas web

# Ruta Home
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para usar un nombre como parametro en el url
@app.route("/<name>")
def user(name):
    return render_template("usuario.html", content=name)

# Ruta para correr html donde se corre codigo python dentro del html
@app.route("/runpy")
def runpy():
    return render_template("runpy.html")

# Se envia una lista a un html
@app.route("/runlist")
def runlista():
    return render_template("runlist.html", content=["Carlos", "Mark", "John", "Ben"])

# ******************************* Secion para Correr la aplicacion **********************************
# Se levanta la aplicacion
if __name__ == "__main__":
    app.run()
            


