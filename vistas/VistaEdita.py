import tkinter
from tkinter import ttk ,Toplevel , Entry , messagebox
from controladores import ObraLiteraria

class VistaEdita:
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal
 
    def ventana_edita_obra(self,titulo, autor,id_obra):
        self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        def guarda():
            titulo=titulo_edit.get()
            autor=autor_edit.get()
            tiene_titulo=len(titulo)- titulo.count(' ')
            
            if(tiene_titulo > 0):
                confirma=self.controladorObra.modificar_obra(titulo.upper(), autor.upper(), id_obra)
                if(confirma == True):
                    messagebox.showinfo('Informacion', '¡Obra editada exitosamente!')
                    ventana_edita_obra.destroy()
                else:
                    messagebox.showerror('Error','Problema con la base de datos \n intente nuevamente o contacte al administrador')
                    ventana_edita_obra.destroy()
            elif(tiene_titulo<=0):
                messagebox.showwarning(title="Información", message="El campo 'Titulo' debe estar lleno :-]")           
                ventana_edita_obra.destroy()
        
        
        
        
        
        ventana_edita_obra=Toplevel(self.ventana_principal)
        ventana_edita_obra.geometry("300x200")
        
        lbl_encabezado=ttk.Label(ventana_edita_obra, text="Edite los datos de la obra seleccionada")
        lbl_encabezado.place_configure(x=40 , y=10)
        
        
        titulo_edit=tkinter.StringVar()
        titulo_edit.set(titulo)
        lbl_titulo=tkinter.Label(ventana_edita_obra, text="Titulo: ").place(x=10, y=30)
        ntry_titulo=Entry(ventana_edita_obra , textvariable=titulo_edit)
        ntry_titulo.place_configure(x=60, y=30 , width=200) 
        
        autor_edit=tkinter.StringVar()
        autor_edit.set(autor)
        
        lbl_autor=tkinter.Label(ventana_edita_obra, text="Autor: ").place(x=10, y=60)
        ntry_autor=Entry(ventana_edita_obra , textvariable=autor_edit)
        ntry_autor.place_configure(x=60, y=60 , width=200) 
        
        btn_guardar=ttk.Button(ventana_edita_obra, text='Guardar', command= guarda).place(x=50, y=100)
        
        btn_salir=ttk.Button(ventana_edita_obra, text="Salir", command=ventana_edita_obra.destroy).place(x=150, y=100)