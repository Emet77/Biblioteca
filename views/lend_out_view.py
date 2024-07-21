
import tkinter  
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window
 

class lend_out_view():
 
    def __init__(self, contenedor) -> None:
        self.main_window=contenedor
        # style = ttkbootstrap.Style()
   
    def lend_out_frame(self):
        self.lend_out_driver=  lend_out_driver.lend_out_driver()
 
        def remove_book_from_list(s):
            elimina_registro=frame_book_list.selection()
            elimina_id_lista=frame_book_list.item(frame_book_list.selection())
           
            if(elimina_id_lista['text']==''):
                #"Esta vacio"
                pass
               
            else: 
                list_of_ids.remove( elimina_id_lista['values'][0])
                frame_book_list.delete(elimina_registro)
       
        list_of_ids=[]
        def add_book_to_list(s):
            seleccion_ejemplar=frame_to_show_search.item(frame_to_show_search.selection())
            
            if(seleccion_ejemplar['values'][2] not in list_of_ids):
                list_of_ids.append(seleccion_ejemplar['values'][2])#solo una lista
                frame_book_list.insert('',0,text=seleccion_ejemplar['text'], values=(seleccion_ejemplar['values'][2]))#cuadro treeview
               
        def function_btn_search():
            search_this=var_word_to_search_book.get()
            in_this_place=var_where_search.get()
            resultado_busqueda=self.lend_out_driver.buscar_ejemplares_prestamo(search_this, in_this_place)
            
            delete_frame_search = frame_to_show_search.get_children()
            for element in delete_frame_search:
                frame_to_show_search.delete(element)
       
            resultado_busqueda.reverse()
            for elemento in resultado_busqueda:  
            
                # ['La vuelta al mundo en 80 días 0', 'Julio Verne1', 'Santillana2', 2, 5, 1]
                frame_to_show_search.insert('',0,text=elemento[0],values=(elemento[1],elemento[2],elemento[3]) )
            
        lend_out_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth' )
        lend_out_frame.configure(width="990",height="560")
        # frame.place(x=0,y=0)
        
        lbl_title_welcome=ttkbootstrap.Label(lend_out_frame,text='Creacion de prestamos', font='Helvetica', anchor='n')
        lbl_title_welcome.place(x=350,y=0)

        lbl_info_search=ttk.Label(lend_out_frame, text='Buscar ejemplares por obra, editorial o numero',font='Helvetica')
        lbl_info_search.place(x=20, y=25)
        
        var_word_to_search_book=tkinter.StringVar()
        ntry_search_book=tkinter.Entry(lend_out_frame, textvariable=var_word_to_search_book)
        ntry_search_book.place_configure(x=20 , y=55,height=25)

        var_where_search=tkinter.StringVar()
        cmbox_where_search=ttk.Combobox(lend_out_frame ,state="readonly",values=('Titulo', 'Autor', 'Editorial','Identificador'), textvariable=var_where_search)
        cmbox_where_search.place(x=165, y=55, width=70 , height=25)
        
        btn_search=tkinter.Button(lend_out_frame, text='Buscar', command=function_btn_search)# command=funcion_btn_busca
        btn_search.place_configure( x=255, y=55, height=25) 

        frame_to_show_search=ttk.Treeview(lend_out_frame, columns=('Titulo','Autor','Editorial','Disponibles','Total') )
        frame_to_show_search.place(x=20, y=50+35,width="520" , height="150")
        frame_to_show_search.heading('#0', text='Titulo')
        frame_to_show_search.heading('#1', text='Autor')
        frame_to_show_search.heading('#2',text='Editorial')
        frame_to_show_search.heading('#3', text='Identificador')
        # frame_to_show_search.heading('#4', text='Total')
        frame_to_show_search.column('#0', width=150, minwidth=150)
        frame_to_show_search.column('#1', width=150, minwidth=150)
        frame_to_show_search.column('#2', width=100, minwidth=100)
        frame_to_show_search.column('#3', width=20, minwidth=90)
        # frame_to_show_search.column('#4', width=50)
       
        frame_to_show_search.bind("<Double-1>", add_book_to_list)

        scrollbar_frame_search = ttk.Scrollbar(lend_out_frame, orient=tkinter.VERTICAL, command=frame_to_show_search.yview)
        scrollbar_frame_search.place(x=537 , y=50+35 ,height="150")
    
        

        frame_book_list=ttk.Treeview(lend_out_frame, columns=('Titulo','Identificador'))
        frame_book_list.place(x=555, y=50+35, width='200',height='150')
        frame_book_list.configure(padding=3)
        frame_book_list.heading('#0', text='Titulo')
        frame_book_list.heading('#1', text='Identificador')
        frame_book_list.column('#0', width=100)
        frame_book_list.column('#1', width=100)
        
        frame_book_list.bind("<<TreeviewSelect>>", remove_book_from_list)
        scrollbar_list_book = ttk.Scrollbar(lend_out_frame, orient=tkinter.VERTICAL, command=frame_book_list.yview).place(x=750 , y=50+37 ,height="150")
        
        lbl_list_advice=ttk.Label(lend_out_frame, text='Lista de ejemplares',font='Helvetica')
        lbl_list_advice.place(x=590, y=50+5)

        list_of_curses=self.lend_out_driver.cursos_disponibles()
        lbl_course=ttk.Label(lend_out_frame, text='Curso')
        lbl_course.place(x=20,y=250, width='150')

        var_course=tkinter.StringVar()
        course_select=ttk.Combobox(lend_out_frame, state="readonly", values=list_of_curses,textvariable=var_course)#, values=lista_de_cursos
        course_select.place(x=20, y=270,width='60')









        return lend_out_frame