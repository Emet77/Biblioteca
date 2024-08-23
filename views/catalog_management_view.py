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

        lbl_welcome_message = ttkbootstrap.Label(catalog_magement_view_frame,text="Administracion de obras literarias", font='Helvetica')
        lbl_welcome_message.place(x=400 , y= 30)

        return catalog_magement_view_frame