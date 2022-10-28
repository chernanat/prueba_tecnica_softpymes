"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import get_companies,get_colors,get_branches,get_items,get_thirds


terceros = get_thirds()

for i in terceros:
  lista_nombres = []
  if (i['tradename'] != ''):
    lista_nombres.append(i['tradename'])
  else: 
    nombre = i['firstname'] + i['lastname'] + i['maidenname']
    lista_nombres.append(nombre)
    lista_nombres.sort()
    for i in lista_nombres:
      print(i)
