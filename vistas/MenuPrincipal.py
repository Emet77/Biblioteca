import tkinter
from tkinter import ttk 
from vistas.MenuPersonaPrestamo import MenuPersonaPrestamo
from vistas import MenuObraEjemplar , MenuPersonaPrestamo
from controladores import ObraLiteraria
class MenuPrincipal():
    

    def menu_obra_ejemplar(self):
        menu_obr_ejm= MenuObraEjemplar.MenuObraEjemplar(self.ventana_principal)
        
        menu_obr_ejm.menu_obr_ejm()
    def menu_persona_prestamo(self):
        menu_persn_prstm=MenuPersonaPrestamo.MenuPersonaPrestamo(self.ventana_principal)
        menu_persn_prstm.menu_persona_prestamo()
    def ventana_principal(self):
        self.ventana_principal=tkinter.Tk()
        self.ventana_principal.title('Biblioteca IES-9012')
        self.ventana_principal.geometry("1000x500")#
        self.controlador= ObraLiteraria.ObraLiteraria('','',0)
        
        self.var_buscar=tkinter.StringVar()
        self.entry_buscar=ttk.Entry(self.ventana_principal , textvariable=self.var_buscar ).place(x=10 , y=10 , width = 200 , height =30)
        self.btn_buscar=ttk.Button(self.ventana_principal,text='Buscar').place(x=220, y=10)
        
        
        self.cuadro_resultados= ttk.Treeview(self.ventana_principal , columns=('Obra','Autor','Cantidad','Codigo') )
        self.cuadro_resultados.heading('#0', text='Obra')
        self.cuadro_resultados.heading('#1', text='Autor')
        self.cuadro_resultados.heading('#2', text='Cantidad')
        self.cuadro_resultados.heading('#3', text='Codigo')
        self.cuadro_resultados.column("#0",width=100) 
        self.cuadro_resultados.column("#1",width=100)
        self.cuadro_resultados.column("#2",width=100)
        self.cuadro_resultados.column("#3",width=70)
        self.cuadro_resultados.place(x=10 ,y=50 ,width = 300 , height =200)
        scrollbar = ttk.Scrollbar(self.ventana_principal, orient=tkinter.VERTICAL, command=self.cuadro_resultados.yview).place(x=310 , y=50 ,height="200")
        
        boton_obras_ejemplares=ttk.Button(self.ventana_principal, text='Menu de obras   \nY\n ejemplares ', command=self.menu_obra_ejemplar).place(x=10, y=260)
        boton_personas_prestamos=ttk.Button(self.ventana_principal, text='Menu de personas   \ny\n prestamos', command=self.menu_persona_prestamo).place(x=200 , y=260)
        
         #\n
        btn_agregar_prestam=ttk.Button(self.ventana_principal, text='Agregar').place(x=340, y=120)
        btn_reinicia=ttk.Button(self.ventana_principal, text='Empezar\nNuevamente').place(x=340, y=160)
        
        self.cuadro_obras_presta=ttk.Treeview(self.ventana_principal, columns=('Titulo','Cantidad'))
        self.cuadro_obras_presta.heading('#0', text='Titulo')
        self.cuadro_obras_presta.heading('#1', text='Cantidad')
        self.cuadro_obras_presta.column('#0',width=100)
        self.cuadro_obras_presta.column('#1',width=100)
        self.cuadro_obras_presta.place(x=450 , y=50, width=200 , height =200)
        
        
        var_prestatario=tkinter.StringVar()
        ntry_prestatario=ttk.Entry(self.ventana_principal, textvariable=var_prestatario).place(x=670 , y=50 , width = 200 , height =30)
        btn_buscar_prestatario=ttk.Button(self.ventana_principal,text='Buscar prestatario').place(x=880 , y=50)
        
        self.cuadro_prestatarios=ttk.Treeview(self.ventana_principal, columns=('Nombre','Apellido','Curso','DNI'))
        self.cuadro_prestatarios.heading('#0', text='Nombre')
        self.cuadro_prestatarios.heading('#1', text='Apellido')
        self.cuadro_prestatarios.heading('#2', text='Curso')
        self.cuadro_prestatarios.heading('#3', text='DNI')
        self.cuadro_prestatarios.column('#0', width=100)       
        self.cuadro_prestatarios.column('#1', width=100)       
        self.cuadro_prestatarios.column('#2', width=100)       
        self.cuadro_prestatarios.column('#3', width=100)
        self.cuadro_prestatarios.place(x=670, y=90, width = 300 , height =160)
        
        btn_agrega_persona=ttk.Button(self.ventana_principal, text='Agregar Persona').place(x=670,y=260)
        btn_termina_prestamo=ttk.Button(self.ventana_principal,text='Prestar').place(x=895, y=260)
        
         
        
        
        self.ventana_principal.mainloop()
        
    