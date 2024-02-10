import tkinter
from tkinter import ttk ,Toplevel , Entry , messagebox
from controladores import ObraLiteraria
class VistaAgregarPersona :
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal
    
    def ventana_agrega_persona(self):
        #self.controladorObra =ObraLiteraria.ObraLiteraria('','',0) sera un controlador de persona/prestamo
        
        ventana_agrega_persona=Toplevel(self.ventana_principal)
        ventana_agrega_persona.geometry("300x300")
        ventana_agrega_persona.title('Agregar una Persona')
        lbl_nombre = ttk.Label(ventana_agrega_persona,text="Nombre").place(x=10 , y=30, width =70 , height=20 )
        var_nombre=tkinter.StringVar()
        entry_nombre= Entry(ventana_agrega_persona,textvariable= var_nombre).place(x=90,y=30)
        
        lbl_apellido = ttk.Label(ventana_agrega_persona, text="Apellido").place(x=10, y=60  )
        var_apellido=tkinter.StringVar()
        entry_apellido= Entry(ventana_agrega_persona, textvariable=var_apellido).place(x=90, y=60)
        
        lbl_dni= ttk.Label(ventana_agrega_persona, text="DNI").place(x=10, y=90, width=80, height=40)
        var_dni=tkinter.IntVar() 
        validate_entry = lambda text: text.isdecimal()
        entry_dni=ttk.Entry(ventana_agrega_persona , validate="key",validatecommand=(ventana_agrega_persona.register(validate_entry), "%S") , textvariable=var_dni)
        entry_dni.place(x=90 , y=90)     
    
        lbl_alu_prof= ttk.Label(ventana_agrega_persona, text="Alumno/\nProfesor").place(x=10 , y=130)
        var_alu_prof=tkinter.StringVar()
        cbx_alu_prof=ttk.Combobox(ventana_agrega_persona,state="readonly",values=['1ero','2do','3ero' ,'4to','5to','Profesor'], textvariable=var_alu_prof)
        cbx_alu_prof.place(x=90, y=130 , width=40)
        
        lbl_alu_div= ttk.Label(ventana_agrega_persona, text="División").place(x=130 , y=130)
        var_alu_div=tkinter.StringVar()
        cbx_alu_div=ttk.Combobox(ventana_agrega_persona,state="readonly",values=['1era','2da','3era' ,'4ta','5ta'], textvariable=var_alu_div)
        cbx_alu_div.place(x=180, y=130 , width=40)
        
        btnGuardar=ttk.Button(ventana_agrega_persona, text="Guardar"  ).place(x=30 , y=170 , width=80 , height=60)
        btnSalir=ttk.Button(ventana_agrega_persona, text="Salir" , command= ventana_agrega_persona.destroy).place(x=130 , y=170 , width=80 , height=60)      
        
        