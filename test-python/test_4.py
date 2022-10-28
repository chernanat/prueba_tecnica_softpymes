"""
  4) Mostrar de los terceros que se tienen en el archivo data.py 
  los cuales no poseen ni email o no tengan cellPhone.
"""
from data import get_companies,get_colors,get_branches,get_items,get_thirds


terceros = get_thirds()

for i in terceros:
  if (i['email']) == ''  or (i['cellPhone']) == '':
    print(i)