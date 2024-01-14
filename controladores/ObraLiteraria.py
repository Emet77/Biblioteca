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
        
    def traer_todos_los_datos(self):
        consulta = "SELECT * FROM `obraliteraria`"
        self.ejecutar_consulta(consulta)
    def buscar_obra(self,criterio):
        self.criterio=criterio 
        #esto es la consulta de la busqueda     
        consulta_obras=f"SELECT obraliteraria.titulo , obraliteraria.autor, obraliteraria.idObra FROM obraliteraria  WHERE obraLiteraria.autor LIKE '%{self.criterio}%' OR obraLiteraria.titulo LIKE '%{self.criterio}%';"
        #
        #esto es una 'LISTA DE TUPLAS' resultado de ejecutar la busquedad de arriba
        obras_buscadas=self.ejecutar_consulta(consulta_obras)
        #
        
        lista_de_obras=[]
        for obra in obras_buscadas:
             cantida_ejepares_obra=[]   
             cantida_ejepares_obra.append(obra[0])#Titulo
             cantida_ejepares_obra.append(obra[1])#Autor
             cantida_ejepares_obra.append(obra[2])#id De la obra
             
             consulta_cantidad=f"SELECT COUNT(idEjemplar) FROM ejemplar WHERE idObra = {obra[2]};"
             cantidad_ejemplares=(self.ejecutar_consulta(consulta_cantidad))#cantidad de ejemplares de esta obra
             cantida_ejepares_obra.append(cantidad_ejemplares)
             
             lista_de_obras.append(cantida_ejepares_obra)
             
        
         
        return lista_de_obras
    
    
    
    def crear_obra(self, titulo, autor, cantidad, importancia):
        if(importancia=="SI"):
            evalua=1
        else:
            evalua=0
        #print("Desde el controlador de obra literaria: ", titulo, autor, cantidad, importancia)
        consulta=f"INSERT INTO `obraliteraria`(`idObra`, `titulo`, `autor`, `cantidaEjemplares`, `importancia`) VALUES (null,'{titulo}','{autor}','{cantidad}','{evalua}');"
        self.ejecutar_consulta(consulta)
        return True
    def agrega_ejemplar(self,idObra,cantida):
        consulta=f"INSERT INTO `ejemplar`(`idEjemplar`, `idObra`, `estado`) VALUES (null,'{idObra}',1);"
        cont=1
        while cont <= cantida:
            cont=cont+1
            print(cont)
            resultado=self.ejecutar_consulta(consulta)
        
    
    def eliminar_obra(self):
        pass
    
    def modificar_obra(self):
        pass
    
