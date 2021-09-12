# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:12:54 2021

@author: jmgar
"""

import requests


# # Creamos la petición HTTP con GET:
# data = requests.get("http://localhost:5002/coches")

# # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
# if data.status_code == 200:
#     data = data.json()
    
#     for d in data.items():
#         print(d[1].get('marca'))
#         print(d[1].get('modelo'))
#         print(d[1].get('cilindrada'))
#         print(d[1].get('kms'))
#         print(d[1].get('matricula'))
#         print("#########################")
          
    
# Creamos la petición HTTP con GET:
data = requests.get("http://localhost:5002/coches", params = {"marca":"BMW", "modelo":"Serie 3"})


# Imprimimos el resultado si el código de estado HTTP es 200 (OK):
if data.status_code == 200:

    data = data.json() #convertimos la respuesta en dict
    for d in data.items():
        print(d[1].get('marca'))
        print(d[1].get('modelo'))
        print(d[1].get('cilindrada'))
        print(d[1].get('kms'))
        print(d[1].get('matricula'))
        print("#########################")

# Creamos la peticion HTTP con POST:
input_data = {'marca': 'Nuevamarca', 'modelo': 'nuevo_modelo', 'matricula': '0000ZZZ', 'kms': 200000, 'cilindrada': 1500}
resp = requests.post('http://localhost:5002/coches', json=input_data)
print (resp)


# Creamos la peticion HTTP con PUT:
input_data = {'marca': 'Actualizamarca', 'modelo': 'actualiza_modelo', 'matricula': '0000ZZZ', 'kms': 300000, 'cilindrada': 1100}
resp = requests.put('http://localhost:5002/coches/2', json=input_data)
print (resp)


# Creamos la peticion HTTP con DELETE:
resp = requests.delete('http://localhost:5002/coches/2')
print (resp)

    
    
    