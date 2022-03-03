import string
from flask import Flask, render_template

app = Flask(__name__) #instancia de flask (__variablereservada__)

@app.get("/") #crea_una_ruta
def index():
    return render_template("index.html")           #'<h1>Estas en la pagina de inicio</h1>'

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

#Ruta con parametro
@app.get("/contactos/<contactoId>/edit")
def editarContacto(contactoId):
    suma =2+2

    return render_template('contactos/editar.html', 
        contactoId = contactoId,
        suma = suma
    )

#/edad/27
@app.get("contactos/<int:edadPersona>/edita")
def edad(edadPersona):

    return render_template('contactos/editar1.html', edadPersona = edadPersona)

app.run(debug=True)