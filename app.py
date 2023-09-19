import os
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=30)
bootstrap = Bootstrap(app)

# Configuración de mensajes de 'flash'
app.config["FLASH_MESSAGES"] = True
app.config["FLASH_MESSAGES_CATEGORY"] = "message"

listado = [
    {"Nombre": 'Jose', "Clase": "Matemáticas", "Materia": "Álgebra", "Calificación": 85},
    {"Nombre": 'Jose', "Clase": "Tecnología", "Materia": "Biología", "Calificación": 92},
    {"Nombre": 'Jose', "Clase": "Historia", "Materia": "Geografía", "Calificación": 78},
    {"Nombre": 'Jose', "Clase": "Arte", "Materia": "Pintura", "Calificación": 95},
    {"Nombre": 'Jose', "Clase": "Música", "Materia": "Piano", "Calificación": 88},
    {"Nombre": 'Jose', "Clase": "Deportes", "Materia": "Fútbol", "Calificación": 70},
    {"Nombre": 'Jose', "Clase": "Idiomas", "Materia": "Inglés", "Calificación": 90},
    {"Nombre": 'Jose', "Clase": "Ciencias", "Materia": "Física", "Calificación": 82},
    {"Nombre": 'Pedro', "Clase": "Matemáticas", "Materia": "Álgebra", "Calificación": 78},
    {"Nombre": 'Pedro', "Clase": "Tecnología", "Materia": "Biología", "Calificación": 73},
    {"Nombre": 'Pedro', "Clase": "Historia", "Materia": "Geografía", "Calificación": 68},
    {"Nombre": 'Pedro', "Clase": "Arte", "Materia": "Pintura", "Calificación": 91},
    {"Nombre": 'Pedro', "Clase": "Música", "Materia": "Piano", "Calificación": 73},
    {"Nombre": 'Pedro', "Clase": "Deportes", "Materia": "Fútbol", "Calificación": 79},
    {"Nombre": 'Pedro', "Clase": "Idiomas", "Materia": "Inglés", "Calificación": 91},
    {"Nombre": 'Pedro', "Clase": "Ciencias", "Materia": "Física", "Calificación": 59}
]

# Definir el formulario de contacto
class ContactForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(min=5)])
    email = StringField("Correo Electrónico", validators=[DataRequired(), Email()])
    message = StringField("Mensaje", validators=[DataRequired()])
    submit = SubmitField("Enviar")


@app.route("/")
def index():
    name = session.get("name")
    return render_template("index.html", name=name)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Aquí puedes manejar el envío del formulario, por ejemplo, enviar un correo electrónico
        # y luego redirigir a otra página o mostrar un mensaje de éxito.
        session["name"] = form.name.data
        flash("Formulario enviado con éxito", "success")
        return redirect(url_for("index"))

    return render_template("contact.html", form=form)

@app.route('/calificaciones/<nombre>')
def calificaciones(nombre):
    # Filtrar la lista listado por el nombre proporcionado
    calificaciones_filtradas = [calificacion for calificacion in listado if calificacion['Nombre'] == nombre]
    return render_template('calificaciones.html', nombre=nombre, calificaciones=calificaciones_filtradas)

if __name__ == "__main__":
    app.run(debug=True)
