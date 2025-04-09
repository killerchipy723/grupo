from flask import Flask,render_template,request,redirect,url_for,flash

app = Flask(__name__)

#Ruta Principa 
@app.route("/",methods=['GET','POST'])
def principal():
    return render_template("index.html")


#Correr Aplicacion
if __name__=='__main__':
    app.run(debug=True)

