import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from src.blockchain import Blockchain
from hashlib import sha256

blockchain = Blockchain()

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.txt', '.doc', '.docx', '.pdf', '.jpg', '.png', '.jpeg']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 200
filesDir = root_folder + '/files/'
app.config['UPLOAD_FOLDER'] = filesDir

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registrar')
def registrar():
    return render_template('register.html')

@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        motivo = request.form['motivo']
        archivo = request.files['archivo']
        filename = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        fileHash = sha256(filename.encode()).hexdigest()
        hashBloque = blockchain.crearBloque(email, motivo, fileHash)
        print(' -- -- ', email, ' - ', motivo, ' - ', filename)
        print(' -->>> ', fileHash) 
        print(' >>>>> ', hashBloque)
        return render_template('record.html', email=email, fileHash=hashBloque)

@app.route('/validar')
def validate():
    return render_template('validate.html')

@app.route('/detalle/<searchHash>', methods=['GET'])
def detalle(searchHash):
    result = blockchain.getBlockByHash(searchHash)
    if result == 'none':
        return render_template('detailFail.html')
    else:
        email = result.correo
        motivo = result.motivo
        fecha = result.timestamp
        return render_template('detail.html', email = email, motivo = motivo, fecha = fecha)

if __name__ == '__main__':
    app.run(debug=True)