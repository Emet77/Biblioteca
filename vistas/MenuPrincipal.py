import tkinter
from tkinter import ttk , Frame, Toplevel
from vistas import VistaAgregar, VistaEliminar
class MenuPrincipal():
    
    def __init__(self , controlador) :
        self.controlador  = controlador
    
    def buscar(self):
        eliminar =self.cuadro_resultados.get_children()
        for elemento in eliminar:
            self.cuadro_resultados.delete(elemento)
        criterio = self.var_buscar.get()
        resultado = self.controlador.buscar_obra(criterio)
        
        for elemento in resultado:  
            self.cuadro_resultados.insert('',0,text=elemento[0],values=(elemento[1],elemento[3],elemento[2]) )
     
    def agregar(self):
        ventana_agregar= VistaAgregar.VistaAgregar(self.ventana_principal)
        comprueba = self.cuadro_resultados.item(self.cuadro_resultados.selection())
        if(comprueba['text'] == ''):
            ventana_agregar.ventana_agrega_obra()
            
        else:
            ventana_agregar.ventana_agrega_ejemplar(comprueba['text'],comprueba['values'][0],comprueba['values'][1],comprueba['values'][2])
        self.buscar() 
    def elimina(self):
        vista_elimina = VistaEliminar.VistaEliminar(self.ventana_principal)
        comprueba = self.cuadro_resultados.item(self.cuadro_resultados.selection())
        if (comprueba['text'] == ''):
            vista_elimina.ventana_elimina_ejemplar()
            self.buscar() 
        else:  
            id_obra= self.cuadro_resultados.item(self.cuadro_resultados.selection())['values'][2]  
            titulo=self.cuadro_resultados.item(self.cuadro_resultados.selection())['text']
            vista_elimina.ventana_elimina_obra(id_obra , titulo)
            self.buscar()           
        
        
    def ventana_principal(self):
        self.ventana_principal=tkinter.Tk()
        self.ventana_principal.title('Biblioteca IES-9012')
        self.ventana_principal.geometry("800x600")
        
        self.var_buscar=tkinter.StringVar()
        self.entry_buscar=ttk.Entry(self.ventana_principal , textvariable=self.var_buscar ).place(x=10 , y=10 , width = 200 , height =30)
        self.btn_buscar=ttk.Button(self.ventana_principal,text='Buscar', command=self.buscar).place(x=220, y=10)
        
        
        self.cuadro_resultados= ttk.Treeview(self.ventana_principal , columns=('Obra','Autor','Cantidad','Codigo'))
        self.cuadro_resultados.heading('#0', text='Obra')
        self.cuadro_resultados.heading('#1', text='Autor')
        self.cuadro_resultados.heading('#2', text='Cantidad')
        self.cuadro_resultados.heading('#3', text='Codigo')
        self.cuadro_resultados.place(x=10 ,y=50 ,width = 600 , height =300)
        scrollbar = ttk.Scrollbar(self.ventana_principal, orient=tkinter.VERTICAL, command=self.cuadro_resultados.yview).place(x=615 , y=40 ,height="240")
        
        boton_agregar=ttk.Button(self.ventana_principal, text='Agregar', command=self.agregar).place(x=700, y=50)
        
         
       
    
        boton_eliminar=ttk.Button(self.ventana_principal, text='Eliminar',  command=self.elimina)
        boton_eliminar.place(x=700, y=100)
        self.ventana_principal.mainloop()
        
    