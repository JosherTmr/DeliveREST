#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import abort
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
clienteBD = [{}]
paqueteBD = [{}]
@app.route('/')
def home():
    return('''
    <script language="JavaScript" type="text/javascript">

//<![CDATA[

mensagem = prompt("Por favor, ingresa tu nombre",'');

if (mensagem==null) {

document.write("¡Hola, visitante!")

}else{

if (mensagem=='') {

document.write("<b><font face=arial size=5 color=#000000>¡Hola, visitante!<\/font><\/b>")

}else{

document.write("<b><font face=arial size=5 color=#000000>¡Hola "+mensagem+"! Bienvenido a mi sitio<\/font><\/b>");

}

}

//]]>

</script>

<span class="Apple-style-span" style="font-family: 'Trebuchet MS', sans-serif;">

</span>

<span class="Apple-style-span" style="font-family: 'Trebuchet MS', sans-serif;">

</span> ''')
@app.route('/clientes/' or '/clientes' ,methods=['GET'])
def get_all_cientes():
    return jsonify({'clientes': clienteBD})

@app.route('/clientes/<cltId>',methods=['GET'])
def get_clientes(cltId):
    usr = [clt for clt in clienteBD if (clt['id'] == cltId)]
    return jsonify({'clt': usr})

@app.route('/clientes/<cltId>',methods=['PUT'])
def update_clientes(cltId):
    row = [clt for clt in clienteBD if (clt['id'] == cltId)]
    if 'nombre' in request.json:
        row[0]['nombre'] = request.json['nombre']
    if 'apellidos' in request.json:
        row[0]['apellidos'] = request.json['apellidos']
    if 'direccion' in request.json:
        row[0]['direccion'] = request.json['direccion']
    if 'cpostal' in request.json:
        row[0]['cpostal'] = request.json['cpostal']

    return jsonify({'clt': row[0]})

@app.route('/clientes/',methods=['POST'])
def create_cliente():
    dat = {
    'id': request.json['id'],
    'nombre': request.json['nombre'],
    'apellidos': request.json['apellidos'],
    'direccion': request.json['direccion'],
    'cpostal': request.json['cpostal']
    }
    clienteBD.append(dat)
    return jsonify(dat)

@app.route('/clientes/<cltId>',methods=['DELETE'])
def delete_student(cltId):
    row = [clt for clt in clienteBD if (clt['id'] == cltId)]
    if len(row) == 0:
        abort(404)
    clienteBD.remove(row[0])
    return jsonify({'response': 'Success'})

@app.route('/paquetes', methods = ['GET'])
def get_all_paquetes():
    return jsonify({'paquetes': paqueteBD})
@app.route('/paquetes/<pqtId>', methods = ['GET'])
def get_paquetes(pqtId):
    paq = [pqt for pqt in paqueteBD if (pqt['id'] == pqtId)]
    return jsonify({'pqt': paq})

    
    



    

if __name__ == '__main__':
    app.run()


# In[ ]:




