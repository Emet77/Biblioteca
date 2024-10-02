import tkinter
import ttkbootstrap.localization  
from tkinter import filedialog
from PIL import Image , ImageTk 
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window
from drivers import partner_management_driver

class view_btn_modify_partner():
    def __init__(self, contenedor):
        self.main_window=contenedor
    
    def frame_modify_partner(self):
        self.driver_partner_management=partner_management_driver.partner_management_driver()
        def function_clean_interface():
            ntry_id.delete(0,tkinter.END)
            ntry_name.delete(0,tkinter.END)
            ntry_cellphone.delete(0,tkinter.END)
            ntry_dni.delete(0,tkinter.END)
            ntry_search_partner_dni.delete(0,tkinter.END)

            # function_btn_search()

        def function_btn_search():
            search_this=var_partner_dni_search.get()
            search_results=self.driver_partner_management.buscar_socio(search_this)
            delete_elements=frame_partner_list.get_children()

            for i in delete_elements:
                frame_partner_list.delete(i)              
            for result in search_results:
                frame_partner_list.insert('',0,text=result[0],values=(result[1],result[2],result[3]) )
        
        def function_select_partner(s):
            function_clean_interface()
            lbl_title.configure(text='Editar Datos de Socio',bootstyle='dark')
            selected_partner= frame_partner_list.item(frame_partner_list.selection())
            id=selected_partner['text']
            name=selected_partner['values'][0]
            phone_number=selected_partner['values'][1]
            dni_number=selected_partner['values'][2]
            ntry_name.insert( 0, string=name)
            ntry_cellphone.insert(0,string=phone_number)
            ntry_dni.insert(0,string=dni_number)
            ntry_id.insert(0,string=id)
                
        def function_save_changes():
            try:
                id_partner=var_partner_id.get()
                name=var_partner_name.get()
                cellphone_number=var_partner_cellphone.get()
                dni=var_partner_dni.get()
                # cant_name=len(name) DEBE CONTAR las letras y no los espacios en blanco
                cant_number=len(str(cellphone_number))
                cant_dni=len(str(dni))
            
                if(id_partner==0):
                    lbl_title.configure(text='Primero debe buscar y seleccionar un socio',bootstyle='danger')
                elif(name==''):
                    lbl_title.configure(text='Faltan el Nombre',bootstyle='danger')
                elif(cant_number<10):
                    lbl_title.configure(text='El Numero celular esta incompleto',bootstyle='danger')
                elif( cant_dni<8):
                    lbl_title.configure(text='El DNI esta incompleto',bootstyle='danger')

                elif(name!='' and cellphone_number>=0 and dni>=0):
                    lbl_title.configure(text='¡Datos Guardados Con Exito!',bootstyle='success')
                    self.driver_partner_management.editar_datos_socio(id_partner,name,cellphone_number,dni)
                    function_clean_interface()
                    function_btn_search()
                    # print('esto va ir al controlador: ',name,' ',id_partner,' ',cellphone_number,' ',dni)
                    

            except:
                lbl_title.configure(text='Busque y seleccione un socio para editar',bootstyle='danger')
            
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

        lbl_title=ttkbootstrap.Label(frame_cero,text='Editar Datos de Socio',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)

        frame_one=ttkbootstrap.LabelFrame(container_frame,text='Buscar por DNI o numero de asociado',bootstyle='info')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5)
        frame_one.grid_columnconfigure(0,weight=1)
        frame_one.grid_columnconfigure(1,weight=1)
        frame_one.grid_rowconfigure(0,weight=1)

       
        var_partner_dni_search=tkinter.StringVar()
        ntry_search_partner_dni=ttkbootstrap.Entry(frame_one,state='normal',textvariable=var_partner_dni_search)
        ntry_search_partner_dni.grid(row=0,column=0,sticky='news',pady=3,padx=3)

        btn_search=ttkbootstrap.Button(frame_one,text='Buscar',command=function_btn_search)
        btn_search.grid(row=0,column=1)

        frame_partner_list=ttkbootstrap.Treeview(frame_one,columns=('id','nombre','telefono'))
        frame_partner_list.grid(row=1,column=0,sticky='news',columnspan=2,pady=3,padx=3)
        frame_partner_list.heading('#0',text='id')
        frame_partner_list.heading('#1',text='Nombre')
        frame_partner_list.heading('#2',text='Telefono')
        frame_partner_list.heading('#3',text='Dni')

        frame_partner_list.column('#0',width=25,minwidth=25)   
        frame_partner_list.column('#1',width=55,minwidth=55)    
        frame_partner_list.column('#2',width=55,minwidth=55)    
        frame_partner_list.column('#3',width=55,minwidth=55)   

        frame_partner_list.bind("<Double-1>",function_select_partner)
        frame_two=ttkbootstrap.LabelFrame(container_frame,text='frame Labels',bootstyle='info')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5)

        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_rowconfigure(1,weight=1)
        frame_two.grid_rowconfigure(2,weight=1)

        lbl_name=ttkbootstrap.Label(frame_two,text='Nombre de Usuario',font='Helvetica',bootstyle='dark')
        lbl_name.grid(row=0,column=0,sticky='w',pady=3,padx=3)

        lbl_cellphone=ttkbootstrap.Label(frame_two,text='Numero Celular',font='Helvetica',bootstyle='dark')
        lbl_cellphone.grid(row=1,column=0,sticky='w',pady=3,padx=3)

        lbl_dni=ttkbootstrap.Label(frame_two,text='DNI del Usuario',font='Helvetica',bootstyle='dark')
        lbl_dni.grid(row=2,column=0,sticky='w',pady=3,padx=3)

        #<----------------------Entrys de loss datos--------------------->
        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Entrys ',bootstyle='danger')
        frame_three.grid(row=1,column=2,sticky='news',pady=5,padx=5)
        frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_rowconfigure(1,weight=1)
        frame_three.grid_rowconfigure(2,weight=1)

        frame_three.grid_columnconfigure(0,weight=1)

        var_partner_id=tkinter.IntVar()
        ntry_id=ttkbootstrap.Entry(frame_three,textvariable=var_partner_id)#esta variable se coloca en el frame pero no se muestra 

        var_partner_name=tkinter.StringVar()
        ntry_name=ttkbootstrap.Entry(frame_three, font='Helvetica',textvariable=var_partner_name)
        ntry_name.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        # Validar que solo ingresen numeros enteros el los ntry cellphone y dni
        validate_entry = lambda text: text.isdecimal()
        var_partner_cellphone=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_cellphone=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal',validate="key",validatecommand=(frame_three.register(validate_entry), "%S"), textvariable=var_partner_cellphone)  
        ntry_cellphone.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_partner_dni=tkinter.IntVar()
        ntry_dni=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal',validate="key",validatecommand=(frame_three.register(validate_entry), "%S"), textvariable=var_partner_dni)
        ntry_dni.grid(row=2,column=0,sticky='we',pady=3,padx=3)

         #<----------------------boton modifi y cancel--------------------->
        frame_four=ttkbootstrap.LabelFrame(container_frame,text='Boton crear ',bootstyle='danger')
        frame_four.grid(row=2,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        frame_four.grid_columnconfigure(0,weight=1)
        

        btn_cancell=ttkbootstrap.Button(frame_four,text='Cancelar',bootstyle='info',command=function_clean_interface)
        btn_cancell.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        btn_save_changes=ttkbootstrap.Button(frame_four,text='Guardar Cambios',bootstyle='success',command=function_save_changes)
        btn_save_changes.grid(row=0,column=1,sticky='e',pady=3,padx=3)

        return container_frame
