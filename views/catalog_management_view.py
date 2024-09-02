import tkinter  
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window

class catalog_magement_view():
    def __init__(self, contenedor) -> None:
        self.main_window=contenedor
    
    def catalog_management_view(self ):
        big_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth' )
        big_frame.configure(width="990",height="560")

        litle_frame_options=ttkbootstrap.LabelFrame(big_frame, text='Frame Chiquito' , width=150, height=560)
        litle_frame_options.place(x=0 , y=0)

        return big_frame