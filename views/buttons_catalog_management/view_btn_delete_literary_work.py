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

class view_btn_delete_literary_work():
 
    def __init__(self, contenedor):
        self.main_window=contenedor
    
    def frame_delete_partner(self):
        self.driver_partner_management=catalog_driver.catalog_driver()
        def function_clean_interface():
            functio_on_entrys()
            ntry_id.delete(0,tkinter.END)
            ntry_title.delete(0,tkinter.END)
            ntry_author.delete(0,tkinter.END)
            ntry_editorial.delete(0,tkinter.END)
            ntry_book_amount.delete(0,tkinter.END)
            # ntry_search_partner_dni.delete(0,tkinter.END)
            functio_off_entrys()
            # function_btn_search()

        def function_btn_search():
            function_clean_interface()
            var_literary_wrk_id.set(0)
            search_this=var_partner_dni_search.get()
            search_results=self.driver_partner_management.buscar_obra_catalogo(search_this,'general')
            delete_elements=frame_search_literary_work.get_children()

            for i in delete_elements:
                frame_search_literary_work.delete(i)              
            for result in search_results:
                frame_search_literary_work.insert('',0,text=result[0],values=(result[1],result[2],result[3]) )

        def functio_on_entrys():
            ntry_title.configure(state='normal')
            ntry_author.configure(state='normal')
            ntry_editorial.configure(state='normal')
            ntry_book_amount.configure(state='normal')
        def functio_off_entrys():
            ntry_title.configure(state='disable')
            ntry_author.configure(state='disable')
            ntry_editorial.configure(state='disable')
            ntry_book_amount.configure(state='disable')
        def function_selected_literary_wrk(s):
            # lbl_title.configure(text='Editar Datos de Socio',bootstyle='dark')
            try:
                selected_literary_wrk= frame_search_literary_work.item(frame_search_literary_work.selection())

                id=selected_literary_wrk['values'][2]
                title=selected_literary_wrk['text']
                author=selected_literary_wrk['values'][0]
                editorial=selected_literary_wrk['values'][1]
                available_quantity=self.driver_partner_management.ejemplares_totales(id) 
                function_clean_interface()
                functio_on_entrys()
                ntry_id.insert(0,string=id)
                ntry_title.insert( 0, string=title)
                ntry_author.insert(0,string=author)
                ntry_editorial.insert(0,string=editorial)
                ntry_book_amount.insert(0,string=available_quantity)
                functio_off_entrys()
            except:
                pass


                
        def function_delete_partner():

            id_to_delete=var_literary_wrk_id.get()
            if(id_to_delete==0):
                Messagebox.show_info(title='Información',message='Busque y seleccione una obra')
            elif(id_to_delete>0):
                delete_warning= Messagebox.show_question( message='¿Desea eliminar la obra seleccionada?' , title='Titulo' ,buttons=['No:secondary', 'Sí:primary'])
                if(delete_warning=='Sí'):
                    self.driver_partner_management.eliminar_obra_literaria(id_to_delete)
                    Messagebox.show_info(title='Información',message='¡Obra eliminada con exito!')
                    function_clean_interface()
                    function_btn_search()
                elif(delete_warning=='No'):
                    function_clean_interface()
                
        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_columnconfigure(2,weight=1)
        container_frame.grid_rowconfigure(2,weight=1)

        frame_cero=ttkbootstrap.LabelFrame(container_frame,text='',bootstyle='info')
        frame_cero.grid(row=0,column=0,sticky='ew',columnspan=3,pady=5,padx=5)
        frame_cero.grid_columnconfigure(0,weight=1)

        lbl_title=ttkbootstrap.Label(frame_cero,text='Eliminar Datos de Obra Literaria',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)

        frame_one=ttkbootstrap.LabelFrame(container_frame,text='Buscar por titulo, autor',bootstyle='info')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5)
        frame_one.grid_columnconfigure(0,weight=1)
        frame_one.grid_columnconfigure(1,weight=1)
        frame_one.grid_rowconfigure(0,weight=1)

       
        var_partner_dni_search=tkinter.StringVar()
        ntry_search_partner_dni=ttkbootstrap.Entry(frame_one,state='normal',textvariable=var_partner_dni_search)
        ntry_search_partner_dni.grid(row=0,column=0,sticky='news',pady=3,padx=3)

        btn_search=ttkbootstrap.Button(frame_one,text='Buscar',command=function_btn_search)
        btn_search.grid(row=0,column=1)

        frame_search_literary_work=ttkbootstrap.Treeview(frame_one,columns=('titulo','autor'))
        frame_search_literary_work.grid(row=1,column=0,sticky='news',columnspan=2,pady=3,padx=3)
        frame_search_literary_work.heading('#0',text='Titulo')
        frame_search_literary_work.heading('#1',text='Autor')
        frame_search_literary_work.heading('#2',text='Editorial')
        
        frame_search_literary_work.column('#0',width=25,minwidth=25)   
        frame_search_literary_work.column('#1',width=55,minwidth=55)    
        frame_search_literary_work.column('#2',width=55,minwidth=55)   
 
        frame_search_literary_work.bind("<<TreeviewSelect>>",function_selected_literary_wrk)
        frame_two=ttkbootstrap.LabelFrame(container_frame,text='frame Labels',bootstyle='info')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5)

        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_rowconfigure(1,weight=1)
        frame_two.grid_rowconfigure(2,weight=1)
        frame_two.grid_rowconfigure(3,weight=1)


        lbl_title=ttkbootstrap.Label(frame_two,text='Titulo',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='w',pady=3,padx=3)

        lbl_autor=ttkbootstrap.Label(frame_two,text='Autor',font='Helvetica',bootstyle='dark')
        lbl_autor.grid(row=1,column=0,sticky='w',pady=3,padx=3)

        lbl_editorial=ttkbootstrap.Label(frame_two,text='Editorial',font='Helvetica',bootstyle='dark')
        lbl_editorial.grid(row=2,column=0,sticky='w',pady=3,padx=3)

        lbl_amount_books=ttkbootstrap.Label(frame_two,text='Cantidad Disponible',font='Helvetica',bootstyle='dark')
        lbl_amount_books.grid(column=0,row=3,sticky='w',pady=3,padx=3)
        #<----------------------Entrys de loss datos--------------------->
        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Entrys ',bootstyle='danger')
        frame_three.grid(row=1,column=2,sticky='news',pady=5,padx=5)
        frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_rowconfigure(1,weight=1)
        frame_three.grid_rowconfigure(2,weight=1)
        frame_three.grid_rowconfigure(3,weight=1)

        frame_three.grid_columnconfigure(0,weight=1)

        var_literary_wrk_id=tkinter.IntVar()
        ntry_id=ttkbootstrap.Entry(frame_three,textvariable=var_literary_wrk_id)#esta variable se coloca en el frame pero no se muestra 

        var_title=tkinter.StringVar()
        ntry_title=ttkbootstrap.Entry(frame_three,state='disable',textvariable=var_title ,font='Helvetica')
        ntry_title.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        # Validar que solo ingresen numeros enteros el los ntry cellphone y dni
        
        var_author=tkinter.StringVar()
        ntry_author=ttkbootstrap.Entry(frame_three,font='Helvetica',state='disable', textvariable=var_author)  
        ntry_author.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_editorial=tkinter.StringVar()
        ntry_editorial=ttkbootstrap.Entry(frame_three,font='Helvetica',state='disable', textvariable=var_editorial)
        ntry_editorial.grid(row=2,column=0,sticky='we',pady=3,padx=3)

        var_book_amount=tkinter.StringVar()
        ntry_book_amount=ttkbootstrap.Entry(frame_three,font='Helvetica',state='disabled')
        ntry_book_amount.grid(row=3,column=0,sticky='we',padx=3,pady=3)


         #<----------------------boton modifi y cancel--------------------->
        frame_four=ttkbootstrap.LabelFrame(container_frame,text='',bootstyle='danger')
        frame_four.grid(row=2,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        frame_four.grid_columnconfigure(0,weight=1)
        

        # btn_cancell=ttkbootstrap.Button(frame_four,text='Cancelar',bootstyle='info',command=function_clean_interface)
        # btn_cancell.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        btn_save_changes=ttkbootstrap.Button(frame_four,text='¿Eliminar Obra?',bootstyle='danger',command=function_delete_partner)
        btn_save_changes.grid(row=0,column=1,sticky='e',pady=3,padx=3)

        return container_frame
