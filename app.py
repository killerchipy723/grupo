from flask import Flask,render_template,request,redirect,url_for,flash
from db import db_getConnection

app = Flask(__name__)
app.secret_key = 'clave-super-secreta'

#Ruta Principa 
@app.route("/",methods=['GET','POST'])
def principal():
    if request.method=='GET':
        conexion = db_getConnection()
        query = "select * from alumno"
        cursor = conexion.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    return render_template("index.html",alumno=data)

@app.route("/Evento",methods=['POST'])
def reg_Evento():
    conexion = db_getConnection()
    if request.method=='POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']        
        query = "INSERT INTO evento(nombre,fecha)VALUES(%s,%s)"
        cursor = conexion.cursor()
        cursor.execute(query,(nombre,fecha))
        conexion.commit()
        flash("Registro Exitoso.","success")
        return redirect(url_for('principal'))
    else:
        print("Error al insertar el registro")


@app.route("/RegGrupo",methods=['POST'])
def reg_Grupo():
        conexion = db_getConnection()
        if request.method=="POST":
            idalumno = request.form['alumno']
            nombre = request.form['nombre']
            edad = request.form['edad']
            es = request.form['tipo']
            if not idalumno or not nombre or not edad or not es:
                #flash("Por favor complete todos los campos antes de enviar.")
                return redirect(url_for('reg_Grupo'))  # o el nombre correcto de tu vista/formulario
            query = "INSERT INTO familia(idalumno,nombre,edad,es)VALUES(%s,%s,%s,%s)"
            cursor = conexion.cursor()
            cursor.execute(query,(idalumno,nombre,edad,es))
            conexion.commit()
            flash("Registro Exitoso.","success")
            return redirect(url_for('principal'))
        else:
            print("Error al Guardar el Registro")
       

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
        flash("Registro Exitoso.","success")
        return redirect(url_for('principal'))
    else:
        flash("No fue posible ingresar el registro.","danger")
    
    # Agregar Personas
    
    




#Correr Aplicacion
if __name__=='__main__':
    app.run(debug=True)

