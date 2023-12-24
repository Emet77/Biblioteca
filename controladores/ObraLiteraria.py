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
        consulta=f"SELECT obraliteraria.titulo , obraliteraria.autor, obraliteraria.cantidaEjemplares, obraliteraria.idObra FROM obraliteraria  WHERE obraLiteraria.autor LIKE '%{self.criterio}%' OR obraLiteraria.titulo LIKE '%{self.criterio}%';"
        #consulta= f"SELECT * FROM obraliteraria WHERE obraLiteraria.autor LIKE '%{self.criterio}%';"
        resultado=self.ejecutar_consulta(consulta)
        return resultado
    def eliminar_obra(self):
        pass
    
    def modificar_obra(self):
        pass
    
    def crear_obra(self, titulo, autor, cantidad, importancia):
        print("Desde el controlador de obra literaria: ", titulo, autor, cantidad, importancia)