import tkinter
from tkinter import messagebox
from ttkbootstrap.dialogs import MessageDialog , Messagebox
import ttkbootstrap.localization  
from tkinter import filedialog
from PIL import Image , ImageTk 
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
from drivers import partner_management_driver
import ttkbootstrap.window

class view_btn_delete_literary_work():
 
    def __init__(self, contenedor):
        self.main_window=contenedor
    
    def frame_delete_partner(self):
        self.driver_partner_management=partner_management_driver.partner_management_driver()
        def function_clean_interface():
            functio_on_entrys()
            ntry_id.delete(0,tkinter.END)
            ntry_name.delete(0,tkinter.END)
            ntry_cellphone.delete(0,tkinter.END)
            ntry_dni.delete(0,tkinter.END)
            # ntry_search_partner_dni.delete(0,tkinter.END)
            functio_off_entrys()
            # function_btn_search()

        def function_btn_search():
            function_clean_interface()
            var_partner_id.set(0)
            search_this=var_partner_dni_search.get()
            search_results=self.driver_partner_management.buscar_socio(search_this)
            delete_elements=frame_search_literary_work.get_children()

            for i in delete_elements:
                frame_search_literary_work.delete(i)              
            for result in search_results:
                frame_search_literary_work.insert('',0,text=result[0],values=(result[1],result[2],result[3]) )

        def functio_on_entrys():
            ntry_name.configure(state='normal')
            ntry_cellphone.configure(state='normal')
            ntry_dni.configure(state='normal')
        def functio_off_entrys():
            ntry_name.configure(state='disable')
            ntry_cellphone.configure(state='disable')
            ntry_dni.configure(state='disable')

        def function_select_partner(s):
            # lbl_title.configure(text='Editar Datos de Socio',bootstyle='dark')
            try:
                selected_partner= frame_search_literary_work.item(frame_search_literary_work.selection())
                id=selected_partner['text']
                name=selected_partner['values'][0]
                phone_number=selected_partner['values'][1]
                dni_number=selected_partner['values'][2]
                function_clean_interface()
                functio_on_entrys()
                ntry_id.insert(0,string=id)
                ntry_name.insert( 0, string=name)
                ntry_cellphone.insert(0,string=phone_number)
                ntry_dni.insert(0,string=dni_number)
                functio_off_entrys()
            except:
                pass


                
        def function_delete_partner():

            id_partner_delete=var_partner_id.get()
            if(id_partner_delete==0):
                Messagebox.show_info(title='Información',message='Busque y seleccione con f')
            elif(id_partner_delete>0):
                delete_warning= Messagebox.show_question( message='¿Desea eliminar el socio seleccionado?' , title='Titulo' ,buttons=['No:secondary', 'Sí:primary'])
                if(delete_warning=='Sí'):
                    self.driver_partner_management.eliminar_socio(id_partner_delete)
                    Messagebox.show_info(title='Información',message='¡Socio eliminado con exito')
                    function_clean_interface()
                    function_btn_search()
                elif(delete_warning=='No'):
                    function_clean_interface()
                
        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_columnconfigure(2,weight=1)
        # container_frame.grid_rowconfigure(0,weight=1)
        # container_frame.grid_rowconfigure(1,weight=1)
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
 
        frame_search_literary_work.bind("<<TreeviewSelect>>",function_select_partner)
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

        var_partner_id=tkinter.IntVar()
        ntry_id=ttkbootstrap.Entry(frame_three,textvariable=var_partner_id)#esta variable se coloca en el frame pero no se muestra 

        var_partner_name=tkinter.StringVar()
        ntry_name=ttkbootstrap.Entry(frame_three,state='disable',textvariable=var_partner_name,font='Helvetica')
        ntry_name.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        # Validar que solo ingresen numeros enteros el los ntry cellphone y dni
        validate_entry = lambda text: text.isdecimal()
        var_partner_cellphone=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_cellphone=ttkbootstrap.Entry(frame_three,font='Helvetica',state='disable',validate="key",validatecommand=(frame_three.register(validate_entry), "%S"), textvariable=var_partner_cellphone)  
        ntry_cellphone.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_partner_dni=tkinter.IntVar()
        ntry_dni=ttkbootstrap.Entry(frame_three,font='Helvetica',state='disable',validate="key",validatecommand=(frame_three.register(validate_entry), "%S"), textvariable=var_partner_dni)
        ntry_dni.grid(row=2,column=0,sticky='we',pady=3,padx=3)

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
