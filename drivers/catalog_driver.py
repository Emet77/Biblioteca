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
                #Agregar un where a esta consulta para que devuelva datos cuando se le da un criterio de busqueda
        resultado_busqueda=self.ejecutar_consulta(consulta)
        #solo devolver los datos autor titulo editorial y identific
        #delegar cantidad disponible y cantidad todal en una nueva funcion del controlador
        #tambien delegar la busqueda de la portada
        lista_datos=[]
        for obra in resultado_busqueda:
            lista_datos.append(obra)
        # for resultado in resultado_busqueda:
        #     result=list(resultado)
        #     consulta_disponibles=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {resultado[3]} AND ejemplar.disponibilidad=0; "
        #     cantidad_ejemplares_disp= self.ejecutar_consulta(consulta_disponibles)
     
            
        #     consulta_totales=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {resultado[3]};" 
        #     cantidad_ejemp_total=self.ejecutar_consulta(consulta_totales)
        #     result.insert(3, cantidad_ejemplares_disp[0][0])
        #     result.insert(4, cantidad_ejemp_total[0][0])
            
        #     lista_datos.append(result)

        # pprint(lista_datos)
        return lista_datos
    def ejemplares_disponibles(self,id):
        consulta_disponibles=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {id} AND ejemplar.disponibilidad=0; "
        cantidad_ejemplares_disp= self.ejecutar_consulta(consulta_disponibles)
        return cantidad_ejemplares_disp[0][0]
    def ejemplares_totales(self,id):
        consulta_totales=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {id};" 
        cantidad_ejemp_total=self.ejecutar_consulta(consulta_totales)
        return cantidad_ejemp_total[0][0]
    def mostrar_portada(self,id):
        consulta=f"SELECT `portada` FROM `obraliteraria` WHERE obraliteraria.id_obra={id};"
        portada=self.ejecutar_consulta(consulta)
        return portada[0][0]
    
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
        consulta=f"UPDATE `obraliteraria` SET `portada`='{nuevo_dir}' WHERE obraliteraria.id_obra={id_obra};"
        self.ejecutar_consulta(consulta)
    
    def eliminar_portada(self, id_obra):
        consulta=f"UPDATE `obraliteraria` SET `portada`=NULL WHERE obraliteraria.id_obra={id_obra};"
        self.ejecutar_consulta(consulta)
    def agregar_resumen(self, id_obra , resumen):
        #agregar a la base de datos el campo resumen donde se almacenara el texto con el resumen de la obra
        #f = open("myfile.txt", "x") Ejemplo para crear un archivo en python usando open y agregando "x" como parametro
        # f = open("myfile.txt", "w") crea y sobreescribe si ya existe un archivo con ese nombre
        pass
    def leer_resumen(self, id_obra):
        #consultar la bd por la informacion del texto a leer 
        consulta=f"SELECT `resumen` FROM `obraliteraria` WHERE obraliteraria.id_obra={id_obra}; "
        direccion=self.ejecutar_consulta(consulta)
        if(direccion[0][0]==None):
            # no ejecutar
            n="Este libro no tiene Resumen  :("
            return n
        else:
            # tratar de abrir
            resumen=open(direccion[0][0])
            leer_resumen=resumen.read()
            resumen.close()
            return leer_resumen
            

        
    def guardar_datos(self, id, autor, titulo, editorial, resumen):
        #crear un archivo .txt que sirva de resumen enlazado con el numero de la obra
        actual_dir=os.getcwd()
        resumen_texto = open(f"{actual_dir}\\resources\\summaries\\{id}.txt", "w")
        resumen_texto.write(resumen)
        resumen_texto.close()
        directorio_resumen=f"{actual_dir}\\resources\\summaries\\{id}.txt"
        directorio_resumen_n=directorio_resumen.replace('\\','//')
        print(directorio_resumen)
        print(directorio_resumen_n)
        consulta=f"UPDATE `obraliteraria` SET `resumen`='{directorio_resumen_n}' WHERE obraliteraria.id_obra={id};"
        self.ejecutar_consulta(consulta)
        #ahora que ya crea texto y guarda la ubicacion en la base de datos debemmos agregar los demas datos