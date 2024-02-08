import tkinter
from tkinter import ttk ,Toplevel , Entry , messagebox
from controladores import ObraLiteraria
class VistaEliminar:
    controlador_obralit=ObraLiteraria.ObraLiteraria('','',0)
    #En el constructor por defecto debemos requerir el id de la obra a eliminar
    #cuando se quiera eliminar un ejemplar en particular debemos solicitar el id de ejemplar en la ventana elimina
    #atravez de un cuadro de dialogo
    
    #distinguir dos funciones una para eliminar ejemplar y otra para eliminar obras
    def __init__(self,ventana_principal):
        self.ventana_principal = ventana_principal

    
    def ventana_elimina_obra(self,id_obra, titulo):
        self.id_obra = id_obra
        self.titulo = titulo
        def borra():
            abortar=messagebox.askquestion(title='Eliminar obra completa', message=f"¿Esta seguro que desea continuar?\n se borrara la obra '{self.titulo}'")
            if abortar=='yes':
                comprueba=self.controlador_obralit.eliminar_obra(self.id_obra)
                if(comprueba == True):
                    messagebox.showinfo(title='Información', message='¡Obra eliminada con exito!')
                elif(comprueba==False):
                    messagebox.showerror(title='Fatal Error', message='Error al conectarse a la base de datos')
 
            ventana_elimina.destroy()
            
            
        ventana_elimina=Toplevel(self.ventana_principal)
        ventana_elimina.geometry("300x200")
        
        lbl_pregunta=ttk.Label(ventana_elimina, text="¿Desea eliminar la obra completa?").pack()
        lbl_titulo=ttk.Label(ventana_elimina, text=titulo).pack()
        
        btn_elimina=ttk.Button(ventana_elimina , text='Eliminar', command=borra).pack()
        
    def ventana_elimina_ejemplar(self):
        def borra():            
            abortar=messagebox.askquestion(title='Eliminar ejemplar', message='¿Esta seguro que desea continuar?\n se borrara el ejemplar')
            if abortar=='yes':
                id_ejem= numero_ejemplar.get()
                eliminar_ejemplar=self.controlador_obralit.eliminar_ejemplar(id_ejem)
                if(eliminar_ejemplar==True):
                    messagebox.showinfo(title='Información', message='¡Ejemplar eliminado con exito!')
                elif(eliminar_ejemplar ==  False):
                    messagebox.showerror(title="Error", message="El ejemplar indicado no existe")              
            else:
                pass
            ventana_elimina.destroy()
        
        
        ventana_elimina=Toplevel(self.ventana_principal)
        ventana_elimina.geometry("300x200")
        
        lbl_pregunta=ttk.Label(ventana_elimina, text='¿Que ejemplar desea eliminar?' ).pack()
        lbl_numero=ttk.Label(ventana_elimina, text='ingrese el numero identificador').pack()
        
        numero_ejemplar=tkinter.IntVar() 
        validate_entry = lambda text: text.isdecimal()
        ntry_id=ttk.Entry(ventana_elimina , validate="key",validatecommand=(ventana_elimina.register(validate_entry), "%S") , textvariable=numero_ejemplar)
        ntry_id.pack(side=lbl_numero)
        
        btn_elimina=ttk.Button(ventana_elimina, text='Eliminar', command=borra).pack()


