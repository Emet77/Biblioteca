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
        self.book_driver=catalog_driver.catalog_driver()
        def function_search_book():
            # tomamos el valor como string y lo casteamos a int
            book_number=var_ntry_book_number.get()
            book_number=int(book_number)
            info=self.book_driver.buscar_info_ejemplar(book_number)
            label_result_author.configure(text=info[0])
            label_result_title.configure(text=info[1])
            label_result_editorial.configure(text=info[2])
            


        
        # CONTINUAR:
        # el numero ingresado se cambia de base cuando se ingresa un 0 delante(listo)   
        # arreglar cuando el controlador no encuentre informacion que el no sigua con los demas pasos()
        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        
        container_frame.grid_rowconfigure(0,weight=1)
        container_frame.grid_rowconfigure(1,weight=1)
        container_frame.grid_rowconfigure(3,weight=1)
        container_frame.grid_rowconfigure(4,weight=1)





        frame_title=ttkbootstrap.LabelFrame(container_frame,text='',bootstyle='info')
        frame_title.grid(row=0,column=0,sticky='news',pady=5,padx=5)
        frame_title.grid_columnconfigure(0,weight=1)
        lbl_title=ttkbootstrap.Label(frame_title,text='Eliminar Ejemplar',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)
        
        frame_warning=ttkbootstrap.LabelFrame(container_frame, text='aviso de borrar libro',bootstyle='dark')
        frame_warning.grid(row=1,column=0,sticky='news',columnspan=1,pady=5,padx=5)
        frame_warning.grid_columnconfigure(0,weight=1)
        text_warning=f"""Recuerde: se debe eliminar un ejemplar solamente cuando este ya no este apto para seguir siendo usado como tal
        (Faltan hojas, daños por agua,etc)"""
        label_warning=ttkbootstrap.Label(frame_warning,text=text_warning,bootstyle='dark',font='Helvetica',anchor='center')
        label_warning.grid(row=0,column=0,sticky='n', padx=3,pady=3)

        #<------------------frame to show information about a book xD ----------------->

        frame_search_book=ttkbootstrap.LabelFrame(container_frame,text='buscar y datos libro',bootstyle='info')
        frame_search_book.grid(row=2,column=0,sticky='news',padx=5,pady=5)

        frame_search_book.grid_columnconfigure(0,weight=1)
        frame_search_book.grid_columnconfigure(1,weight=1)
        frame_search_book.grid_columnconfigure(2,weight=1)
        frame_search_book.grid_columnconfigure(3,weight=1)

        frame_search_book.grid_rowconfigure(0,weight=1)
        frame_search_book.grid_rowconfigure(1,weight=1)
        frame_search_book.grid_rowconfigure(2,weight=1)

        label_number=ttkbootstrap.Label(frame_search_book,text='Numero de ejemplar: ',font='Helvetica')
        label_number.grid(column=0,row=0)

        label_author=ttkbootstrap.Label(frame_search_book,text='Autor: ',font='Helvetica')
        label_author.grid(column=0,row=1)

        label_book_title=ttkbootstrap.Label(frame_search_book,text='Titulo: ',font='Helvetica')
        label_book_title.grid(column=0,row=2)

        validate_entry = lambda text: text.isdecimal()
        var_ntry_book_number=tkinter.StringVar() #esto era un intVar..cuidao
        entry_book_number=ttkbootstrap.Entry(frame_search_book,font='Helvetica',state='normal',validate="key",validatecommand=(frame_search_book.register(validate_entry), "%S"), textvariable=var_ntry_book_number)
        entry_book_number.grid(row=0,column=1,sticky='we',pady=3,padx=3)
        entry_book_number.delete(0,END)

        label_result_author=ttkbootstrap.Label(frame_search_book,text='resultado autor',font='Helvetica')
        label_result_author.grid(column=1,row=1)

        label_result_title=ttkbootstrap.Label(frame_search_book,text='resultado titulo',font='Helvetica')
        label_result_title.grid(column=1,row=2)

        button_search=ttkbootstrap.Button(frame_search_book,text='Buscar',bootstyle='danger',command=function_search_book)
        button_search.grid(column=2, row=0)

        label_editorial=ttkbootstrap.Label(frame_search_book,text='Editorial: ',font='Helvetica')
        label_editorial.grid(column=2,row=1)

        label_result_editorial=ttkbootstrap.Label(frame_search_book,text='resultado editorial',font='Helvetica')
        label_result_editorial.grid(column=3,row=1)


        frame_btn_delete=ttkbootstrap.Labelframe(container_frame,text='boton! eliminar',bootstyle='danger')
        frame_btn_delete.grid(column=0,row=3,sticky='news',padx=5,pady=5)#,columnspan=4
        #frame_search_book.grid(row=2,column=0,sticky=EW,padx=5,pady=5)

        button_delete=ttkbootstrap.Button(frame_btn_delete,text='¿Eliminar?',bootstyle='danger')
        button_delete.grid(column=0, row=0,sticky='n',padx=5,pady=5)
        print('filas y column en delete',frame_btn_delete.grid_size())

        return container_frame