import pprint 
import mysql.connector
from pprint import *
class catalog_driver():
    def __init__(self) -> None:
        pass
    
    def ejecutar_consulta(self, consulta):
        self.consulta = consulta
        conexion = mysql.connector.connect( host='localhost' , user='root' , passwd='' , database='biblioteca4117test2')
        cursor= conexion.cursor()
        cursor.execute(consulta)
        resultado= cursor.fetchall()
        conexion.commit()
        return resultado 
    
    def buscar_obra_catalogo(self, criterio_busqueda, donde_buscar):
        match donde_buscar:
            case 'Titulo':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra
                        FROM obraliteraria
                        WHERE obraLiteraria.titulo LIKE '%{criterio_busqueda}%' 
                        ORDER BY obraLiteraria.titulo;"""

            case 'Autor':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra
                        FROM obraliteraria 
                        WHERE obraLiteraria.autor LIKE '%{criterio_busqueda}%' 
                        ORDER BY obraLiteraria.autor;"""
            case 'Editorial':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra 
                            FROM obraliteraria 
                            WHERE obraLiteraria.editorial LIKE '%{criterio_busqueda}%'
                            ORDER BY obraliteraria.editorial; """
                
            case '':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra
                        FROM obraliteraria
                        ORDER BY obraliteraria.titulo;""" 
                
        resultado_busqueda=self.ejecutar_consulta(consulta)
        lista_datos=[]
        
        for resultado in resultado_busqueda:
            result=list(resultado)
            consulta_disponibles=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {resultado[3]} AND ejemplar.disponibilidad>0; "
            cantidad_ejemplares_disp= self.ejecutar_consulta(consulta_disponibles)
     
            
            consulta_totales=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {resultado[3]};" 
            cantidad_ejemp_total=self.ejecutar_consulta(consulta_totales)
            result.insert(3, cantidad_ejemplares_disp[0][0])
            result.insert(4, cantidad_ejemp_total[0][0])
            
            lista_datos.append(result)
        
        return lista_datos

