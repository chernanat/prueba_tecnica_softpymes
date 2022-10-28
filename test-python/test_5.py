"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""
from data import get_companies,get_colors,get_branches,get_items,get_thirds

companies = get_companies()

terceros = get_thirds()

for i in terceros:
  lista_nombres = []
  nombre = i['firstname'] 
  if i['firstname']:
    lista_nombres.append(nombre)
    lista_nombres.sort()
  else:
    pass
  for i in terceros:
    for j in companies:
      if (j['id'] == i['companyid']):
        j['companyid'] = i
        print(companies)
