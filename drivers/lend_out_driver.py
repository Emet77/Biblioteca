import pprint 
import mysql.connector
from pprint import *
from datetime import datetime



class lend_out_driver():
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
    
    
    
    def buscar_ejemplares_prestamo(self, criterio_busqueda, donde_buscar):
        match donde_buscar:
            case 'Titulo':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,ejemplar.id_ejemplar,obraliteraria.id_obra
                        FROM obraliteraria , ejemplar 
                        WHERE obraLiteraria.titulo LIKE '%{criterio_busqueda}%' 
                        AND obraliteraria.id_obra=ejemplar.id_obra_fk
                        AND ejemplar.disponibilidad=0
                        ORDER BY obraliteraria.titulo;"""
            case 'Autor':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,ejemplar.id_ejemplar,obraliteraria.id_obra
                        FROM obraliteraria , ejemplar 
                        WHERE obraLiteraria.autor LIKE '%{criterio_busqueda}%' 
                        AND obraliteraria.id_obra=ejemplar.id_obra_fk
                        AND ejemplar.disponibilidad=0
                        ORDER BY obraliteraria.autor;"""
            case 'Editorial':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,ejemplar.id_ejemplar,obraliteraria.id_obra
                        FROM obraliteraria , ejemplar 
                        WHERE obraliteraria.editorial LIKE '%{criterio_busqueda}%' 
                        AND obraliteraria.id_obra=ejemplar.id_obra_fk
                        AND ejemplar.disponibilidad=0
                        ORDER BY obraliteraria.editorial;"""
            case 'Identificador':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial, obraliteraria.id_obra 
                        FROM obraliteraria , ejemplar 
                        WHERE obraliteraria.id_obra=(SELECT ejemplar.id_obra_fk FROM ejemplar WHERE ejemplar.id_ejemplar = '{criterio_busqueda}'); """
            case '':
                consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial, obraliteraria.id_obra 
                        FROM obraliteraria 
                        WHERE obraLiteraria.titulo LIKE '%{criterio_busqueda}%' 
                        OR obraLiteraria.autor LIKE '%{criterio_busqueda}%' 
                        OR obraliteraria.editorial LIKE '%{criterio_busqueda}%' 
                        OR obraliteraria.id_obra=(SELECT ejemplar.id_obra_fk FROM ejemplar WHERE ejemplar.id_ejemplar = '{criterio_busqueda}'); """         
        if(criterio_busqueda=='' and donde_buscar==''):
            consulta=f"""SELECT obraliteraria.titulo, obraliteraria.autor, obraliteraria.editorial,ejemplar.id_ejemplar
                        FROM obraliteraria , ejemplar 
                        WHERE obraliteraria.id_obra=ejemplar.id_obra_fk
                        AND ejemplar.disponibilidad=0
                        ORDER BY ejemplar.id_ejemplar;"""  
        resultado_busqueda=self.ejecutar_consulta(consulta)
  
 
        return resultado_busqueda
    
    
    def cursos_disponibles(self):
        consulta="SELECT curso.id_curso , curso.curso FROM curso ORDER BY curso.id_curso;"
        resultado=[]
        resultado=self.ejecutar_consulta(consulta)
        return resultado
    
    def diviciones_disponibles(self):
        consulta="SELECT divicion.id_divicion , divicion.divicion FROM divicion ORDER BY divicion.id_divicion; "
        resultado=[]
        resultado=self.ejecutar_consulta(consulta)
        return resultado
    def verifica_id_socio(self,id_estudiante):
        consulta=f"""SELECT estudiante.nombre, estudiante.dni, estudiante.id_estudiante
                    FROM estudiante 
                    WHERE estudiante.id_estudiante LIKE'{id_estudiante}'or estudiante.dni LIKE'{id_estudiante}';"""
                    
        informacion_estudiante=[]
        informacion_estudiante=self.ejecutar_consulta(consulta)
        
        fecha_actual=datetime.now()
        f=fecha_actual.date()

        return informacion_estudiante
     
    def crear_prestamo(self,
                       id_curso,
                       id_divicion,
                       id_estudiante,
                       tipo_prestamo,
                       lista_ids_ejemplares
                       ):
        #el campo disponibilidad guardara el id al cual se esta enlazando actualmente el libro
        #cuando no este prestado este campo sera 0 y se entendera por ello que esta disponible
        #campo estado_prestamo debe ser inizializado en 0 significando que no esta finalizado
        #cuando este en 1 signifiac que esta finalizado
        fecha=datetime.now()
        fecha_inicio=fecha.date()
        if(tipo_prestamo ==1):   
            #prestamo personal    
            consulta_crea_prestamo_estudiante=f"""INSERT INTO `prestamo`(`id_prestamo`, `id_curso_fk`, `id_divicion_fk`, `id_estudiante_fk`, `tipo_prestamo`, `fecha_inicio`, `fecha_finaliza`) 
                        VALUES (null,'{id_curso}','{id_divicion}','{id_estudiante}','{tipo_prestamo}','{fecha_inicio}',null);"""
            self.ejecutar_consulta(consulta_crea_prestamo_estudiante)
            consulta_id_prestamo=f"""SELECT MAX(id_prestamo) FROM prestamo;"""
            id_ultimo_prestamo=self.ejecutar_consulta(consulta_id_prestamo)
            
            for id in lista_ids_ejemplares:
               
                consulta_crea_detalle_prestamo=f"""INSERT INTO `detalle_prestamo`(`id_detalle_prestamo`, `id_prestamo_fk`, `id_ejemplar_fk`, `fecha_prestado`, `fecha_devuelto`, `finalizado`) 
                                                    VALUES (null,{id_ultimo_prestamo[0][0]},{id},'{fecha_inicio}',null,0);"""
                self.ejecutar_consulta(consulta_crea_detalle_prestamo)
                consulta_id_detalle="SELECT MAX(id_detalle_prestamo) FROM detalle_prestamo;"
                id_detalle=self.ejecutar_consulta(consulta_id_detalle)
                
                consulta_cambia_disp_ejemplar=f"""UPDATE `ejemplar` SET `disponibilidad`= {id_detalle[0][0]} WHERE ejemplar.id_ejemplar={id}"""
                self.ejecutar_consulta(consulta_cambia_disp_ejemplar)
            return True
        
            #retornar un mesaje o algo para mostrar que el prestamo fue exitoso o si hubo algun error
        elif(tipo_prestamo ==0):
            consulta_crea_prestamo_grupal=f"""INSERT INTO `prestamo`(`id_prestamo`, `id_curso_fk`, `id_divicion_fk`, `id_estudiante_fk`, `tipo_prestamo`, `fecha_inicio`, `fecha_finaliza`) 
                        VALUES (null,'{id_curso}','{id_divicion}',null,'{tipo_prestamo}','{fecha_inicio}',null);"""
            self.ejecutar_consulta(consulta_crea_prestamo_grupal)
            consulta_id_prestamo=f"""SELECT MAX(id_prestamo) FROM prestamo;"""
            id_ultimo_prestamo_grup=self.ejecutar_consulta(consulta_id_prestamo)
            
            for id in lista_ids_ejemplares:
           
                consulta_crea_detalle_prestamo=f"""INSERT INTO `detalle_prestamo`(`id_detalle_prestamo`, `id_prestamo_fk`, `id_ejemplar_fk`, `fecha_prestado`, `fecha_devuelto`,`finalizado`) 
                                                    VALUES (null,{id_ultimo_prestamo_grup[0][0]},{id},'{fecha_inicio}',null,0);"""
                self.ejecutar_consulta(consulta_crea_detalle_prestamo)
                consulta_id_detalle="SELECT MAX(id_detalle_prestamo) FROM detalle_prestamo;"
                id_detalle=self.ejecutar_consulta(consulta_id_detalle)
                
                consulta_cambia_disp_ejemplar=f"""UPDATE `ejemplar` SET `disponibilidad`= {id_detalle[0][0]} WHERE ejemplar.id_ejemplar={id}"""
                self.ejecutar_consulta(consulta_cambia_disp_ejemplar)
            return True
    
    def busca_prestamo(self, donde_buscar):
        E='Finalizado', 'Sin finalizar', 'Grupal','Personal'
        match donde_buscar:
            case 'Finalizado':
                condicion='prestamo.estado_prestamo=True'
            case 'Sin finalizar':
                condicion='prestamo.estado_prestamo=False'
            case 'Grupal':
                condicion='prestamo.tipo_prestamo=False'
            case 'Personal':
                condicion='prestamo.tipo_prestamo=True'

        criterio=''
        lista_inf_prestamo=[]
        if(criterio==''):
            consuta_todo=f"""SELECT prestamo.id_estudiante_fk, prestamo.id_curso_fk, prestamo.id_divicion_fk, prestamo.fecha_inicio,prestamo.fecha_finaliza, prestamo.id_prestamo 
                            FROM `prestamo`
                            WHERE {condicion};
                            """
            resultado=self.ejecutar_consulta(consuta_todo)
            
            for registro in resultado:
                pprint(registro)
                i=0
                info_mostrar=[]
                for indice in registro:
                    match i:
                        case 0:
                            campo="estudiante.nombre "
                            tabla="estudiante"
                            condicion="estudiante.id_estudiante"
                        case 1:
                            campo="curso.curso"
                            tabla="curso"
                            condicion="curso.id_curso"
                        case 2:
                            campo="divicion.divicion"
                            tabla="divicion"
                            condicion="divicion.id_divicion"
                    if(indice!=None ):
                        if(i<=2):
                            # print("se ejecuta esta consulta para obtener el dato ", campo , "correspondiente al indice ", indice)
                            consulta_general=f"""SELECT {campo} FROM {tabla} WHERE {condicion} ={indice};"""
                            # print(consulta_general)
                            dato=self.ejecutar_consulta(consulta_general)
                            info_mostrar.append(dato[0][0])
                        else:
                            # print("agrega el campo Date correspondiente al indice", i)
                            info_mostrar.append(indice)
                                
                    elif(indice==None):
                        # print("se agrega un campo vacio, porque el indice esta vacio")
                        info_mostrar.append('')
                    i+=1 
                lista_inf_prestamo.append(info_mostrar)
            return(lista_inf_prestamo)
    
    def busca_detalle_prestamo(self, id_prestamo):
        #necesito el ide del pretamo y con ese ide buscar los detalles del prestamo en la bd para que sean tomados
        consulta=f"""SELECT detalle_prestamo.id_ejemplar_fk, detalle_prestamo.fecha_prestado, fecha_devuelto
                        FROM detalle_prestamo
                        WHERE detalle_prestamo.id_prestamo_fk={id_prestamo};"""
        devuelve_resultado=self.ejecutar_consulta(consulta)
        lista_detalle=[]
        for detalle in devuelve_resultado:
            lista_inf_detalle=[]
  
            id_ejem=detalle[0]
            consulta_titulo=f"""SELECT obraliteraria.titulo
                                FROM obraliteraria
                                WHERE obraliteraria.id_obra=(SELECT ejemplar.id_obra_fk FROM ejemplar WHERE ejemplar.id_ejemplar={id_ejem} ); """
            titulo=self.ejecutar_consulta(consulta_titulo)   
            lista_inf_detalle.append(titulo[0][0])
            lista_inf_detalle.append(detalle[0])
            lista_inf_detalle.append(detalle[1])
            if(detalle[2]!=None):
                lista_inf_detalle.append(detalle[2])
            else:
                lista_inf_detalle.append('')
            lista_detalle.append(lista_inf_detalle)
            pprint(lista_detalle)
        return lista_detalle
        
    def devuelve_ejemplar(self,id_ejemplar_dev):
        #evaluar antes de devolver un libro si este fue prestado
        fech=datetime.now()
        devolucion_fech=fech.date()
        consulta_id_detalle=f"SELECT ejemplar.disponibilidad FROM ejemplar WHERE ejemplar.id_ejemplar={id_ejemplar_dev};"
        id_detalle=self.ejecutar_consulta(consulta_id_detalle)
        print("consulta el numero identificador del detalle: ", id_detalle[0][0])
        if(id_detalle==0):
            return False
        else:    
            
            
            consulta_finaliza_detalle=f"UPDATE `detalle_prestamo` SET `fecha_devuelto`= '{devolucion_fech}',`finalizado`=1 WHERE detalle_prestamo.id_detalle_prestamo={id_detalle[0][0]}"
            self.ejecutar_consulta(consulta_finaliza_detalle)
            print(consulta_finaliza_detalle)
            consulta_actualiza_disp=f"""UPDATE `ejemplar` SET `disponibilidad`=0 WHERE ejemplar.id_ejemplar={id_ejemplar_dev};"""    
            print(consulta_actualiza_disp)
            self.ejecutar_consulta(consulta_actualiza_disp)
    
            consulta_id_prestamo=f"SELECT detalle_prestamo.id_prestamo_fk FROM detalle_prestamo WHERE detalle_prestamo.id_detalle_prestamo={id_detalle[0][0]};"
            numero_prestamo=self.ejecutar_consulta(consulta_id_prestamo)
            
            consulta_detalle_finaliza=f"SELECT detalle_prestamo.finalizado FROM detalle_prestamo WHERE detalle_prestamo.id_prestamo_fk={numero_prestamo[0][0]};"         
            finaliza_prestamo=self.ejecutar_consulta(consulta_detalle_finaliza)
            pprint(finaliza_prestamo)
            bandera=True
            for estado_detll in finaliza_prestamo:
                print(estado_detll[0])
                if(estado_detll[0]==0):
                    bandera=False
                  
                print(estado_detll)
            
            if(bandera==True):
                print('el prestamo se da por finalizado')
                consulta_finaliza_prestamo=f"""UPDATE `prestamo` SET `fecha_finaliza`='{devolucion_fech}',`estado_prestamo`=1 
                                                WHERE prestamo.id_prestamo={numero_prestamo[0][0]}"""
                self.ejecutar_consulta(consulta_finaliza_prestamo)
            elif(bandera==False):
                print("esto todavia no se acaba")
            
            return True

        