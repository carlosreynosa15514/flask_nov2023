"""
Este es el programa principal para levantar la pagina web con Flask
La liga del tutorial es: https://youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&si=g2NF73W2qRxZjcPp

En este programa se revisa el concepto de templates Inheritance

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

# *********************************** Seccion de Funciones - Rutas de la Web *************************
# Se crean las funciones decoradas que sirven como rutas para las paginas web

# Ruta Home
@app.route("/")
def home():
    return render_template("herencia.html")

# Ruta para probar Herencia con otro file
@app.route("/herencia2")
def herencia2():
    return render_template("herencia2.html")


# ******************************* Secion para Correr la aplicacion **********************************
# Se levanta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
            


