import tkinter
from tkinter import ttk , Frame, Toplevel
from controladores import ObraLiteraria
from vistas.vistasMPP import VistaAgregarPersona

class MenuPersonaPrestamo:
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal
    def agrega_persona(self):
        ventana_agrega_persona=VistaAgregarPersona.VistaAgregarPersona(self.ventana_principal)
        ventana_agrega_persona.ventana_agrega_persona()
    def menu_persona_prestamo(self):
        self.controlador= ObraLiteraria.ObraLiteraria('','',0)
        menu_persn_prstm=Toplevel(self.ventana_principal)
        menu_persn_prstm.title('Menu prestamos y personas')
        menu_persn_prstm.geometry("900x300")
        
        var_busc_persn=tkinter.StringVar()
        ntry_busca_persona=ttk.Entry(menu_persn_prstm, textvariable= var_busc_persn).place(x=10, y=20)
        btn_busc_persn=ttk.Button(menu_persn_prstm, text='Buscar').place(x=150, y=20)
        
        cuadro_persona=ttk.Treeview(menu_persn_prstm, colum=('Nombre','Apellido','Curso','DNI'))
        cuadro_persona.heading('#0',text='Nombre')
        cuadro_persona.heading('#1',text='Apellido')
        cuadro_persona.heading('#2',text='Curso')
        cuadro_persona.heading('#3',text='DNI')
        cuadro_persona.column('#0', width=100)
        cuadro_persona.column('#1', width=100)
        cuadro_persona.column('#2', width=100)
        cuadro_persona.column('#3', width=100)
        cuadro_persona.place(x=10 , y=50 , width=400, height=150)
        
        btn_agrega_persona=ttk.Button(menu_persn_prstm , text='Agregar\nPersona', command=self.agrega_persona).place(x=10 , y=210)
        btn_edita_p=ttk.Button(menu_persn_prstm, text='Editar').place(x=100 , y=210)
        btn_elimina_p=ttk.Button(menu_persn_prstm , text='Eliminar').place(x=190 , y=210)

        cuadro_prestamo=ttk.Treeview(menu_persn_prstm, colum=('Inicio','Finalización','Ejemplares','DNI'))
        cuadro_prestamo.heading('#0',text='Inicio')
        cuadro_prestamo.heading('#1',text='Finalización')
        cuadro_prestamo.heading('#2',text='Ejemplares')
        cuadro_prestamo.heading('#3',text='DNI')
        cuadro_prestamo.column('#0', width=100)
        cuadro_prestamo.column('#1', width=100)
        cuadro_prestamo.column('#2', width=100)
        cuadro_prestamo.column('#3', width=100)
        cuadro_prestamo.place(x=490 , y=50 , width=400, height=150)
        
        
        btn_finaliza_prestamo=ttk.Button(menu_persn_prstm, text='Finalizar\nPrestamo').place(x=490 , y=210)
        btn_devuelve_ejemplar=ttk.Button(menu_persn_prstm, text='Devolver\nEjemplar').place(x=600, y=210)
        btn_sale=ttk.Button(menu_persn_prstm , text='Salir' ).place(x=730 , y=250, width=150)
        