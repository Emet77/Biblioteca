import tkinter
from tkinter import ttk ,Toplevel , Entry
from controladores import ObraLiteraria

class VistaAgregar:
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal

    def ventana_agrega_obra(self):
        self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        
        def guardar():
            titulo=varTitulo.get()
            autor=varAutor.get()
            cantida=varCantidad.get()
            importancia=varImportacia.get()
            self.controladorObra.crear_obra(titulo,autor,cantida,importancia) 
        
       
            

        ventana_agrega_obra=Toplevel(self.ventana_principal)
        ventana_agrega_obra.geometry("250x250")
        ventana_agrega_obra.title('Agregar una obra literaria')
        lblTitulo = ttk.Label(ventana_agrega_obra,text="Titulo").place(x=10 , y=30, width =35 , height=20 )
        varTitulo=tkinter.StringVar()
        entryTitulo= Entry(ventana_agrega_obra,textvariable= varTitulo).place(x=55,y=30)
        
        lblAutor = ttk.Label(ventana_agrega_obra, text="Autor").place(x=10, y=60)
        varAutor=tkinter.StringVar()
        entryAutor= Entry(ventana_agrega_obra, textvariable=varAutor).place(x=55, y=60)
        
        lblCantidad= ttk.Label(ventana_agrega_obra, text="Cantida").place(x=10, y=90, width=50, height=20)
        varCantidad=tkinter.StringVar() 
        entryCantidad= Entry(ventana_agrega_obra, textvariable= varCantidad).place(x=70 , y=90, width=40)
        #agregar una validacion para que solo sean numeros los que se ingresen en el campo entryCantidad
        lblImportancia= ttk.Label(ventana_agrega_obra, text="¿Es una obra Importante?").place(x=10 , y=120)
        varImportacia=tkinter.StringVar()
        entryImportancia=ttk.Combobox(ventana_agrega_obra,state="readonly",values=["SI","NO"], textvariable=varImportacia)
        entryImportancia.place(x=150, y=120 , width=40)
        
        btnGuardar=ttk.Button(ventana_agrega_obra, text="Guardar" , command=guardar ).place(x=30 , y=170 , width=80 , height=60)
        btnSalir=ttk.Button(ventana_agrega_obra, text="Salir" , command= ventana_agrega_obra.destroy).place(x=130 , y=170 , width=80 , height=60)        
    
    def guardar(self):
        pass
        
        
        
        
        
        
        
    def ventana_agrega_ejemplar(self):
        self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        ventana_agrega_ejemplar=Toplevel(self.ventana_principal)
        ventana_agrega_ejemplar.geometry("400x300")
        ventana_agrega_ejemplar.title("Agregar 'ejemplares' a una obra literaria")        

    def ventana_edita_obra(self):
        self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        ventana_agrega_obra=Toplevel(self.ventana_principal)
        ventana_agrega_obra.geometry("400x300")
        ventana_agrega_obra.title('Agregar una obra literaria')
        lblTitulo = ttk.Label(ventana_agrega_obra,text="Titulo")
        lblTitulo.place(x=10 , y=30, width =35 , height=20 )
        prueba=("fasaa")
        varTitulo=tkinter.StringVar(value=prueba) #Este value y los demas deben ser reemplazados con un valor enviado
                                                #la ventana principal 
        entryTitulo= Entry(ventana_agrega_obra,textvariable= varTitulo).place(x=55,y=30 )        