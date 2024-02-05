import mysql.connector

class ObraLiteraria:
    def __init__(self , titulo, autor, cantidad_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_ejemplares = cantidad_ejemplares
    
    def ejecutar_consulta(self, consulta):
        self.consulta = consulta
        conexion = mysql.connector.connect( host='localhost' , user='root' , passwd='' , database='bibliotecaies')
        cursor= conexion.cursor()
        cursor.execute(consulta)
        resultado= cursor.fetchall()
        conexion.commit()
        return resultado
    
    def validar_obra(self, titulo, autor ):
        consulta= f"SELECT COUNT(idObra) FROM obraliteraria WHERE `titulo`='{titulo}' AND `autor` ='{autor}' ;"
        resultado_consulta = self.ejecutar_consulta(consulta)
        print(resultado_consulta)
        if resultado_consulta[0][0] == 0:
            return True
        else:
            return False
        
    def buscar_obra(self,criterio):
        self.criterio=criterio    
        consulta_obras=f"SELECT obraliteraria.titulo , obraliteraria.autor, obraliteraria.idObra FROM obraliteraria  WHERE obraLiteraria.autor LIKE '%{self.criterio}%' OR obraLiteraria.titulo LIKE '%{self.criterio}%';"
        obras_buscadas=self.ejecutar_consulta(consulta_obras)
      
        lista_de_obras=[]
        for obra in obras_buscadas:
             cantida_ejemplares_obra=[]   
             cantida_ejemplares_obra.append(obra[0])#Titulo
             cantida_ejemplares_obra.append(obra[1])#Autor
             cantida_ejemplares_obra.append(obra[2])#id De la obra
             
             consulta_cantidad=f"SELECT COUNT(idEjemplar) FROM ejemplar WHERE idObra = {obra[2]};"
             cantidad_ejemplares=(self.ejecutar_consulta(consulta_cantidad))#cantidad de ejemplares de esta obra
             cantida_ejemplares_obra.append(cantidad_ejemplares)
             
             lista_de_obras.append(cantida_ejemplares_obra)
        return lista_de_obras
    
    
    
    def crear_obra(self, titulo, autor,importancia, cantidad):
        revisar_datos= self.validar_obra(titulo , autor)
        if revisar_datos==True:
            if(importancia=="SI"):
                evalua=1
            else:
                evalua=0
            nueva_obra=f"INSERT INTO `obraliteraria`(`idObra`, `titulo`, `autor`, `importancia`) VALUES (null,'{titulo}','{autor}','{evalua}');"
            id_obra_nueva=f"SELECT obraliteraria.idObra FROM obraliteraria  WHERE obraLiteraria.autor ='{autor}' and obraLiteraria.titulo ='{titulo}';"
            self.ejecutar_consulta(nueva_obra)
            captura_id=self.ejecutar_consulta(id_obra_nueva)
            id=captura_id[0][0]
            self.agrega_ejemplar(id , cantidad) 
            return True
        else:
            return False
    
    def agrega_ejemplar(self,idObra,cantida):
        consulta=f"INSERT INTO `ejemplar`(`idEjemplar`, `idObra`, `estado`) VALUES (null,'{idObra}',1);"
        cont=1
      
        while cont <= cantida:
            cont=cont+1
            resultado=self.ejecutar_consulta(consulta)
        return True
        
    
    def eliminar_obra(self,id_obra):
        try:
            elim_obra=f"DELETE FROM obraliteraria WHERE `obraliteraria`.`idObra` = {id_obra};"
            self.ejecutar_consulta(elim_obra)
            return True
        except mysql.connector.errors.DatabaseError:
            return False
        
            
            
    def eliminar_ejemplar(self,id_ejemp):
        exist_ejemplar= f"SELECT COUNT(idEjemplar) FROM ejemplar WHERE idEjemplar = {id_ejemp};"
        comprueba=self.ejecutar_consulta(exist_ejemplar)
         
        if(comprueba[0][0] >0):
            consulta_elim=f"DELETE FROM `ejemplar` WHERE `ejemplar`.`idEjemplar` = {id_ejemp}; "
            self.ejecutar_consulta(consulta_elim)
            return True
        elif(comprueba[0][0]==0):
            return False
            
        
        
    def modificar_obra(self, titulo , autor , id_obra):
        consulta_edita=f"UPDATE `obraliteraria` SET  `titulo`='{titulo}',`autor`='{autor}'  WHERE `idObra`= {id_obra}"
        try:
            self.ejecutar_consulta(consulta_edita)
            return True
        except:
            return False
        
    





