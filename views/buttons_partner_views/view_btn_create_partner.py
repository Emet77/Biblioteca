import tkinter
import ttkbootstrap.localization  
from tkinter import filedialog
from PIL import Image , ImageTk 
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window
from drivers import partner_management_driver

class view_btn_create_partner():
    def __init__(self, contenedor):
        self.main_window=contenedor
        self.management_driver=partner_management_driver.partner_management_driver()
    
    def frame_create_partner(self):
        def function_clean_interface():
            pass
        def function_btn_create_partner():
            name=var_partner_name.get()
            cellphone_number=var_partner_cellphone.get()
            dni=var_partner_dni.get()
            print('esto va al controlador: ',name,' ',cellphone_number,' ',dni )

        container_frame=ttkbootstrap.LabelFrame(self.main_window,text='Contenedor de todo xd')
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_rowconfigure(2,weight=1)
        container_frame.grid_rowconfigure(3,weight=1)


        frame_cero=ttkbootstrap.LabelFrame(container_frame,text='lbl titulo',bootstyle='danger')
        frame_cero.grid(row=0,column=0,sticky='new',columnspan=3,pady=5,padx=5)
        frame_cero.grid_rowconfigure(0,weight=1)
        frame_cero.grid_columnconfigure(0,weight=1)
        
        lbl_title=ttkbootstrap.Label(frame_cero,text='Crear Socio',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n',pady=3,padx=3)

        frame_one=ttkbootstrap.LabelFrame(container_frame,text='labels ',bootstyle='danger')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5)
        frame_one.grid_rowconfigure(0,weight=1)
        frame_one.grid_rowconfigure(1,weight=1)
        frame_one.grid_rowconfigure(2,weight=1)


        lbl_name=ttkbootstrap.Label(frame_one,text='Nombre completo: ',font='Helvetica',bootstyle='dark')
        lbl_name.grid(row=0,column=0,sticky='w',pady=3,padx=3)
        
        lbl_cellphone=ttkbootstrap.Label(frame_one,text='Numero Telefonico : ',font='Helvetica',bootstyle='dark')
        lbl_cellphone.grid(row=1,column=0,sticky='w',pady=3,padx=3)
        
        lbl_dni=ttkbootstrap.Label(frame_one,text='Ingrese DNI: ',font='Helvetica',bootstyle='dark')
        lbl_dni.grid(row=2,column=0,sticky='w',pady=3,padx=3)

        frame_two=ttkbootstrap.LabelFrame(container_frame,text='Entrys ',bootstyle='danger')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_rowconfigure(1,weight=1)
        frame_two.grid_rowconfigure(2,weight=1)

        frame_two.grid_columnconfigure(0,weight=1)
        
        var_partner_name=tkinter.StringVar()
        ntry_name=ttkbootstrap.Entry(frame_two,textvariable=var_partner_name)
        ntry_name.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        # Validar que solo ingresen numeros enteros el los ntry cellphone y dni
        var_partner_cellphone=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_cellphone=ttkbootstrap.Entry(frame_two,state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_partner_cellphone)
        
        ntry_cellphone.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_partner_dni=tkinter.IntVar()
        ntry_dni=ttkbootstrap.Entry(frame_two,state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_partner_dni)
        ntry_dni.grid(row=2,column=0,sticky='we',pady=3,padx=3)

        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Boton crear ',bootstyle='danger')
        frame_three.grid(row=2,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        # frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_columnconfigure(0,weight=1)
        # frame_three.grid_columnconfigure(1,weight=1)

        btn_create_parner=ttkbootstrap.Button(frame_three,text='Crear Socio',bootstyle='success',command=function_btn_create_partner)
        btn_create_parner.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        print(frame_three.grid_size())


        # ntry_name=ttkbootstrap.Entry(frame_one)
        # ntry_name.grid(row=0,column=1,sticky='e',pady=3,padx=3)   

        # frame_2=ttkbootstrap.LabelFrame(container_frame,text='entry y label telefono',bootstyle='danger')
        # frame_2.grid(row=2,column=0,sticky='new')
        # frame_2.grid_rowconfigure(0,weight=1)
        # # frame_one.grid_columnconfigure(0,weight=1)
        # # frame_one.grid_columnconfigure(1,weight=1)

        # lbl_cellphone=ttkbootstrap.Label(frame_2,text='Numero Telefonico : ',font='Helvetica',bootstyle='dark')
        # lbl_cellphone.grid(row=0,column=0,sticky='w',pady=3,padx=3)

        # ntry_cellphone=ttkbootstrap.Entry(frame_2)
        # ntry_cellphone.grid(row=0,column=1,sticky='e',pady=3,padx=3)

        # frame_3=ttkbootstrap.LabelFrame(container_frame,text='entry y label DNI',bootstyle='danger')
        # frame_3.grid(row=3,column=0,sticky='new')
        # frame_3.grid_rowconfigure(0,weight=1)
        # frame_3.grid_columnconfigure(1,weight=1)
        # # frame_one.grid_columnconfigure(1,weight=1)

        # lbl_dni=ttkbootstrap.Label(frame_3,text='Ingrese DNI: ',font='Helvetica',bootstyle='dark')
        # lbl_dni.grid(row=0,column=0,sticky='w',pady=3,padx=3)

        # ntry_dni=ttkbootstrap.Entry(frame_3)
        # ntry_dni.grid(row=0,column=1,sticky='w',pady=3,padx=3)
        




        return container_frame