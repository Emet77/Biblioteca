import tkinter
from tkinter import ttk ,Toplevel , Entry
from controladores import ObraLiteraria

class VistaAgregar:
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal
    def ventana_agrega_obra(self):
        self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        ventana_agrega_obra=Toplevel(self.ventana_principal)
        ventana_agrega_obra.geometry("400x300")
        ventana_agrega_obra.title('Agregar una obra literaria')
        lblTitulo = ttk.Label(ventana_agrega_obra,text="Titulo")
        lblTitulo.place(x=10 , y=30, width =35 , height=20 )
        varTitulo=tkinter.StringVar()
        entryTitulo= Entry(ventana_agrega_obra,textvariable= varTitulo).place(x=55,y=30 )
        
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