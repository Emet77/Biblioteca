import os
import tkinter
from tkinter import messagebox
from ttkbootstrap.dialogs import MessageDialog , Messagebox
import ttkbootstrap.localization  
from tkinter import filedialog
from PIL import Image , ImageTk 
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
from drivers import catalog_driver
import ttkbootstrap.window



class view_btn_delete_one_book():
    def __init__(self, contenedor):
        self.main_window=contenedor
        

    def frame_delete_one_book(self):
        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)

        frame_title=ttkbootstrap.LabelFrame(container_frame,text='',bootstyle='info')
        frame_title.grid(row=0,column=0,sticky='ew',columnspan=3,pady=5,padx=5)
        frame_title.grid_columnconfigure(0,weight=1)
        lbl_title=ttkbootstrap.Label(frame_title,text='Eliminar Ejemplar',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)
        
        frame_warning=ttkbootstrap.LabelFrame(container_frame, text='aviso de borrar libro',bootstyle='dark')
        frame_warning.grid(row=0,column=0,sticky='ew',columnspan=3,pady=5,padx=5)
        frame_warning.grid_columnconfigure(0,weight=1)
        text_warning=f"""Recuerde: se debe eliminar un ejemplar solamente cuando este ya no este apto para seguir siendo usado como tal
        (Faltan hojas, daños por agua,etc)"""
        label_warning=ttkbootstrap.Label(frame_warning,text=text_warning,bootstyle='dark')
        label_warning.grid(row=0,column=0,sticky='n', padx=3,pady=3)


        return container_frame