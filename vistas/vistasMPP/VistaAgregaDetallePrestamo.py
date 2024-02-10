import tkinter
from tkinter import ttk ,Toplevel , Entry , messagebox
from controladores import ObraLiteraria
class VistaAgregaDetallePrestamo:
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal
    
    def ventana_agrega_detalle(self,titulo,cant_max):
        ventana_agrega_detalle=Toplevel(self.ventana_principal)
        ventana_agrega_detalle.title('Agregar obra al prestamo')
        ventana_agrega_detalle.geometry("250x250")
        
        lbl_pregunta=ttk.Label(ventana_agrega_detalle, text=f'¿Cuantos ejemplares de \nla obra {titulo} desea agregar?' ).place(x=50,y=20)
        lbl_cant_disp=ttk.Label(ventana_agrega_detalle, text=f'Cantidad disponible: {cant_max}').place(x=10 , y= 60)
        var_cant=tkinter.IntVar()
        entry_cant=ttk.Entry(ventana_agrega_detalle, textvariable=var_cant).place(x=40, y=90)
        
        btn_agrega=ttk.Button(ventana_agrega_detalle, text='Agregar').place(x=40 , y=130)
        btn_cancela=ttk.Button(ventana_agrega_detalle, text='Cancelar', command=ventana_agrega_detalle.destroy).place(x=120, y=130)