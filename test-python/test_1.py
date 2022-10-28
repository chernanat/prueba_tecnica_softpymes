""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
from data import get_companies,get_colors,get_branches,get_items,get_thirds

class empresas:
    def test1():
        companies = get_companies()
        sucursales = get_branches()
        for i in companies:
            for j in sucursales:
                if (i['branches'][0]) == (j['id']):
                    iterador = 0
                    companies[iterador]['branches'][0] = j
                    iterador+=1
                    print(companies)
consulta = empresas
print(consulta.test1())