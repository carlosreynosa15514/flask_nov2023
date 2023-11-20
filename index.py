"""
Este es el programa principal para levantar la pagina web con Flask
La liga del tutorial es: https://youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&si=g2NF73W2qRxZjcPp

"""

# Se importan librerias
from flask import Flask
# Se usan para hacer un redirect al usuario cuando entra a una pagina no autorizada
from flask import redirect, url_for 

# Se crea la instancia de la aplicacion
app = Flask(__name__)

# Variables Globales
user_valid = True

# *********************************** Seccion de Funciones - Rutas de la Web *************************
# Se crean las funciones decoradas que sirven como rutas para las paginas web

# Ruta Homa
@app.route("/")
def home():
    return "Esta es Home <h1>Hola aplicacion</h1>"

# Crea una ruta donde se puede envia un parametro
@app.route("/<name>")
def user(name):
    return f"Hello {name} <hr> <a href='http://127.0.0.1:5000'> Regresa a Home </a>"

# Ruta de administrador
@app.route("/admin")
def admin():
    if user_valid:
        return " <h1>Bienvenido Administrador</h1>  <br> <a href='http://127.0.0.1:5000'>Regresa a Home</a>"
    else:
        return redirect(url_for("no_autorizado"))

# Pagina para redirigir al usuario cuando entra a una pagina no autorizada como admin
@app.route("/no_autorizado")
def no_autorizado():
    return "<h1> Usuario no Autorizado </h1>"

# Usando redirect para enviar a una funcion que acepta parametros
@app.route("/aduser")
def aduser():
    return redirect(url_for("user", name="Carlos Usaste adUser"))


# ******************************* Secion para Correr la aplicacion **********************************
# Se levanta la aplicacion
if __name__ == "__main__":
    app.run()
            


