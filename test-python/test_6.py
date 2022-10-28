"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a tener todos los terceros que pertenezcan a esa compañia
"""
from data import get_companies,get_colors,get_branches,get_items,get_thirds

companies = get_companies()

terceros = get_thirds()

for i in companies:
  lista_nombres = []
  nombre = i['name'] 
  if i['firstname']:
    lista_nombres.append(nombre)
    lista_nombres.sort()
  else:
    pass
  for i in terceros:
    for j in companies:
      if (j['id'] == i['companyid']):
        j['companyid'] = i