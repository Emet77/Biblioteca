import tkinter
from tkinter import ttk , Frame, Toplevel
from vistas import MenuObraEjemplar
from controladores import ObraLiteraria
class MenuPrincipal():
    

    def menu_obra_ejemplar(self):
        menu_obr_ejm= MenuObraEjemplar.MenuObraEjemplar(self.ventana_principal)
        menu_obr_ejm.menu_obr_ejm()
    def ventana_principal(self):
        self.ventana_principal=tkinter.Tk()
        self.ventana_principal.title('Biblioteca IES-9012')
        self.ventana_principal.geometry("1000x600")#
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
        scrollbar = ttk.Scrollbar(self.ventana_principal, orient=tkinter.VERTICAL, command=self.cuadro_resultados.yview).place(x=310 , y=40 ,height="230")
        
        boton_obras_ejemplares=ttk.Button(self.ventana_principal, text='Menu de obras Y ejemplares ', command=self.menu_obra_ejemplar).place(x=10, y=450)
    
         
        
        
        
        
        
        self.ventana_principal.mainloop()
        
    