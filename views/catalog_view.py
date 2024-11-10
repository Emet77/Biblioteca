import os
import tkinter  
from drivers import catalog_driver

import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window
from tkinter import filedialog
from PIL import Image , ImageTk
 

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
                frame_to_show_search.insert('',0,text=element[0],values=(element[1],element[2],element[3]) )#,element[4],element[5]
        def function_clean_interface():
            var_combobox_where_I_search.set('')
            var_summary_obra.set('')
            var_word_to_search.set('')
         
        def book_details(s):
            selected_book= frame_to_show_search.item(frame_to_show_search.selection())
            global img_tk
            title=selected_book['text']
            author=selected_book['values'][0]
            editorial=selected_book['values'][1]
            id_literary_work=selected_book['values'][2]
            quantity_available_books=self.catalog_driver.ejemplares_disponibles(id_literary_work)
            total_books=self.catalog_driver.ejemplares_totales(id_literary_work)
            book_cover=self.catalog_driver.mostrar_portada(id_literary_work)
            book_summary=self.catalog_driver.leer_resumen(id_literary_work)    
            
            lbl_title.configure( text=f'Titulo: {title}')
            lbl_author.configure(text=f'Autor: {author}')
            lbl_editorial.configure(text=f'Editorial: {editorial}')
            lbl_quantity.configure(text=f'Cantidad total: {total_books}')
            lbl_quantity_available.configure(text=f'Cantidad disponible: {quantity_available_books}')

  
            if(book_cover==None or book_cover=='' or book_cover=='NULL'):
                actual_dir= os.getcwd()
                no_cover=f"{actual_dir}\\resources\\covers\\no_cover.PNG"
                img=Image.open(no_cover)
                img=img.resize(size=(300,200))#ajustar resize para que llene el cuadro
                img_tk = ImageTk.PhotoImage(img)  
                lbl_image=ttkbootstrap.Label(frame_cover,image=img_tk)
                lbl_image.place(x=0,y=0)
                                
            else:
                # print(book_cover_label)
                img=Image.open(book_cover )
                img=img.resize(size=(300,200))#ajustar resize para que llene el cuadro
                img_tk = ImageTk.PhotoImage(img)    
                lbl_image= ttkbootstrap.Label(frame_cover,image=img_tk)
                lbl_image.place(x=0,y=0)
                
            summary_obra.configure(state='normal')
            summary_obra.delete('1.0',END)
            summary_obra.insert('1.0', book_summary)
            summary_obra.configure(state='disabled')



        the_biggest_frame=ttkbootstrap.LabelFrame(self.main_window,text='este cuadro contiene todos los demas', bootstyle='primary')
        the_biggest_frame.pack( pady=5,padx=5,expand=True,fill='both')

        cuadro_port_resumen=ttkbootstrap.LabelFrame(the_biggest_frame,text='este cuadro permite que apilar los otros dos', bootstyle='primary')
        cuadro_port_resumen.pack(side=LEFT, fill=Y)
        #<-------------portada Obra-------------------------->
        frame_cover=ttkbootstrap.LabelFrame(cuadro_port_resumen, text='Frame portada', bootstyle='primary',width=300,height=200)
        frame_cover.pack(padx=10,pady=10 ,fill='x')#pady=5,padx=5, anchor=N, side='left'

        #<-------------resumen Obra-------------------------->
        # frame_resumen=ttkbootstrap.LabelFrame(cuadro_port_resumen,text='Frame resumen', bootstyle='primary',width=300,height=200)
        # frame_resumen.pack(pady=5,padx=5)#pady=5,padx=5, before=frame_sup_izq,side='left'
        var_summary_obra="Texto a mostrar en el cuadro obra"
        summary_obra=tkinter.Text(cuadro_port_resumen,width=50,font='Helvetica')
        summary_obra.pack(padx=10,pady=10,ipadx=5,ipady=5 ,fill='both')
        summary_obra.insert('1.0', var_summary_obra)
        summary_obra.configure(state='disabled')  

        #<-------------cuadro busqueda y resultados-------------------------->
        frame_cuadro=ttkbootstrap.LabelFrame(the_biggest_frame,text='Aca va la busqueda y el elcuadro que muestra todo',bootstyle='primary')
        frame_cuadro.pack(padx=5,pady=5, fill='both')
                    #<-------------Botones y entry-------------------------->
        frame_contenedor_busqueda=ttkbootstrap.LabelFrame(frame_cuadro,text='contiene la busqueda',bootstyle='primary')#,width=300,height=50
        frame_contenedor_busqueda.pack(anchor=NW,fill='both', padx=3,pady=3)

        var_word_to_search=tkinter.StringVar()
        ntry_buscar=ttkbootstrap.Entry(frame_contenedor_busqueda,textvariable=var_word_to_search)
        ntry_buscar.pack(side=LEFT, padx=3,pady=3,fill='both')
        

        var_combobox_where_I_search=tkinter.StringVar()
        combobox_where_I_search=ttk.Combobox(frame_contenedor_busqueda,state='readonly', values=('Titulo', 'Autor', 'Editorial'),textvariable=var_combobox_where_I_search)
        # combobox_where_I_search.place(x=750, y=40, width='80')
        combobox_where_I_search.pack(side='left',fill='both', padx=3,pady=3)

        btn_buscar=ttkbootstrap.Button(frame_contenedor_busqueda,text='Buscar',command=btn_catalog_search)
        btn_buscar.pack(after=combobox_where_I_search,padx=3,pady=3, fill='both')


                    #<-------------FIN Botones y entry-------------------------->

        # frame_contenedor_treeview=ttkbootstrap.LabelFrame(frame_cuadro,text='contiene la busqueda',bootstyle='primary')
        # frame_contenedor_treeview.pack(anchor=NW)
        frame_to_show_search=ttkbootstrap.Treeview(frame_cuadro,columns=('titulo','autor','editorial','portada','id'))
        # frame_to_show_search.heading('#0',text='id')
        frame_to_show_search.heading('#0',text='Titulo')
        frame_to_show_search.heading('#1',text='Autor')
        frame_to_show_search.heading('#2',text='Editorial')
        frame_to_show_search.heading('#4',text='id')

        frame_to_show_search.column('#0',width=200, minwidth=40 )#
        frame_to_show_search.column('#1',width=200, minwidth=80)#
        frame_to_show_search.column('#2',width=200, minwidth=120)#
        frame_to_show_search.column('#3',width=200, minwidth=80)#
        frame_to_show_search.column('#4',width=5, minwidth=5)#
        frame_to_show_search.bind("<<TreeviewSelect>>", book_details)

        frame_to_show_search.pack(fill='both')

        frame_info_obra=ttkbootstrap.LabelFrame(frame_cuadro, text='Información Obra', bootstyle='darkly',)
        frame_info_obra.pack(fill='both')

        lbl_title=ttkbootstrap.Label(frame_info_obra, text='Titulo: ',font='Helvetica')
        lbl_title.pack()


        lbl_author=ttkbootstrap.Label(frame_info_obra, text='Autor: ',font='Helvetica')
        lbl_author.pack()

        lbl_editorial=ttkbootstrap.Label(frame_info_obra, text='Editorial: ',font='Helvetica')
        lbl_editorial.pack()

        lbl_quantity=ttkbootstrap.Label(frame_info_obra, text='Cantidad Total: ',font='Helvetica')
        lbl_quantity.pack()

        lbl_quantity_available=ttkbootstrap.Label(frame_info_obra, text='Cantidad Disponible: ',font='Helvetica')
        lbl_quantity_available.pack()

        return the_biggest_frame