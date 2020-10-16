# coding: utf-8
from os import abort
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
clienteBD = []
paqueteBD = []
facturaBD = []
@app.route('/')
def home():
    return("Hola")
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

@app.route('/paquetes/' or '/paquetes', methods = ['GET'])
def get_all_paquetes():
    return jsonify({'paquetes': paqueteBD})
@app.route('/paquetes/<pqtId>', methods = ['GET'])
def get_paquetes(pqtId):
    paq = [pqt for pqt in paqueteBD if (pqt['id_paq'] == pqtId)]
    return jsonify({'pqt': paq})

@app.route('/paquetes/',methods=['POST'])
def create_paquete():
    dat = {
    'id_paq': request.json['id_paq'],
    'nombre_paq': request.json['nombre_paq'],
    'precio': request.json['precio'],
    'destino': request.json['destino'],
    'trayectoria':request.json['trayectoria']
    }
    paqueteBD.append(dat)
@app.route('/paquetes/trayectoria/<Destino>',methods=['GET'])
def set_trayectoria(Destino):
    trayectoriaBD = {
        'local': 3500,
        'Centro América': 5000,
        'Norte América' : 7500,
        'Sur América': 7200,
        'Europa': 12000,
        'Asia': 13500,
        'África': 11350
    }
    return jsonify(trayectoriaBD[Destino])
    
@app.route('/factura/', methods =['POST'])
def crear_factura():
    fac = { 
    'id_factura': request.json['fctId'],
    'id_cliente': request.json['pqtId'],
    'fecha': request.json['fecha'],
    'paquetes': request.json['paquetes'],
    'total' : request.json['total']
    }
    facturaBD.append(fac)
    return jsonify(fac)

@app.route('/factura/<id_factura>', methods= ['GET'])
def get_facturas(id_factura):
    fac = [fct for fct in facturaBD if (fct['id_factura'] == id_factura)]
    return jsonify({'fct': fac})
            

if __name__ == '__main__':
    app.run()






