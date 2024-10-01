import pprint 
import mysql.connector
from pprint import *
from datetime import datetime



class partner_management_driver():
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
    
    
    def buscar_socio(self, criterio):
        consulta=f"""SELECT estudiante.id_estudiante , estudiante.nombre , estudiante.telefono , estudiante.dni
                    FROM `estudiante` WHERE estudiante.dni LIKE '%{criterio}%' OR estudiante.nombre LIKE '%{criterio}%'
                    ORDER BY estudiante.id_estudiante DESC;"""

        resultado = self.ejecutar_consulta(consulta)
        return resultado
    def editar_datos_socio(self , id, nombre, telefono, dni):
        consulta=f"""UPDATE `estudiante` SET `nombre`='{nombre}',`telefono`={telefono},`dni`={dni} 
                        WHERE estudiante.id_estudiante = {id};"""
        resultado=self.ejecutar_consulta(consulta)
        
    def crear_socio(self, nombre , telefono, dni):
        #consulta para ver si existe otro un dni con el mismo numero
        #¿Deberia realizar una consulta para ver que no se repitan los dni?

        consulta=f"""INSERT INTO `estudiante`(`id_estudiante`, `nombre`, `telefono`, `dni`) 
                     VALUES (null,'{nombre}',{telefono},{dni})"""
        resultado=self.ejecutar_consulta(consulta)
    
    def eliminar_socio(self, id):
        # verificar primero si el id de socio existe de otra manera no se puede eliminar
        consulta=f"""DELETE FROM `estudiante` WHERE estudiante.id_estudiante={id};"""
        resultado=self.ejecutar_consulta(consulta)
        