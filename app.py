from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
from db import db_getConnection

app = Flask(__name__)
app.secret_key = 'clave-super-secreta'

#--------------------------Ruta Principal----------------------------------------------------- 
@app.route("/", methods=['GET', 'POST'])
def principal():
    conexion = db_getConnection()
    cursor = conexion.cursor()
    cursor2 = conexion.cursor()
    query = "SELECT * FROM alumno"
    query2 = "SELECT * FROM colegio"
    query3 = "SELECT * FROM evento"
    cursor.execute(query)
    cursor2.execute(query2)
    cursor3 = conexion.cursor()
    cursor3.execute(query3)
    data = cursor.fetchall()
    data2 = cursor2.fetchall()
    data3 = cursor3.fetchall()

    return render_template("index.html", alumno=data, colegio=data2,evento=data3)

#------------------------- Ruta Buscar Alumnos -------------------------------------------
@app.route("/buscar_alumnos")
def buscar_alumnos():
    q = request.args.get('q', '').lower()
    conexion = db_getConnection()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT idalumno, apenomb, dni FROM alumno WHERE LOWER(apenomb) LIKE %s OR dni LIKE %s",
        (f'%{q}%', f'%{q}%')
    )
    resultados = cursor.fetchall()

    # Incluí el idalumno en la respuesta
    return jsonify([{'idalumno': r[0], 'nombre': r[1], 'dni': r[2]} for r in resultados])



#------------------------ Ruta para Registrar Colegio-------------------------------------

@app.route("/Colegio",methods=['POST'])
def agregar_Colegio():
    conexion = db_getConnection()
    if request.method=='POST':
        nombre = request.form['nombre']
        localidad = request.form['localidad']
        query = 'INSERT INTO colegio(nombre,localidad)VALUES(%s,%s)'
        cursor = conexion.cursor()
        cursor.execute(query,(nombre,localidad))
        conexion.commit()
        flash('Registro Exitoso','success')
        return redirect(url_for('principal'))
    else:
        flash('Error al guardar el Registro','danger')

#------------------------------- ruta para registrar Evento -------------------------------------

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

#------------------- Ruta para registrar grupo Familiar -------------------------------------------
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
       

#------------------------Ruta para insertar alumnos------------------------------------------------------------
@app.route("/Registro",methods=['POST'])
def reg_Alumno():
    conexion = db_getConnection()
    if request.method =='POST':
        apenomb = request.form['apenomb']
        dni = request.form['dni']
        colegio = request.form['idcolegio']
        tutor = request.form['tutor']
        dnitutor = request.form['dnitutor']
        telefono = request.form['telefono']
        query = "INSERT INTO alumno (apenomb,dni,idcolegio,tutor,dnitutor,telefono)VALUES(%s,%s,%s,%s,%s,%s)"
        cursor = conexion.cursor()
        cursor.execute(query,(apenomb,dni,colegio,tutor,dnitutor,telefono))
        conexion.commit()         
        flash("Registro Exitoso.","success")
        return redirect(url_for('principal',seccion='alumnos'))
    else:
        flash("No fue posible ingresar el registro.","danger")
    
    
    # -------------- Ruta para Generar Fichas --------------------------------------------------
@app.route("/Ficha", methods=['GET', 'POST'])
def gen_ficha():
    conexion = db_getConnection()
    try:
        if request.method == 'POST':
            idevento = request.form['idevento']
            idalumno = request.form['idalumno']
            fecha = request.form['fecha']
            estado = request.form['estado']
            importe = request.form['importe']
            obs = request.form['obs']

            query = 'INSERT INTO ficha(idevento, idalumno, fecha, estado, importe, obs) VALUES (%s, %s, %s, %s, %s, %s)'
            cursor = conexion.cursor()
            cursor.execute(query, (idevento, idalumno, fecha, estado, importe, obs))
            conexion.commit()

            flash('La ficha se registró correctamente', 'success')
            return redirect(url_for('principal', seccion='regFicha'))
        else:
            flash('No se pudo registrar la ficha, verifique los datos ingresados', 'danger')
    except Exception as e:
        flash(f'Se produjo el siguiente error: {e}', 'danger')

    
    return redirect(url_for('principal', seccion='regFicha'))






    
    




#Correr Aplicacion
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')

