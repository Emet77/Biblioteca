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
        self.partner_management_driver=partner_management_driver.partner_management_driver()
    
    def frame_create_partner(self):
        def function_clean_interface():
            ntry_name.delete(0,tkinter.END)
            ntry_cellphone.delete(0,tkinter.END)
            ntry_dni.delete(0,tkinter.END)
            
        def function_btn_create_partner():
            try:
                name=var_partner_name.get()
                cellphone_number=var_partner_cellphone.get()
                cant_number=len(str(cellphone_number))
                dni=var_partner_dni.get()
                cant_dni=len(str(dni))
                if(name==''):
                    lbl_title.configure(text='faltan nombre',bootstyle='danger')
                elif(cant_number<10):
                    lbl_title.configure(text='el telefono esta icompleto',bootstyle='danger')
                elif( cant_dni<8):
                    lbl_title.configure(text='el dni esta incompleto',bootstyle='danger')

                elif(name!='' and cellphone_number>=0 and dni>=0):
                    lbl_title.configure(text='¡Socio Agregado Con Exito!',bootstyle='success')
                    self.partner_management_driver.crear_socio(name,cellphone_number,dni)
            except:
                lbl_title.configure(text='Faltan Datos',bootstyle='danger')
            

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
        ntry_name=ttkbootstrap.Entry(frame_two,font='Helvetica',textvariable=var_partner_name)
        ntry_name.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        # Validar que solo ingresen numeros enteros el los ntry cellphone y dni
        var_partner_cellphone=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_cellphone=ttkbootstrap.Entry(frame_two,font='Helvetica',state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_partner_cellphone)
        ntry_cellphone.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_partner_dni=tkinter.IntVar()
        ntry_dni=ttkbootstrap.Entry(frame_two,font='Helvetica',state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_partner_dni)
        ntry_dni.grid(row=2,column=0,sticky='we',pady=3,padx=3)

        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Boton crear ',bootstyle='danger')
        frame_three.grid(row=2,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        # frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_columnconfigure(0,weight=1)
        # frame_three.grid_columnconfigure(1,weight=1)
        
        btn_cancell=ttkbootstrap.Button(frame_three,text='Cancelar',bootstyle='info',command=function_clean_interface)
        btn_cancell.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        btn_create_parner=ttkbootstrap.Button(frame_three,text='Crear Socio',bootstyle='success',command=function_btn_create_partner)
        btn_create_parner.grid(row=0,column=1,sticky='e',pady=3,padx=3)

        # print(frame_three.grid_size())

        return container_frame