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
                    ORDER BY estudiante.id_estudiante;"""

        resultado = self.ejecutar_consulta(consulta)
        return resultado
    def editar_datos_socio(self , id, nombre, telefono, dni):
        consulta=f"""UPDATE `estudiante` SET `nombre`='{nombre}',`telefono`={telefono},`dni`={dni} 
                        WHERE estudiante.id_estudiante = {id};"""
        resultado=self.ejecutar_consulta(consulta)
        
    def crear_socio(self, nombre , telefono, dni):
        pass