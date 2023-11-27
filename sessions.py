"""
Este es el programa principal para levantar la pagina web con Flask
La liga del tutorial es: https://youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&si=g2NF73W2qRxZjcPp

En este programa se revisa el concepto de Sessions usando GET y POST
De las sessions se utilizan los datos del usuario

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
# Se usa para la funcionalidad de las sessions
from flask import session
# Para usar una funcion para manipula el tiempo de duracion de la session
from datetime import timedelta

# Se crea la instancia de la aplicacion
app = Flask(__name__)
# Secret Key necesaria para usar sessions
app.secret_key = "cmoreno "
app.permanent_session_lifetime = timedelta(minutes=1) # Puede ser: days=5 etc.

# *********************************** Seccion de Funciones - Rutas de la Web *************************
# Se crean las funciones decoradas que sirven como rutas para las paginas web

# Ruta Home
@app.route("/")
def home():
    return render_template("sessions.html")

# Ruta para probar desplegar el login FORM
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        usuario = request.form["nm"]
        # Se crea la session
        session["user"] = usuario
        return redirect(url_for("user"))
    else:
        # Cuando no hay session abierte se envia al usuario a la paginal del login
        return render_template("login.html")

# Ruta para enviar el nombre del usuario cuando hace login
# Se usa esta ruta para mandar la info desde la los datos guardados de la session
@app.route("/user")
def user():
    # Se revisa si hay session activa con la llave de la session["llave"]
    if "user" in session:
        user = session["user"]
        html = f"""
            <h1> Hola Usuario: --> {user}</h1>
            <a href="http://127.0.0.1:5000"> Home </a>
            <br>
            <a href="http://127.0.0.1:5000/logout"> Logout </a>
        """
        # return f"<h1> Hola Usuario: --> {user}</h1>"
        return html
    else:
        return redirect(url_for("login"))

# Logout cerrando sessions data
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

# ******************************* Seccion para Correr la aplicacion **********************************
# Se levanta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
            


