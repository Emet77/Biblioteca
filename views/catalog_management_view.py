import tkinter  
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window

class catalog_magement_view():
    def __init__(self, contenedor) -> None:
        self.main_window=contenedor
    
    def catalog_management_view(self):
        catalog_magement_view_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth')
        catalog_magement_view_frame.configure(width="990",height="560")

        lbl_welcome_message = ttkbootstrap.Label(catalog_magement_view_frame,text="Administracion de obras literarias\n AÚN EN CONSTRUCCIÓN", font='Helvetica')
        lbl_welcome_message.place(x=400 , y= 30)

        frame_to_show_results=ttk.Treeview(catalog_magement_view_frame,columns=('id','titulo','editorial','cantidad'))
        frame_to_show_results.heading('#0',text='id')
        frame_to_show_results.heading('#1',text='Titulo')
        frame_to_show_results.heading('#2',text='Editorial')
        frame_to_show_results.heading('#3',text='Cantidad')

        frame_to_show_results.column('#0',width=80, minwidth=80) #Arreglar: las etiquetas del cuadro no deben poder achicarse
        frame_to_show_results.column('#1',width=120, minwidth=120)
        frame_to_show_results.column('#2',width=120, minwidth=120)
        frame_to_show_results.column('#3',width=80, minwidth=80)
        frame_to_show_results.place(x=10 , y=120 , width='400', height='300')
        

        return catalog_magement_view_frame