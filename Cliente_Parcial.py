#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


'''Librerias'''
import requests #libreria request 
import json
import random
from datetime import datetime
URICliente = "http://restdelivery.azurewebsites.net/clientes/"
URIPaquete = "http://restdelivery.azurewebsites.net/paquetes/"
URIFactura = "http://restdelivery.azurewebsites.net/factura/"
def get_all_cliente():
    r = requests.get(URICliente) 
    z = json.loads(r.text)
    y = z['clientes']
    for i in range(len(y)):
        print("\tNombre: ", y[i]['nombre'],
              "\n\tApellido: ", y[i]['apellidos'],
              "\n\tCédula: ", y[i]['id'],
              "\n\tDirección: ", y[i]['direccion'],
              "\n\tCodigo Postal: ", y[i]['cpostal'])

def get_cc():
    r = requests.get(URICliente) 
    z = json.loads(r.text)
    y = z['clientes']
    p = []
    for i in range (len(y)):
        p.append(y[i]['id']) 
    return p
    
def get_one_cliente(ID):
    r = requests.get(URICliente+ID)
    z = json.loads(r.text)
    y = z['clt']
    i = 0
    print("\tNombre: ", y[i]['nombre'],
              "\n\tApellido: ", y[i]['apellidos'],
              "\n\tID: ", y[i]['id'],
              "\n\tDirección: ", y[i]['direccion'],
              "\n\tCodigo Postal: ", y[i]['cpostal'])
def add_cliente(codigo, nombre, apellidos, direc, cp):
    new_data ={
         'id':codigo,
         'nombre':nombre,
         'apellidos':apellidos,
         'direccion': direc,
         'cpostal': cp
    }
    requests.post(URICliente, json = new_data)
    return ("Successful")
def edit_cliente(codigo, value, tipo):
    if tipo == 1: 
        new_data = {
            'nombre': value
        }        
        requests.put(URICliente + codigo, json = new_data)
        
    if tipo == 2:
        new_data = {
            'apellidos': value
        }        
        requests.put(URICliente + codigo, json = new_data)
    if tipo == 3: 
        new_data = {
            'direccion': value
        }        
        requests.put(URICliente + codigo, json = new_data)
    if tipo == 4:
        new_data = {
            'cpostal': value
        }        
        requests.put(URICliente + codigo, json = new_data)
def delete(ID, URI):
    r = requests.delete(URI + ID)
    return ("Successful")
def generarId(cant):
    return (random.randint(10,99)*cant)

def crear_paquete(nombre, precio, destino):
    id_paq = generarId(1000)
    r = requests.get(URIPaquete+"trayectoria/"+destino) 
    new_data ={
         'id_paq':str(id_paq),
         'nombre_paq':nombre,
         'precio':precio,
         'destino': destino,
         'trayectoria': r.text
    }
    requests.post(URIPaquete, json = new_data)
    r = requests.get(URIPaquete+str(id_paq)) 
    return json.loads(r.text)


def ver_paquete(id_paq):
    r = requests.get(URIPaquete+id_paq)
    z = json.loads(r.text)
    y = z['pqt']
    i = 0
    print("\tNombre: ", y[i]['nombre_paq'],
          "\n\tPrecio: ", y[i]['precio'],
          "\n\tDestino: ", y[i]['destino'],
          "\n\tCosto trayectoria: ", y[i]['trayectoria'])
    
def ver_all_paquetes(): 
    r = requests.get(URIPaquete)
    z = json.loads(r.text)
    y = z['paquetes']
    for i in range(len(y)):
        print("\tNombre: ", y[i]['nombre_paq'],
          "\n\tPrecio: ", y[i]['precio'],
          "\n\tDestino: ", y[i]['destino'],
          "\n\tCosto trayectoria: ", y[i]['trayectoria'])
def crear_factura(id_cliente, paquetes):
    id_fac = generarId(12345)
    fecha = datetime.now()
    total = 0
    for i in range(len(paquetes)):
        total += (int(paquetes[i][0]["precio"])+int(paquetes[i][0]["trayectoria"]))
    new_data ={
        'id_factura': str(id_fac),
        'id_cliente': str(id_cliente),
        'fecha': str(fecha),
        'paquetes': paquetes,
        'total': str(total)
    }
    requests.post(URIFactura, json = new_data)
    return id_fac
def ver_factura(id_fac):
    r = requests.get(URIFactura+id_fac)
    z = json.loads(r.text)
    y = z['fct']
    i = 0
    print("\tID Factura: ", y[i]['id_factura'],
          "\n\tID Cliente: ", y[i]['id_cliente'],
          "\n\tFecha: ", y[i]['fecha'])
    paq = y[i]['paquetes']
    print("\tPaquetes: ")
    for i in range (len(paq)):
        print ("\t",i+1, paq[i][0]['nombre_paq'])
    print("\n\tTotal: ", y[0]['total'])

if __name__ == '__main__':
    tray = [
        'local', 'Centro América', 'Norte América',
        'Sur América', 'Europa', 'Asia', 
        'África'
        ]
    paq = [] 
    bd = get_cc()
    if not bd:
        print("\t\tBienvenido")
        print("\n\tPorfavor ingrese sus datos de usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cc = input("Cedula de ciudadanía: ")
        direc = input("Dirección: ")
        cp = input("Código postal: ")
        print(add_cliente(cc, nombre, apellido, direc, cp))
    if bd:
        cc = input("Cedula de ciudadanía: ")
        if cc in bd:
            print("\t\tBienvenido")
        else: 
            print("\t\tBienvenido")
            print("\n\tPorfavor ingrese sus datos de usuario")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            direc = input("Dirección: ")
            cp = input("Código postal: ")
            print(add_cliente(cc, nombre, apellido, direc, cp))
            
            
            
    
        
    while True: 
        print("*************************Opciones*************************")
        print("\t\t1. Usuario")
        print("\t\t2. Crear Paquetes")
        print("\t\t3. Concretar entrega")
        print("\t\t4. Salir")
        print("**********************************************************")
        try:
            opc= int(input("Seleccione una opción: "))
            if opc in range(5): 
                if opc == 1: 
                    while True: 
                        print("\t1. Editar usuario")
                        print("\t2. Ver todos los usuarios")
                        print("\t3. Eliminar usuario")
                        print("\t4. Atras")
                        try: 
                            opc2 = int(input("Seleccione una opción: "))
                            if opc2 in range(5):
                                    if opc2 == 1: 
                                        while True:
                                            codigo = input("Ingrese la Cedula: ")
                                            print("1. Editar nombre.")
                                            print("2. Editar apellido.")
                                            print("3. Editar direccion.")
                                            print("4. Editar codigo postal.")
                                            opc3 = int(input("Seleccione una opción:"))
                                            if opc3 == 1:
                                                nombre = input("Nombre: ")
                                                edit_cliente(codigo, nombre, opc3)
                                                get_one_cliente(codigo)
                                                break
                                            if opc3 == 2: 
                                                apellido = input("Apellido: ")
                                                edit_cliente(codigo, apellido, opc3)
                                                get_one_cliente(codigo)
                                                break
                                            if opc3 == 3: 
                                                direccion = input("Direccion: ")
                                                edit_cliente(codigo, direccion, opc3)
                                                get_one_cliente(codigo)
                                                break
                                            if opc3 == 4: 
                                                cp = input("Codigo postal: ")
                                                edit_cliente(codigo, cp, opc3)
                                                get_one_cliente(codigo)
                                                break
                                            else: 
                                                ("Opción invalida")
                                    if opc2 == 2: 
                                          get_all_cliente()
                                    if opc2 == 3: 
                                        codigo = input("Ingrese la cedula a eliminar: ")
                                        delete(codigo, URICliente)
                                    if opc2 == 4:
                                        break
                            else:
                                print('Opción invalida')
                        except ValueError:
                            print("Error, ingrese solamente numeros")                         
                    
                if opc == 2:
                    print("\tCrear paquete")
                    nombre_paq = input("Ingrese el nombre de su producto: ")
                    precio = input("Ingrese el precio: ")
                    for i in range( len(tray)):
                        print(i+1,".",tray[i])
                    sel= int(input("Seleccione>>"))
                    destino = tray[sel-1]
                    p = crear_paquete(nombre, precio, destino)
                    paq.append(p['pqt'])
                    while True:
                        print("\t1. Ver mis paquetes")
                        print("\t2. Eliminar paquete")
                        print("\t3. Atras")
                        try:
                            opc2 = int(input("Seleccione una opción: "))
                            if opc2 in range(4):
                                if opc2 == 1:
                                    for i in range (len(paq)):
                                        print("Mis paquetes: ")
                                        print(paq)
                                        print("\tNombre: ", paq[i][0]['nombre_paq'],
                                              "\n\tPrecio: ",paq[i][0]['precio'],
                                              "\n\tID: ", paq[i][0]['id_paq'],
                                              "\n\tDestino: ", paq[i][0]['destino'],
                                              "\n\tCosto trayectoria: ", paq[i][0]['trayectoria'])
                                if opc2 == 2:
                                    ID = input("Ingrese ID de paquete: ")
                                    delete(ID, URIPaquete)
                                    for i in range(len(paq)):
                                        if  paq[i][i]['id_paq'] == ID:
                                            paq.pop(i)
                                    
                                if opc2 == 3: 
                                    break
                            else:
                                print('Opción invalida')
                        
                        except ValueError:
                            print("Error, ingrese solamente numeros")           
                                    
                                    
                                
                    
                if opc == 3:
                    print("\n¡Gracias por preferirnos!")
                    print("\n\tFactura de envío")
                    id_fac = crear_factura(cc, paq)
                    ver_factura(str(id_fac))
                    print("\n")
                
                if opc == 4: 
                    break
                    
                            

            else:
                print('Opción invalida')
        except ValueError:
            print("Error, ingrese solamente numeros")
    

    
    
    
    
        
    
    
    
    
    
    
        
        


    
    
    


# In[ ]:





# In[ ]:




