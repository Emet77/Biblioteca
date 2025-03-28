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
        self.literary_work_driver=catalog_driver.catalog_driver()
        #PROBLEMA:  se tiene que guardar el ide de cada obra que seleccionemos para poder editarla.
        #crear una var para almacenarla cada vez que seleccionamos una pero no mostrar esa var en el cuadro de resultados
        def btn_search_literary_work():
            search_this= var_search_literary_work.get()
            #in_this_place=var_combobox_where_I_search.get()

            search_results=self.literary_work_driver.buscar_obra_catalogo(search_this, 'edit')
            pprint(search_results)
            eliminar = frame_books_list.get_children()
            for elemento in eliminar:
                frame_books_list.delete(elemento)
        
            search_results.reverse()
            for element in search_results:  
                frame_books_list.insert('',0,text=element[1],values=(element[2],element[3],element[4]) )



        def function_select_literary_work(s):
            function_clean_interface()
            lbl_title.configure(text='Editar Datos de Socio',bootstyle='dark')
            selected_book= frame_books_list.item(frame_books_list.selection())
            id=selected_book['text']
            title=selected_book['values'][0]
            author=selected_book['values'][1]
            editorial=selected_book['values'][2]
            ntry_title.insert( 0, string=title)
            ntry_author.insert(0,string=author)
            ntry_editorial.insert(0,string=editorial)
            print("el id de esta obra es: ", selected_book)

        def function_clean_interface():
            ntry_id.delete(0,tkinter.END)
            ntry_name.delete(0,tkinter.END)
            ntry_cellphone.delete(0,tkinter.END)
            ntry_dni.delete(0,tkinter.END)
            ntry_search_partner_dni.delete(0,tkinter.END)            


 
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

       
        var_search_literary_work=tkinter.StringVar()
        ntry_search_partner_dni=ttkbootstrap.Entry(frame_one,state='normal',textvariable=var_search_literary_work)
        ntry_search_partner_dni.grid(row=0,column=0,sticky='news',pady=3,padx=3)

        btn_search=ttkbootstrap.Button(frame_one,text='Buscar', command=btn_search_literary_work)#,command=function_btn_search
        btn_search.grid(row=0,column=1)

        frame_books_list=ttkbootstrap.Treeview(frame_one,columns=('titulo','autor'))#titulo autor editorial
        frame_books_list.grid(row=1,column=0,sticky='news',columnspan=2,pady=3,padx=3)
        frame_books_list.heading('#0',text='Titulo')
        frame_books_list.heading('#1',text='Autor')
        frame_books_list.heading('#2',text='Editorial')
        #frame_books_list.heading('#3',text='Dni')

        frame_books_list.column('#0',width=25,minwidth=25)   
        frame_books_list.column('#1',width=55,minwidth=55)    
        frame_books_list.column('#2',width=55,minwidth=55)     

        frame_books_list.bind("<Double-1>",function_select_literary_work)

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

        var_title=tkinter.StringVar()
        ntry_title=ttkbootstrap.Entry(frame_three, font='Helvetica',textvariable=var_title)
        ntry_title.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

      
        
        var_author=tkinter.StringVar()
        ntry_author=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal', textvariable=var_author)  
        ntry_author.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_editorial=tkinter.StringVar()
        ntry_editorial=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal', textvariable=var_editorial)
        ntry_editorial.grid(row=2,column=0,sticky='we',pady=3,padx=3)


#<------------------------area botones------------------------>
        frame_four=ttkbootstrap.LabelFrame(container_frame,text='Boton crear ',bootstyle='danger')
        frame_four.grid(row=2,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        frame_four.grid_columnconfigure(0,weight=1)
        

        btn_cancell=ttkbootstrap.Button(frame_four,text='Cancelar',bootstyle='info')#,command=function_clean_interface
        btn_cancell.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        btn_save_changes=ttkbootstrap.Button(frame_four,text='Guardar Cambios',bootstyle='success')#,command=function_save_changes
        btn_save_changes.grid(row=0,column=1,sticky='e',pady=3,padx=3)

       




        return container_frame        