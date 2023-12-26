import tkinter
from tkinter import ttk ,Toplevel , Entry , messagebox
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
            mensaje = self.controladorObra.crear_obra(titulo,autor,cantida,importancia) 
            if(mensaje == True):
                messagebox.showinfo('informacion', 'Una nueva obra fue agregada')
                ventana_agrega_obra.destroy()
            else:
                messagebox.showerror('Error','Algo salio mal :c \n contacte con el administrador ')
                ventana_agrega_obra.destroy()
                      
        
       
            

        ventana_agrega_obra=Toplevel(self.ventana_principal)
        ventana_agrega_obra.geometry("250x250")
        ventana_agrega_obra.title('Agregar una obra literaria')
        lblTitulo = ttk.Label(ventana_agrega_obra,text="Titulo").place(x=10 , y=30, width =35 , height=20 )
        varTitulo=tkinter.StringVar()
        entryTitulo= Entry(ventana_agrega_obra,textvariable= varTitulo).place(x=55,y=30)
        
        lblAutor = ttk.Label(ventana_agrega_obra, text="Autor").place(x=10, y=60)
        varAutor=tkinter.StringVar()
        entryAutor= Entry(ventana_agrega_obra, textvariable=varAutor).place(x=55, y=60)
        
        lblCantidad= ttk.Label(ventana_agrega_obra, text="Cantidad de \n ejemplares").place(x=10, y=90, width=80, height=40)
        varCantidad=tkinter.IntVar() 
        validate_entry = lambda text: text.isdecimal()
        entryCantidad=ttk.Entry(ventana_agrega_obra , validate="key",validatecommand=(ventana_agrega_obra.register(validate_entry), "%S") , textvariable=varCantidad)
        entryCantidad.place(x=100 , y=90, width=40)     
    
        lblImportancia= ttk.Label(ventana_agrega_obra, text="¿Es una obra Importante?").place(x=10 , y=130)
        varImportacia=tkinter.StringVar()
        entryImportancia=ttk.Combobox(ventana_agrega_obra,state="readonly",values=["SI","NO"], textvariable=varImportacia)
        entryImportancia.place(x=150, y=130 , width=40)
        
        btnGuardar=ttk.Button(ventana_agrega_obra, text="Guardar" , command=guardar ).place(x=30 , y=170 , width=80 , height=60)
        btnSalir=ttk.Button(ventana_agrega_obra, text="Salir" , command= ventana_agrega_obra.destroy).place(x=130 , y=170 , width=80 , height=60)            
           
        
        
        
    def ventana_agrega_ejemplar(self):
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