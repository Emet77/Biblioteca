import os
import pprint
import shutil 
import mysql.connector
from pprint import *
class catalog_driver():
    def __init__(self) -> None:
        pass
    
    def ejecutar_consulta(self, consulta):
        self.consulta = consulta
        conexion = mysql.connector.connect( host='localhost' , user='root' , passwd='' , database='biblioteca4117')
        cursor= conexion.cursor()
        cursor.execute(consulta)
        resultado= cursor.fetchall()
        conexion.commit()
        return resultado 
    
    def buscar_obra_catalogo(self, criterio_busqueda, donde_buscar):
        match donde_buscar:
            case 'Titulo':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra,obraliteraria.portada
                        FROM obraliteraria
                        WHERE obraLiteraria.titulo LIKE '%{criterio_busqueda}%' 
                        ORDER BY obraLiteraria.titulo;"""

            case 'Autor':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra,obraliteraria.portada
                        FROM obraliteraria 
                        WHERE obraLiteraria.autor LIKE '%{criterio_busqueda}%' 
                        ORDER BY obraLiteraria.autor;"""
            case 'Editorial':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra,obraliteraria.portada
                            FROM obraliteraria 
                            WHERE obraLiteraria.editorial LIKE '%{criterio_busqueda}%'
                            ORDER BY obraliteraria.editorial; """
                
            case '':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,obraliteraria.id_obra,obraliteraria.portada
                        FROM obraliteraria
                        ORDER BY obraliteraria.titulo;""" 
                
        resultado_busqueda=self.ejecutar_consulta(consulta)
        lista_datos=[]
        
        for resultado in resultado_busqueda:
            result=list(resultado)
            consulta_disponibles=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {resultado[3]} AND ejemplar.disponibilidad=0; "
            cantidad_ejemplares_disp= self.ejecutar_consulta(consulta_disponibles)
     
            
            consulta_totales=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {resultado[3]};" 
            cantidad_ejemp_total=self.ejecutar_consulta(consulta_totales)
            result.insert(3, cantidad_ejemplares_disp[0][0])
            result.insert(4, cantidad_ejemp_total[0][0])
            
            lista_datos.append(result)
        pprint(lista_datos)
        return lista_datos

    def agregarportada_obra(self ,documento_copia,id_obra):

        documento_copia=documento_copia
        divididos=documento_copia.split('.')#ASI dividimos por secciones la ruta para quedarnos solo con el nombre del archivo
        divididos.reverse()#ponemos el nombre al principio para seleccionarlo
        extencion_archivo=divididos[0]
        actual_dir= os.getcwd()
        dir=shutil.copy(documento_copia, f"{actual_dir}\\resources\\covers\\{id_obra}.{extencion_archivo}") 
        #al parecer este caracter '\' genera problemas en la base de datos pero si lo reemplazamos por '//'
        #se soluciona 
        nuevo_dir=dir.replace('\\','//')
        consulta=f"UPDATE `obraliteraria` SET `portada`='{nuevo_dir} 'WHERE obraliteraria.id_obra={id_obra};"
        self.ejecutar_consulta(consulta)
    
    def eliminar_portada(self, id_obra):
        consulta=f"UPDATE `obraliteraria` SET `portada`=NULL WHERE obraliteraria.id_obra={id_obra};"
        self.ejecutar_consulta(consulta)