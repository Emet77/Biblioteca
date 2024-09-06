import shutil
import tkinter
import os
import ttkbootstrap.localization  
from tkinter import filedialog
from PIL import Image , ImageTk
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window

class catalog_magement_view():
    def __init__(self, contenedor) -> None:
        self.main_window=contenedor
    
    def catalog_management_view(self ):
        
        self.catalog_driver= catalog_driver.catalog_driver()
        #<-----------------------Pantallas para cada boton--------------------------------------->
        def function_btn_edit():
            def function_btn_add_cover():
                global img_tk
                filename = filedialog.askopenfilename(filetypes=(("Archivos de imagen",( "*.jpg","*.png" )),("Todos los archivos", "*.*")))
                # lbl_link=ttkbootstrap.Label(book_cover, text=filename)
                # lbl_link.place(x=0 , y=0)
                var_link_cover.set(filename)
                img=Image.open(filename)
                img=img.resize(size=(130,130))#ajustar resize para que llene el cuadro
                img_tk = ImageTk.PhotoImage(img)    
                # shutil.copy(filename, "D:\Proyectos en python\Biblioteca\resources\covers")
                lbl_image= ttkbootstrap.Label(book_cover,image=img_tk)
                lbl_image.place(x=0, y=0)
            def function_delete_cover():
                # necesitamos eliminar la referencia de la foto en la bd 
                pass
            def function_save_changes():
                self.catalog_driver.agregarportada_obra() #aca agregar link_cover
                print(var_link_cover.get())
            
            def btn_search():
                selected_book= frame_to_show_search.item(frame_to_show_search.selection())
                search_this= var_search_literary_work.get()
                in_this_place=''
                search_results=self.catalog_driver.buscar_obra_catalogo(search_this,in_this_place)

                eliminar = frame_to_show_search.get_children()
                for elemento in eliminar:
                    frame_to_show_search.delete(elemento)
            
                search_results.reverse()
                for element in search_results:  
                    frame_to_show_search.insert('',0,text=element[5],values=(element[0], element[1], element[2]) )
            def function_clean_ntrys():
                ntry_edit_title.delete(0,tkinter.END)
                ntry_edit_author.delete(0,tkinter.END)
                ntry_edit_editorial.delete(0,tkinter.END)
            def function_selected_book(s):
                selected_book= frame_to_show_search.item(frame_to_show_search.selection())
                book_id=selected_book['text']
                book_title=selected_book['values'][0]
                book_author=selected_book['values'][1]
                book_editorial=selected_book['values'][2]
                function_clean_ntrys()
                ntry_edit_title.insert( 0, string=book_title)
                ntry_edit_author.insert( 0, string=book_author)
                ntry_edit_editorial.insert( 0, string=book_editorial)
                print('nombre del libro a editrar= ',book_title)
                print('id del libro a editar = ',book_id)
                print('autor libro= ', book_author)
                print('editorial libro= ', book_editorial)


            btn_edit_frame=ttkbootstrap.LabelFrame(big_frame, text='Editar Obra Literaria' ,width=825, height=550, bootstyle='info')
            btn_edit_frame.place(x=155 , y=0)

            var_search_literary_work=tkinter.StringVar()
            ntry_search_literary_work=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_search_literary_work)
            ntry_search_literary_work.place(x=10 , y=20)

            btn_search=ttkbootstrap.Button(btn_edit_frame, text='Buscar', command=btn_search)
            btn_search.place(x=150 , y=20)

            frame_to_show_search=ttk.Treeview(btn_edit_frame,columns=('id','titulo','autor','editorial'))
            frame_to_show_search.heading('#0',text='id')
            frame_to_show_search.heading('#1',text='Titulo')
            frame_to_show_search.heading('#2',text='Autor')
            frame_to_show_search.heading('#3',text='Editorial')

            frame_to_show_search.column('#0',width=40, minwidth=40) 
            frame_to_show_search.column('#1',width=80, minwidth=80)
            frame_to_show_search.column('#2',width=100, minwidth=120)
            frame_to_show_search.column('#3',width=80, minwidth=80)
            #Agregar una barra de desplazamiento para el cuadro
            frame_to_show_search.place(x=10 , y=90 , width='350', height='300')
            frame_to_show_search.bind("<<TreeviewSelect>>", function_selected_book)

            book_cover=ttkbootstrap.LabelFrame(btn_edit_frame,text='Portada', bootstyle='info')
            # front_frame.config(relief='solid', bd=3, background='red')
            # book_cover.configure(bootstyle='dark')
            book_cover.place(x=400, y=20, width='150', height='150')

            btn_add_cover=ttkbootstrap.Button(btn_edit_frame, text='Agregar portada' , bootstyle='success', command=function_btn_add_cover) 
            btn_add_cover.place(x=580 , y=30)
            var_link_cover=tkinter.StringVar()
            
            btn_delete_cover=ttkbootstrap.Button(btn_edit_frame, text='Eliminar portada', bootstyle='warning')
            btn_delete_cover.place(x=580 , y=80)

            lbl_title=ttkbootstrap.Label(btn_edit_frame, text='Titulo')
            lbl_title.place(x=400, y=180)

            var_edit_title=tkinter.StringVar()
            var_id_literary_work=tkinter.IntVar()
            ntry_edit_title=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_edit_title)
            ntry_edit_title.place(x=400, y=200)

            lbl_edit_author=ttkbootstrap.Label(btn_edit_frame, text='Autor')
            lbl_edit_author.place(x=400 , y=250)

            var_edit_author=tkinter.StringVar()
            ntry_edit_author=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_edit_author)
            ntry_edit_author.place(x=400 , y=270)

            lbl_edit_editorial=ttkbootstrap.Label(btn_edit_frame, text='Editorial')
            lbl_edit_editorial.place(x=400, y=320)

            var_edit_editorial=tkinter.StringVar()
            ntry_edit_editorial=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_edit_editorial)
            ntry_edit_editorial.place(x=400, y=340)

            # var_summary_literary_work=tkinter.StringVar()
            var_summary_literary_work="""Acá se van a mostrar los resumenes de obras literarias"""
            txt_summary_obra=ttkbootstrap.Text(btn_edit_frame)
            txt_summary_obra.place(x=580, y=120, width='230', height='270')
            txt_summary_obra.insert('1.0', var_summary_literary_work)
            txt_summary_obra.configure(state='disabled')

            btn_cancel_edit=ttkbootstrap.Button(btn_edit_frame, text='Cancelar Edición')
            btn_cancel_edit.place(x=350, y=430)

            btn_save_changes=ttkbootstrap.Button(btn_edit_frame, text='Guardar Cambios' , command=function_save_changes)
            btn_save_changes.place(x=500 , y=430)

        def function_btn_create():
            create_frame=ttkbootstrap.LabelFrame(big_frame, text='Pantalla de opciones-Para Crear' ,width=825, height=550, bootstyle='info')
            create_frame.place(x=155 , y=0)
            lbl_title_message=ttkbootstrap.Label(create_frame, text='Ventana Crear Obra Literaria' , font='Helvetica')
            lbl_title_message.place(x=200, y=30)

            btn_return=ttkbootstrap.Button(create_frame, text='Volver' )
            btn_return.place(x=250 , y=100)
            

        def function_btn_delete_literary_work():
            delete_literary_work_frame=ttkbootstrap.LabelFrame(big_frame, text='Pantalla de opciones-Para Eliminar Obra literaria' ,width=825, height=550, bootstyle='info')
            delete_literary_work_frame.place(x=155 , y=0)
            lbl_title_message=ttkbootstrap.Label(delete_literary_work_frame, text='Ventana Eliminar Obra Literaria' , font='Helvetica')
            lbl_title_message.place(x=200, y=30)

            btn_return=ttkbootstrap.Button(delete_literary_work_frame, text='Volver' )
            btn_return.place(x=250 , y=100)
            
        
        def function_btn_delete_copy():
            #solo eliminar un ejemplar
            pass
        





        #<-----------------------cuadro chiquito para colocar los botones------------------------>
        big_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth' )
        big_frame.configure(width="990",height="560")

        litle_frame_options=ttkbootstrap.LabelFrame(big_frame, text='Frame Chiquito' , width=150, height=550, bootstyle='primary')
        litle_frame_options.place(x=0 , y=0)

        btn_edit_literary_work=ttkbootstrap.Button(litle_frame_options, text='Editar Obra', bootstyle='primary' , command=function_btn_edit)
        btn_edit_literary_work.place(x=10 , y=20)

        btn_create_literary_work=ttkbootstrap.Button(litle_frame_options, text='Crear Obra literaria ' , command=function_btn_create)
        btn_create_literary_work.place(x=10, y=70)

        btn_delete_literary_work=ttkbootstrap.Button(litle_frame_options, text='Eliminar Obra Literaria',command=function_btn_delete_literary_work)
        btn_delete_literary_work.place(x=10, y=120)

        btn_delete_copy=ttkbootstrap.Button(litle_frame_options, text='Eliminar Ejemplar')
        btn_delete_copy.place(x=10 , y=170)




        #<-----------------------cuadro mediano a la derecha para colocar las pantallas de los botones anteriores-------------------->

        # medium_frame_right=ttkbootstrap.LabelFrame(big_frame, text='Pantalla de opciones' ,width=825, height=550, bootstyle='info')
        # medium_frame_right.place(x=155 , y=0)


        return big_frame