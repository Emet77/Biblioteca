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

class view_btn_edit_literary_work():
    def __init__(self,contenedor):
        self.main_window=contenedor
    

    def view_btn_edit_literary_work_frame(self):
        container_frame=ttkbootstrap.LabelFrame(self.main_window,text='datos a editar obra')
        container_frame.grid(row=0,column=0)

        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_columnconfigure(2,weight=1)
        # container_frame.grid_rowconfigure(0,weight=1)
        # container_frame.grid_rowconfigure(1,weight=1)
        container_frame.grid_rowconfigure(2,weight=1)

        frame_cero=ttkbootstrap.LabelFrame(container_frame,text='frame_titulo',bootstyle='info')
        frame_cero.grid(row=0,column=0,sticky='ew',columnspan=3,pady=5,padx=5)
        frame_cero.grid_columnconfigure(0,weight=1)

        lbl_title=ttkbootstrap.Label(frame_cero,text='Editar Datos de Obra',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)

        frame_one=ttkbootstrap.LabelFrame(container_frame,text='Buscar por titulo/autor',bootstyle='info')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5)
        frame_one.grid_columnconfigure(0,weight=1)
        frame_one.grid_columnconfigure(1,weight=1)
        frame_one.grid_rowconfigure(0,weight=1)

       
        var_partner_dni_search=tkinter.StringVar()
        ntry_search_partner_dni=ttkbootstrap.Entry(frame_one,state='normal',textvariable=var_partner_dni_search)
        ntry_search_partner_dni.grid(row=0,column=0,sticky='news',pady=3,padx=3)

        btn_search=ttkbootstrap.Button(frame_one,text='Buscar')#,command=function_btn_search
        btn_search.grid(row=0,column=1)

        frame_partner_list=ttkbootstrap.Treeview(frame_one,columns=('titulo','autor'))#titulo autor editorial
        frame_partner_list.grid(row=1,column=0,sticky='news',columnspan=2,pady=3,padx=3)
        frame_partner_list.heading('#0',text='Titulo')
        frame_partner_list.heading('#1',text='Autor')
        frame_partner_list.heading('#2',text='Editorial')
        #frame_partner_list.heading('#3',text='Dni')

        frame_partner_list.column('#0',width=25,minwidth=25)   
        frame_partner_list.column('#1',width=55,minwidth=55)    
        frame_partner_list.column('#2',width=55,minwidth=55)    
        #frame_partner_list.column('#3',width=55,minwidth=55)   

        #frame_partner_list.bind("<Double-1>",function_select_partner)

        frame_two=ttkbootstrap.LabelFrame(container_frame,text='frame Labels',bootstyle='info')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5)

        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_rowconfigure(1,weight=1)
        frame_two.grid_rowconfigure(2,weight=1)

        lbl_name=ttkbootstrap.Label(frame_two,text='Titulo',font='Helvetica',bootstyle='dark')
        lbl_name.grid(row=0,column=0,sticky='w',pady=3,padx=3)

        lbl_cellphone=ttkbootstrap.Label(frame_two,text='Autor',font='Helvetica',bootstyle='dark')
        lbl_cellphone.grid(row=1,column=0,sticky='w',pady=3,padx=3)

        lbl_dni=ttkbootstrap.Label(frame_two,text='Editorial',font='Helvetica',bootstyle='dark')
        lbl_dni.grid(row=2,column=0,sticky='w',pady=3,padx=3)
#<------------------------configurar los entrys para que acepten datos de tipo string------------------------>

        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Entrys ',bootstyle='danger')
        frame_three.grid(row=1,column=2,sticky='news',pady=5,padx=5)
        frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_rowconfigure(1,weight=1)
        frame_three.grid_rowconfigure(2,weight=1)

        frame_three.grid_columnconfigure(0,weight=1)

        var_partner_id=tkinter.IntVar()
        ntry_id=ttkbootstrap.Entry(frame_three,textvariable=var_partner_id)#esta variable se coloca en el frame pero no se muestra 

        var_partner_name=tkinter.StringVar()
        ntry_name=ttkbootstrap.Entry(frame_three, font='Helvetica',textvariable=var_partner_name)
        ntry_name.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        # Validar que solo ingresen numeros enteros el los ntry cellphone y dni
        validate_entry = lambda text: text.isdecimal()
        var_partner_cellphone=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_cellphone=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal',validate="key",validatecommand=(frame_three.register(validate_entry), "%S"), textvariable=var_partner_cellphone)  
        ntry_cellphone.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_partner_dni=tkinter.IntVar()
        ntry_dni=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal',validate="key",validatecommand=(frame_three.register(validate_entry), "%S"), textvariable=var_partner_dni)
        ntry_dni.grid(row=2,column=0,sticky='we',pady=3,padx=3)


#<------------------------area botones------------------------>
        frame_four=ttkbootstrap.LabelFrame(container_frame,text='Boton crear ',bootstyle='danger')
        frame_four.grid(row=2,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        frame_four.grid_columnconfigure(0,weight=1)
        

        btn_cancell=ttkbootstrap.Button(frame_four,text='Cancelar',bootstyle='info')#,command=function_clean_interface
        btn_cancell.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        btn_save_changes=ttkbootstrap.Button(frame_four,text='Guardar Cambios',bootstyle='success')#,command=function_save_changes
        btn_save_changes.grid(row=0,column=1,sticky='e',pady=3,padx=3)

       




        return container_frame        