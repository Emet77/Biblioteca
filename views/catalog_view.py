import tkinter  
from drivers import catalog_driver

import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window
 

class catalog_view():
    def __init__(self, contenedor) -> None:
        self.main_window=contenedor
        
    def catalog_view(self):

        self.catalog_driver= catalog_driver.catalog_driver()

        def btn_catalog_search():
            search_this= var_word_to_search.get()
            in_this_place=var_combobox_where_I_search.get()

            search_results=self.catalog_driver.buscar_obra_catalogo(search_this, in_this_place)

            eliminar = frame_to_show_search.get_children()
            for elemento in eliminar:
                frame_to_show_search.delete(elemento)
        
            search_results.reverse()
            for element in search_results:  
                frame_to_show_search.insert('',0,text=element[0],values=(element[1],element[2],element[3],element[4],element[5]) )
        
        def book_details(s):
            selected_book= frame_to_show_search.item(frame_to_show_search.selection())
            title=selected_book['text']
            author=selected_book['values'][0]
            editorial=selected_book['values'][1]
            quantity_available_books=selected_book['values'][2]
            total=selected_book['values'][3]
            
            lbl_title.configure( text=f'Titulo: {title}')
            lbl_author.configure(text=f'Autor: {author}')
            lbl_editorial.configure(text=f'Editorial: {editorial}')
            lbl_quantity.configure(text=f'Cantidad total: {total}')
            lbl_quantity_available.configure(text=f'Cantidad disponible: {quantity_available_books}')

        # style = ttkbootstrap.Style()
        catalog_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth' )
        catalog_frame.configure(width="990",height="560")
        # frame.place(x=0,y=0)
        
        lbl_title_welcome=ttkbootstrap.Label(catalog_frame,text='Catalogo de obras de la biblioteca', font='Helvetica', anchor='n')
        lbl_title_welcome.place(x=350,y=0)

        #cuadro que contiene la portada del libro
        front_frame=ttkbootstrap.Frame(catalog_frame)
        # front_frame.config(relief='solid', bd=3, background='red')
        front_frame.configure(bootstyle='dark')
        front_frame.place(x=40, y=60, width='200', height='250')


        lbl_title=ttk.Label(catalog_frame, text='Titulo:' ) 
        lbl_title.place(x=250, y=80)

        lbl_author=ttk.Label(catalog_frame, text='Autor:')
        lbl_author.place(x=250, y=110)        
        
        lbl_editorial=ttk.Label(catalog_frame, text='Editorial:')
        lbl_editorial.place(x=250, y=140)  
        
        lbl_quantity=ttk.Label(catalog_frame, text='Cantidad total:')
        lbl_quantity.place(x=250, y=170)
        
        lbl_quantity_available=ttk.Label(catalog_frame, text='Cantidad disponible:')
        lbl_quantity_available.place(x=250, y=200)

        var_summary_obra=""""Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.
                                Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 
                                Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                                Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        #reemplazar var resumen obra por la direccion del resumen guardado en la bd/ el archivo de text debe estar en una carpeta contenedora no en la BD
        summary_obra=tkinter.Text(catalog_frame)
        summary_obra.place(x=40, y=340, width='350', height='150')
        summary_obra.insert('1.0', var_summary_obra)
        summary_obra.configure(state='disabled')  
        
        lbl_where_I_search=ttk.Label(catalog_frame, text="Busqueda de obras por titulo, autor o editorial")
        lbl_where_I_search.place(x=700, y=20)
        
        var_word_to_search=tkinter.StringVar()
        ntry_word_to_search=ttk.Entry(catalog_frame, textvariable=var_word_to_search)
        ntry_word_to_search.place(x=600, y=40)

        var_combobox_where_I_search=tkinter.StringVar()
        combobox_where_I_search=ttk.Combobox(catalog_frame,state='readonly', values=('Titulo', 'Autor', 'Editorial'),textvariable=var_combobox_where_I_search)
        combobox_where_I_search.place(x=750, y=40, width='80')
        
        btn_search_in_catalog=ttk.Button(catalog_frame, text='Buscar', command=btn_catalog_search)#command= btn_busca_obra agregar despues
        btn_search_in_catalog.place(x=850, y=40)

        frame_to_show_search=ttk.Treeview(catalog_frame,bootstyle='info',columns=('Titulo','Autor','Editorial','Disponibles', 'id_obra','totales'))
        frame_to_show_search.place(x=450, y=90,width="600" , height="400")
        frame_to_show_search.heading('#0',text='Titulo')
        frame_to_show_search.heading('#1',text='Autor')
        frame_to_show_search.heading('#2',text='Editorial')
        frame_to_show_search.heading('#3',text='Disponibles')
        frame_to_show_search.heading('#4',text='Disponibles')
        frame_to_show_search.heading('#5',text='Disponibles')

        frame_to_show_search.column('#0', width=150 , minwidth=150)# minwidth=100
        frame_to_show_search.column('#1', width=150, minwidth=150)
        frame_to_show_search.column('#2', width=150, minwidth=150)
        frame_to_show_search.column('#3', width=75, minwidth=90)

        frame_to_show_search.bind("<<TreeviewSelect>>", book_details)
        frame_to_show_search.get_children()
        
  
        return catalog_frame