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
              
        consulta_obras=f"SELECT obraliteraria.titulo , obraliteraria.autor, obraliteraria.idObra FROM obraliteraria  WHERE obraLiteraria.autor LIKE '%{self.criterio}%' OR obraLiteraria.titulo LIKE '%{self.criterio}%';"
        obras_buscadas=self.ejecutar_consulta(consulta_obras)
        #[('La vuelta al mundo en 80 dias', 'Julio Verne', 1),
        # ('DUNE', 'Frank Herbert', 2), ('De la Tierra a la Luna', 'Julio Verne', 3),
        # ('20mil Leguas de viaje submarino', 'Julio Verne', 4),
        # ('Calculo', 'Robert A. Adams', 5), ('mi libro', 'yo', 6)]
        #   la ejecucion de la busqueda devuelve una lista de tuplas, nececito los elementos ID de cada tupla
        #   este dato se encuentra en la pocicion 2 de cada una de ellas , vamos a iterarlas con un for
        cont=0
        
        list(obras_buscadas)
        for i in obras_buscadas:           
            contar_ejemplares=f"SELECT COUNT(idEjemplar) FROM ejemplar WHERE idObra = {obras_buscadas[cont][2]};"
            cantidad=(self.ejecutar_consulta(contar_ejemplares))
            list(i)
            
            cont=cont+1
            cantidad.append(cantidad)
        print(type(i))
        print(cantidad)
        return obras_buscadas
    
    
    
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
    
