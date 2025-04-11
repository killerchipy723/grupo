from flask import Flask,render_template,request,redirect,url_for,flash
from db import db_getConnection

app = Flask(__name__)

#Ruta Principa 
@app.route("/",methods=['GET','POST'])
def principal():
    return render_template("index.html")

#Ruta para insertar alumnos
@app.route("/Registro",methods=['POST'])
def reg_Alumno():
    conexion = db_getConnection()
    if request.method =='POST':
        apenomb = request.form['apenomb']
        dni = request.form['dni']
        colegio = request.form['colegio']
        tutor = request.form['tutor']
        dnitutor = request.form['dnitutor']
        telefono = request.form['telefono']
        query = "INSERT INTO alumno (apenomb,dni,colegio,tutor,dnitutor,telefono)VALUES(%s,%s,%s,%s,%s,%s)"
        cursor = conexion.cursor()
        cursor.execute(query,(apenomb,dni,colegio,tutor,dnitutor,telefono))
        conexion.commit()
        print('Registro Exitoso')
        return redirect(url_for('principal'))
    else:
        print("Error al Guardar el Registro")



#Correr Aplicacion
if __name__=='__main__':
    app.run(debug=True)

