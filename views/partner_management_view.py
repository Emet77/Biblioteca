import tkinter  
from drivers import catalog_driver,  lend_out_driver, partner_management_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window

class partner_management_view():
    def __init__(self, contenedor):
        self.main_window=contenedor
    def partner_management_view(self):
        self.partner_management_driver=partner_management_driver.partner_management_driver()

        def function_partner_search():
            
            search_this=var_search_partner.get()
            search_results=self.partner_management_driver.buscar_socio(search_this)

            clean_search_frame= frame_to_show_results.get_children()
            for i in clean_search_frame:
                frame_to_show_results.delete(i)
            search_results.reverse()
            for m in search_results:
                frame_to_show_results.insert('',0,text=m[0],values=(m[1],m[2],m[3]) )
            # function_show_panel_edit()
            function_clean_ntrys()
            

        def function_show_details(s):
            self.flag_create_edit_data=True
            selected_partner=frame_to_show_results.item(frame_to_show_results.selection())
            id_partner=selected_partner['text']  
            var_id_partner.set(selected_partner['text'] )
            name=selected_partner['values'][0]
            phone=selected_partner['values'][1]
            dni_partner=selected_partner['values'][2]

            # btn_info_edit.configure(state='normal')
            # function_show_panel_edit()
            function_clean_ntrys()
            
            ntry_partner_name.insert( 0, string=name) #Antes de insertar el valor primero borrar el anterior
            ntry_phone_number.insert(0, string=phone)
            ntry_partner_dni.insert(0, string=dni_partner)
            lbl_partner_id.configure(text=f'Numero Identificador de Socio: {id_partner}' , font='Helvetica')
            btn_save_info.configure(text='Guardar Cambios')
            

        def clean_click_one(s):
            function_clean_ntrys()
            self.flag_create_edit_data=False
            btn_save_info.configure(text='Crea Socio')
        def function_clean_ntrys():

            lbl_partner_id.configure(text=f'Numero Identificador de Socio: ', font='Helvetica')
            ntry_partner_name.delete(0,tkinter.END)
            ntry_phone_number.delete(0,tkinter.END)
            ntry_partner_dni.delete(0,tkinter.END)


        def function_show_panel_edit():
            ntry_partner_dni.configure(state='normal')
            ntry_phone_number.configure(state='normal')
            ntry_partner_name.configure(state='normal')
            # ntry_id_partner.configure(state='normal')
        def function_hiden_panel_edit():
            ntry_partner_dni.configure(state='disable')
            ntry_phone_number.configure(state='disable')
            ntry_partner_name.configure(state='disable')
        
        def function_create_save():
            # esta funcionando pero hay que validad para que no vallan espacios en blanco para que no crashee el programa
            print(self.flag_create_edit_data)
            id=var_id_partner.get()
            name=var_ntry_partner_name.get()
            cellphone=var_ntry_phone_number.get()
            dni=var_ntry_partner_dni.get()
            print(type(id) , id)
            print(type(name) , name)
            print(type(cellphone), cellphone)
            print(type(dni), dni)
            print(id,' ', name ,' ',cellphone,' ' , dni )

            # cellphone=var_ntry_phone_number.get()
            # dni=var_ntry_partner_dni.get()
            # if(self.flag_create_edit_data==True):#eedita datos y podemos hacer .get al var_id
            #     selected_partner=frame_to_show_results.item(frame_to_show_results.selection())
            #     id_partner=selected_partner['text']  
            #     name=selected_partner['values'][0]
               
            #     print(f"estos son los datos a enviar para editar el socio: {id_partner} , {name} , {cellphone} , {dni}")
            # elif(self.flag_create_edit_data==False):
            #     name2=var_ntry_partner_name.get()
            #     cellphone=var_ntry_phone_number.get()
            #     dni=var_ntry_partner_dni.get()
            #     print(f"estos son los datos a enviar para Crear el socio:  {name2} , {cellphone} , {dni}")  
            
            
            
        partner_management_view_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth')
        partner_management_view_frame.configure(width="990",height="560")

        lbl_welcome_message = ttkbootstrap.Label(partner_management_view_frame,text="Gestion de socios", font='Helvetica')
        lbl_welcome_message.place(x=400 , y= 30)

        lbl_search_partner=ttkbootstrap.Label(partner_management_view_frame, text="Buscar socio por DNI o Numero de asociado", font='Helvetica')
        lbl_search_partner.place(x=10, y=50)

        var_search_partner=tkinter.StringVar() #Esta variable es para buscar un socio
        ntry_search_partner=ttkbootstrap.Entry(partner_management_view_frame , textvariable=var_search_partner)
        ntry_search_partner.place(x=10 , y=80)

  
        btn_search_partner=ttkbootstrap.Button(partner_management_view_frame, text='Buscar :)' , command= function_partner_search)
        btn_search_partner.place(x=110, y=80)

        frame_to_show_results=ttk.Treeview(partner_management_view_frame,columns=('id','nombre','telefono','dni'))
        frame_to_show_results.heading('#0',text='id')
        frame_to_show_results.heading('#1',text='Nombre')
        frame_to_show_results.heading('#2',text='Telefono')
        frame_to_show_results.heading('#3',text='DNI')

        frame_to_show_results.column('#0',width=80, minwidth=80) 
        frame_to_show_results.column('#1',width=120, minwidth=120)
        frame_to_show_results.column('#2',width=120, minwidth=120)
        frame_to_show_results.column('#3',width=80, minwidth=80)
        #Agregar una barra de desplazamiento para el cuadro
        frame_to_show_results.place(x=10 , y=120 , width='400', height='300')

        self.flag_create_edit_data=False
        frame_to_show_results.bind("<Double-1>", function_show_details) #Doble click edita los datos Flag = TRue
        frame_to_show_results.bind("<<TreeviewSelect>>", clean_click_one)#un click cancela la edicion Flag =False y crea socio
        # #boton edita
        # btn_info_edit=ttkbootstrap.Button(partner_management_view_frame, state='disable',text='Editar', command=function_show_panel_edit,width='10')
        # btn_info_edit.place(x=450 , y=200)

        # btn elimina
        btn_delete_partner=ttkbootstrap.Button(partner_management_view_frame, state='disable',text='Eliminar', width='10')
        btn_delete_partner.place(x=450, y=250) 

        #lista de labels y entrys para editar o crear un socio       

        lbl_partner_id=ttkbootstrap.Label(partner_management_view_frame, text='Numero Identificador de Socio:', font='Helvetica')
        lbl_partner_id.place(x=540 ,y=60)
        var_id_partner=tkinter.IntVar() #Esta variable es solo para editar un socio se le asigna valor en el momento que seleccionamos en el cuadro
  
        lbl_partner_name=ttkbootstrap.Label(partner_management_view_frame , text='Nombre del asociado' , font='Helvetica')
        lbl_partner_name.place(x=540, y=130)
        
        var_ntry_partner_name=tkinter.StringVar()
        ntry_partner_name=ttkbootstrap.Entry(partner_management_view_frame , textvariable= var_ntry_partner_name )
        ntry_partner_name.place(x=540 , y=160)
        

        lbl_partner_phone_number=ttkbootstrap.Label(partner_management_view_frame, text='Numero telefonico',font='Helvetica')
        lbl_partner_phone_number.place(x=540 ,y=200 )
        validate_entry = lambda text: text.isdecimal()
        var_ntry_phone_number=tkinter.IntVar()
        ntry_phone_number=ttk.Entry(partner_management_view_frame,state='normal',validate="key",validatecommand=(partner_management_view_frame.register(validate_entry), "%S"), textvariable=var_ntry_phone_number)
        ntry_phone_number.place(x=540, y=230)
    

        lbl_partner_dni=ttkbootstrap.Label(partner_management_view_frame, text='DNI' , font='Helvetica')
        lbl_partner_dni.place(x=540 , y=270)

        var_ntry_partner_dni=tkinter.IntVar()
        ntry_partner_dni=ttk.Entry(partner_management_view_frame,state='normal',validate="key",validatecommand=(partner_management_view_frame.register(validate_entry), "%S"), textvariable=var_ntry_partner_dni)
        ntry_partner_dni.place(x=540, y=300)
        

        btn_save_info=ttkbootstrap.Button(partner_management_view_frame, text='Crea Socio', width='20' , command=function_create_save)
        btn_save_info.place(x=570, y=370)
        


        return partner_management_view_frame
