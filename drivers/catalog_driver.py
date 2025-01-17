import os
import pprint
import shutil
import tkinter 
import mysql.connector
from pprint import *
import sqlite3
class catalog_driver():
    def __init__(self) -> None:
        pass
    
    def ejecutar_consulta(self, consulta):
        # self.consulta = consulta
        # conexion = mysql.connector.connect( host='localhost' , user='root' , passwd='' , database='biblioteca4117')
        # cursor= conexion.cursor()
        # cursor.execute(consulta)
        # resultado= cursor.fetchall()
        # conexion.commit()
        # return resultado 
        conexion = sqlite3.connect('databaseStructure/sqlite_biblioteca.db')
        cursor= conexion.cursor()
        resultado = cursor.execute(consulta)
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
        
        return lista_datos
    def ejemplares_disponibles(self,id):
        consulta_disponibles=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {id} AND ejemplar.disponibilidad=0; "
        cantidad_ejemplares_disp= self.ejecutar_consulta(consulta_disponibles)
        #print(cantidad_ejemplares_disp.fetchall()) #Debemos agregar el campo fetchall para que los datosque vienen del cursor puedan ser vistos
        disp = cantidad_ejemplares_disp.fetchall()
        print("estos son los disponibles... ",disp[0][0])
        return disp[0][0]
    
    def ejemplares_totales(self,id):
        consulta_totales=f"SELECT COUNT(ejemplar.id_ejemplar) FROM ejemplar WHERE ejemplar.id_obra_fk = {id};" 
        cantidad_ejemp_total=self.ejecutar_consulta(consulta_totales)
        total= cantidad_ejemp_total.fetchall()
        return total[0][0]
    def mostrar_portada(self,id):
        consulta=f"SELECT `portada` FROM `obraliteraria` WHERE obraliteraria.id_obra={id};"
        portada=self.ejecutar_consulta(consulta)
        portada=portada.fetchall()
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
        actual_dir=os.getcwd()
        resumen_texto = open(f"{actual_dir}\\resources\\summaries\\{id_obra}.txt", "w")
        resumen_texto.write(resumen)
        resumen_texto.close()
        directorio_resumen=f"{actual_dir}\\resources\\summaries\\{id_obra}.txt"
        directorio_resumen=directorio_resumen.replace('\\','//')
        consulta=f"UPDATE `obraliteraria` SET `resumen`='{directorio_resumen}' WHERE obraliteraria.id_obra={id_obra};"
        self.ejecutar_consulta(consulta)

    def leer_resumen(self, id_obra):
        #consultar la bd por la informacion del texto a leer 
        consulta=f"SELECT `resumen` FROM `obraliteraria` WHERE obraliteraria.id_obra={id_obra}; "
        direccion=self.ejecutar_consulta(consulta)
        direccion=direccion.fetchall()
        if(direccion[0][0]==None or direccion[0][0]=='NULL' or direccion[0][0]==''):
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
        consulta=f"UPDATE `obraliteraria` SET `resumen`='{directorio_resumen_n}' WHERE obraliteraria.id_obra={id};"
        self.ejecutar_consulta(consulta)
        #ahora que ya crea texto y guarda la ubicacion en la base de datos debemmos agregar los demas datos

    def agregar_obra_existente(self,desde,hasta,titulo,autor,editorial,resumen,portada):
        #validar si el rango de ejemplares esta ocupado por otra obra literaria
        #el rango ingresado es correspondiente a los ids que tendran los ejemplares en su portada,,osea que el campo id_secundario
        #devbe agregarse en la tabla ejemplares
        numero_desde=desde.get()
        numero_hasta=hasta.get()
        titulo=titulo.get()
        autor=autor.get()
        editorial=editorial.get()
        resumen=resumen.get(1.0,tkinter.END)
        portada=portada.get()
    
        #evaluar los numeos de desde y hasta
        if(numero_desde==''or numero_hasta==''):
            return 0
        else:
            int_desde=int(numero_desde)
            int_hasta=int(numero_hasta)
            if(int_desde>int_hasta):
                return 1
            elif(titulo=='' or autor=='' or editorial==''):
                #Los campos de titulo autor o editorial no deben estar vacios
                return 2
            #Como crear la obra con un rango?
            #se toma el ide de la obra creada y apartir de eso se aplica el rango para crear los ejemplares
            #antes de crear los ejemplares debemos comprobar si el rango de id no esta ya utilizado con otro ejemplar
            #la obra se crea normalmente con los datos de la interface

            #La bd no deja insertar datos repetidos en el ide de ejemplar
            #Si nos saltamos el orden en id_ejemplar la bd roma el ultimo id y apartir de ahi continua con la numeracion            
            contador=int_desde
            lista_ejemplares_repetidos=[]
            while(contador<=int_hasta):
                consulta=f"SELECT COUNT(ejemplar.id_ejemplar) FROM `ejemplar` WHERE ejemplar.id_ejemplar={contador};"
                resultado=self.ejecutar_consulta(consulta)
                resultado=resultado.fetchall()
                if(resultado[0][0]!=0):
                    lista_ejemplares_repetidos.append(contador)
                contador=contador+1
            if(lista_ejemplares_repetidos==[]):
                print("No existen ejemplares repetidos. proceder a la creacion de la obra")
                #tomar datos y realizar un insert con la obra
                # consulta=f"INSERT INTO obraliteraria (id_obra ,titulo,autor,editorial,portada,resumen)VALUES (NULL,'{titulo}','{autor}','{editorial}','{portada}','{resumen}');"
                # m=self.ejecutar_consulta(consulta)
                # consulta=f"SELECT max(id_obra)  FROM	obraliteraria;"
                # max_id=self.ejecutar_consulta(consulta)
                # max_id=max_id.fetchall()
                # print("El ide de la ultima obra creada es: ",max_id[0][0])
                # print("ningum ejemplar se repite, Se crea la obra normalmente")
                # print('este es el dir del resumen: ',resumen)
                # #para saber el maximoid de una obra:SELECT max(id_obra)  FROM	obraliteraria;
                # print(type(resumen))
                
                # print('esta es la dir dela port: ',portada)
                # print(type(portada))
                return 1
            elif(lista_ejemplares_repetidos!=[]):
                print("Estos ejemplares se repiten :( ", lista_ejemplares_repetidos)
                print("No continuar con la ejecucion del programa ")
                return lista_ejemplares_repetidos