import tkinter
# from drivers import catalog_driver,  lend_out_driver, partner_management_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window  
from ttkbootstrap.dialogs import MessageDialog , Messagebox
from views.buttons_catalog_management import view_add_legacy_literary_work ,view_add_literary_work
class catalog_management_view():
    def __init__(self, contenedor):
        self.main_window=contenedor
  
    def catalog_management_frame(self):
    
       
        def function_add_legacy_literary_work():
            object_add_legacy_literary_wrk=view_add_legacy_literary_work.view_add_legacy_literary_work(frame_buttons_views)
            frame_add_legacy_literary_wrk=object_add_legacy_literary_wrk.legacy_literary_work_frame()
            frame_add_legacy_literary_wrk.grid(row=0,column=0,sticky='news')
        def function_add_literary_work():
            #elije de que manera agregar la obra
            # election=Messagebox.show_question(message='¿De que manera desea agregar la obra?',title='Información',buttons=['Agregar Obra Existente:info','Crear Desde Cero:info'])
            # if(election=='Agregar Obra Existente'):
            #     function_add_legacy_literary_work()

            # elif(election=='Crear Desde Cero'):
            #     print('Invocar vista agrega obra desde cero')
            object_add_literary_wrk=view_add_literary_work.view_add_literary_work(frame_buttons_views)
            frame_add_literary_wrk=object_add_literary_wrk.view_add_literary_work_frame()
            frame_add_literary_wrk.grid(row=0,column=0,sticky='news')

        partner_management_frame=ttkbootstrap.Frame(self.main_window)
        partner_management_frame.grid_rowconfigure(0,weight=1)
        partner_management_frame.grid_columnconfigure(0,weight=1)

        frame_container=ttkbootstrap.LabelFrame(partner_management_frame,text='contenedor de todo', bootstyle='info')
        frame_container.grid(row=0,column=0,sticky='nsew')
        frame_container.grid_rowconfigure(0,weight=1)
        # frame_container.grid_columnconfigure(0,weight=1)
        frame_container.grid_columnconfigure(1,weight=1)

        #<-------------------Botones-------------------->
        frame_buttons=ttkbootstrap.LabelFrame(frame_container,text='Botones y opciones', bootstyle='info')
        frame_buttons.grid(row=0,column=0,sticky='nsw',padx=5,pady=5)
        frame_buttons.grid_columnconfigure(0,weight=1)
        frame_buttons.grid_rowconfigure(0,weight=1)
        frame_buttons.grid_rowconfigure(1,weight=1)
        frame_buttons.grid_rowconfigure(2,weight=1)
        frame_buttons.grid_rowconfigure(3,weight=1)


        btn_create_literary_work=ttkbootstrap.Button(frame_buttons,text='Agregar Obra Literaria',command=function_add_literary_work)
        btn_create_literary_work.grid(row=0,column=0,padx=3,pady=3,sticky='ewns')


        btn_modify_literary_work=ttkbootstrap.Button(frame_buttons,text='Modificar Obra Literaria')
        btn_modify_literary_work.grid(row=1,column=0,padx=3,pady=3,sticky='ewns')

        btn_delete_literary_work=ttkbootstrap.Button(frame_buttons,text='Eliminar Obra Literaria'  )
        btn_delete_literary_work.grid(row=2,column=0,padx=3,pady=3,sticky='ewns')
        
        btn_delete_book=ttkbootstrap.Button(frame_buttons,text='Eliminar Ejemplar'  )
        btn_delete_book.grid(row=3,column=0,padx=3,pady=3,sticky='ewns')
        #<-------------------Botones-------------------->

        #<-------------------Vistas de Botones-------------------->
        frame_buttons_views=ttkbootstrap.LabelFrame(frame_container,text='Vistas de los Botones', bootstyle='info')
        frame_buttons_views.grid(row=0,column=1,sticky='news',padx=5,pady=5,columnspan=3)
        frame_buttons_views.grid_columnconfigure(0,weight=1)
        frame_buttons_views.grid_rowconfigure(0,weight=1)    

        # frame_buttons_views.grid_columnconfigure(0,weight=1)
        # frame_buttons_views.grid_rowconfigure(0,weight=1)

        return partner_management_frame




# import shutil
# import tkinter
# import os
# import ttkbootstrap.localization  
# from tkinter import filedialog
# from PIL import Image , ImageTk
# from drivers import catalog_driver,  lend_out_driver
# from pprint import *
# import ttkbootstrap  as ttk
# from ttkbootstrap.constants import *
# import ttkbootstrap.window

# class catalog_magement_view():
#     def __init__(self, contenedor) -> None:
#         self.main_window=contenedor
    
#     def catalog_management_view(self ):
        
#         self.catalog_driver= catalog_driver.catalog_driver()
#         #<-----------------------Pantallas para cada boton--------------------------------------->
#         def function_btn_edit():
#             def function_btn_add_cover():
#                 global img_tk
#                 filename = filedialog.askopenfilename(filetypes=(("Archivos de imagen",( "*.jpg","*.png" )),("Todos los archivos", "*.*")))
#                 # lbl_link=ttkbootstrap.Label(book_cover, text=filename)
#                 # lbl_link.place(x=0 , y=0)
#                 var_link_cover.set(filename)
#                 img=Image.open(filename)
#                 img=img.resize(size=(130,130))#ajustar resize para que llene el cuadro
#                 img_tk = ImageTk.PhotoImage(img)    
#                 lbl_image= ttkbootstrap.Label(book_cover,image=img_tk)
#                 lbl_image.place(x=0, y=0)
#                 self.catalog_driver.agregarportada_obra(var_link_cover.get(),var_id_literary_work.get() )
#                 function_btn_search()
#             def function_delete_cover():
#                 # necesitamos eliminar la referencia de la foto en la bd 
#                 id_lit_work=var_id_literary_work.get()
#                 self.catalog_driver.eliminar_portada(id_lit_work)
#                 function_btn_search()
#             def function_save_changes():

#                  #aca agregar link_cover
#                 id_literary_work=var_id_literary_work.get()
#                 author=var_edit_author.get()
#                 title=var_edit_title.get()
#                 editorial=var_edit_editorial.get()
#                 summary=txt_summary_obra.get("1.0", "end-1c")
#                 self.catalog_driver.guardar_datos(id_literary_work, author,title,editorial,summary)

                
            
#             def function_btn_search():
#                 selected_book= frame_to_show_search.item(frame_to_show_search.selection())
#                 search_this= var_search_literary_work.get()
#                 in_this_place='Titulo'
#                 search_results=self.catalog_driver.buscar_obra_catalogo(search_this,in_this_place)

#                 eliminar = frame_to_show_search.get_children()
#                 for elemento in eliminar:
#                     frame_to_show_search.delete(elemento)
            
#                 search_results.reverse()
#                 for element in search_results:  
#                     frame_to_show_search.insert('',0,text=element[5],values=(element[0], element[1], element[2],element[6]) )

#             def function_clean_ntrys():
#                 ntry_edit_title.delete(0,tkinter.END)
#                 ntry_edit_author.delete(0,tkinter.END)
#                 ntry_edit_editorial.delete(0,tkinter.END)
#                 var_link_cover.set('')

            
#             def function_selected_book(s):
#                 function_clean_ntrys()
#                 global img_tk
#                 selected_book= frame_to_show_search.item(frame_to_show_search.selection())
#                 var_id_literary_work.set(selected_book['text'])
#                 book_title=selected_book['values'][0]
#                 book_author=selected_book['values'][1]
#                 book_editorial=selected_book['values'][2]
#                 book_cover_label=selected_book['values'][3]
        
#                 txt_summary_obra.configure(state='normal')
#                 ntry_edit_title.insert( 0, string=book_title)
#                 ntry_edit_author.insert( 0, string=book_author)
#                 ntry_edit_editorial.insert( 0, string=book_editorial)
#                 if(book_cover_label=='None'):
#                     no_cover='D:\\Proyectos en python\\Biblioteca\\resources\\covers\\no_cover.PNG'#cambiar esto por una direccion relativa
#                     img=Image.open(no_cover)
#                     img=img.resize(size=(130,130))#ajustar resize para que llene el cuadro
#                     img_tk = ImageTk.PhotoImage(img)    
#                     lbl_image= ttkbootstrap.Label(book_cover,image=img_tk)
#                     lbl_image.place(x=0, y=0)                  
#                 else:
#                     # print(book_cover_label)
#                     img=Image.open(book_cover_label )
#                     img=img.resize(size=(130,130))#ajustar resize para que llene el cuadro
#                     img_tk = ImageTk.PhotoImage(img)    
#                     lbl_image= ttkbootstrap.Label(book_cover,image=img_tk)
#                     lbl_image.place(x=0, y=0)
#             def funcion_cancel_changes():
#                 function_btn_search()
#                 function_clean_ntrys()


#             btn_edit_frame=ttkbootstrap.LabelFrame(big_frame, text='Editar Obra Literaria' ,width=825, height=550, bootstyle='info')
#             btn_edit_frame.place(x=155 , y=0)

#             var_search_literary_work=tkinter.StringVar()
#             ntry_search_literary_work=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_search_literary_work)
#             ntry_search_literary_work.place(x=10 , y=20)

#             btn_search=ttkbootstrap.Button(btn_edit_frame, text='Buscar', command=function_btn_search)
#             btn_search.place(x=150 , y=20)

#             frame_to_show_search=ttk.Treeview(btn_edit_frame,columns=('id','titulo','autor','editorial','portada'))
#             frame_to_show_search.heading('#0',text='id')
#             frame_to_show_search.heading('#1',text='Titulo')
#             frame_to_show_search.heading('#2',text='Autor')
#             frame_to_show_search.heading('#3',text='Editorial')
#             frame_to_show_search.heading('#4',text='portada')

#             frame_to_show_search.column('#0',width=40, minwidth=40) 
#             frame_to_show_search.column('#1',width=80, minwidth=80)
#             frame_to_show_search.column('#2',width=100, minwidth=120)
#             frame_to_show_search.column('#3',width=80, minwidth=80)
#             frame_to_show_search.column('#4',width=5, minwidth=5)
#             #Agregar una barra de desplazamiento para el cuadro
#             frame_to_show_search.place(x=10 , y=90 , width='350', height='300')
#             frame_to_show_search.bind("<<TreeviewSelect>>", function_selected_book)

#             book_cover=ttkbootstrap.LabelFrame(btn_edit_frame,text='Portada', bootstyle='info')
#             book_cover.place(x=400, y=20, width='150', height='150')

#             btn_add_cover=ttkbootstrap.Button(btn_edit_frame, text='Agregar portada' , bootstyle='success', command=function_btn_add_cover) 
#             btn_add_cover.place(x=580 , y=30)
#             var_link_cover=tkinter.StringVar()
#             var_id_literary_work=tkinter.StringVar()
            
#             btn_delete_cover=ttkbootstrap.Button(btn_edit_frame, text='Eliminar portada', bootstyle='warning', command=function_delete_cover)
#             btn_delete_cover.place(x=580 , y=80)

#             lbl_title=ttkbootstrap.Label(btn_edit_frame, text='Titulo')
#             lbl_title.place(x=400, y=180)

#             var_edit_title=tkinter.StringVar()
#             var_id_literary_work=tkinter.IntVar()
#             ntry_edit_title=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_edit_title)
#             ntry_edit_title.place(x=400, y=200)

#             lbl_edit_author=ttkbootstrap.Label(btn_edit_frame, text='Autor')
#             lbl_edit_author.place(x=400 , y=250)

#             var_edit_author=tkinter.StringVar()
#             ntry_edit_author=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_edit_author)
#             ntry_edit_author.place(x=400 , y=270)

#             lbl_edit_editorial=ttkbootstrap.Label(btn_edit_frame, text='Editorial')
#             lbl_edit_editorial.place(x=400, y=320)

#             var_edit_editorial=tkinter.StringVar()
#             ntry_edit_editorial=ttkbootstrap.Entry(btn_edit_frame, textvariable=var_edit_editorial)
#             ntry_edit_editorial.place(x=400, y=340)

            
#             var_summary_literary_work=tkinter.StringVar()
#             txt_summary_obra=ttkbootstrap.Text(btn_edit_frame)
#             txt_summary_obra.place(x=580, y=120, width='230', height='270')
#             txt_summary_obra.insert('1.0', var_summary_literary_work)
#             txt_summary_obra.configure(state='disable')
            
#             btn_cancel_edit=ttkbootstrap.Button(btn_edit_frame, text='Cancelar Edición', command=funcion_cancel_changes)
#             btn_cancel_edit.place(x=350, y=430)

#             btn_save_changes=ttkbootstrap.Button(btn_edit_frame, text='Guardar Cambios' , command=function_save_changes)
#             btn_save_changes.place(x=500 , y=430)

#         def function_btn_create():
#             create_frame=ttkbootstrap.LabelFrame(big_frame, text='Pantalla de opciones-Para Crear' ,width=825, height=550, bootstyle='info')
#             create_frame.place(x=155 , y=0)
#             lbl_title_message=ttkbootstrap.Label(create_frame, text='Ventana Crear Obra Literaria' , font='Helvetica')
#             lbl_title_message.place(x=200, y=30)

#             btn_return=ttkbootstrap.Button(create_frame, text='Volver' )
#             btn_return.place(x=250 , y=100)
            

#         def function_btn_delete_literary_work():
#             delete_literary_work_frame=ttkbootstrap.LabelFrame(big_frame, text='Pantalla de opciones-Para Eliminar Obra literaria' ,width=825, height=550, bootstyle='info')
#             delete_literary_work_frame.place(x=155 , y=0)
#             lbl_title_message=ttkbootstrap.Label(delete_literary_work_frame, text='Ventana Eliminar Obra Literaria' , font='Helvetica')
#             lbl_title_message.place(x=200, y=30)

#             btn_return=ttkbootstrap.Button(delete_literary_work_frame, text='Volver' )
#             btn_return.place(x=250 , y=100)
            
        
#         def function_btn_delete_copy():
#             #solo eliminar un ejemplar
#             pass
        





#         #<-----------------------cuadro chiquito para colocar los botones------------------------>
#         big_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth' )
#         big_frame.configure(width="990",height="560")

#         litle_frame_options=ttkbootstrap.LabelFrame(big_frame, text='Frame Chiquito' , width=150, height=550, bootstyle='primary')
#         litle_frame_options.place(x=0 , y=0)

#         btn_edit_literary_work=ttkbootstrap.Button(litle_frame_options, text='Editar Obra', bootstyle='primary' , command=function_btn_edit)
#         btn_edit_literary_work.place(x=10 , y=20)

#         btn_create_literary_work=ttkbootstrap.Button(litle_frame_options, text='Crear Obra literaria ' , command=function_btn_create)
#         btn_create_literary_work.place(x=10, y=70)

#         btn_delete_literary_work=ttkbootstrap.Button(litle_frame_options, text='Eliminar Obra Literaria',command=function_btn_delete_literary_work)
#         btn_delete_literary_work.place(x=10, y=120)

#         btn_delete_copy=ttkbootstrap.Button(litle_frame_options, text='Eliminar Ejemplar')
#         btn_delete_copy.place(x=10 , y=170)




#         #<-----------------------cuadro mediano a la derecha para colocar las pantallas de los botones anteriores-------------------->

#         # medium_frame_right=ttkbootstrap.LabelFrame(big_frame, text='Pantalla de opciones' ,width=825, height=550, bootstyle='info')
#         # medium_frame_right.place(x=155 , y=0)


#         return big_frame