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
            print(search_this)
            search_results=self.partner_management_driver.buscar_socio(search_this)

            clean_search_frame= frame_to_show_results.get_children()
            for i in clean_search_frame:
                frame_to_show_results.delete(i)
            search_results.reverse()
            for m in search_results:
                frame_to_show_results.insert('',0,text=m[0],values=(m[1],m[2],m[3]) )
        def function_show_details(s):
            selected_partner=frame_to_show_results.item(frame_to_show_results.selection())
            # ntry_id_partner.insert(index=0 , string="hola")
            id_partner=selected_partner['text']         
            name=selected_partner['values'][0]
            phone=selected_partner['values'][1]
            dni_partner=selected_partner['values'][2]

            btn_info_edit.configure(state='normal')
            btn_delete_partner.configure(state='normal')
            function_show_panel_edit()
            function_clean_ntrys()
            ntry_id_partner.insert(0, string=id_partner)
            ntry_partner_name.insert( 0, string=name) #Antes de insertar el valor primero borrar el anterior
            ntry_phone_number.insert(0, string=phone)
            ntry_partner_dni.insert(0, string=dni_partner)
            function_hiden_panel_edit()
        def function_clean_ntrys():
            ntry_id_partner.delete(0,tkinter.END)
            ntry_partner_name.delete(0,tkinter.END)
            ntry_phone_number.delete(0,tkinter.END)
            ntry_partner_dni.delete(0,tkinter.END)

        def function_show_panel_edit():
            ntry_partner_dni.configure(state='normal')
            ntry_phone_number.configure(state='normal')
            ntry_partner_name.configure(state='normal')
            ntry_id_partner.configure(state='normal')
        def function_hiden_panel_edit():
            ntry_partner_dni.configure(state='disable')
            ntry_phone_number.configure(state='disable')
            ntry_partner_name.configure(state='disable')
            ntry_id_partner.configure(state='disable')
        def function_save_changes():
            btn_info_edit.configure(state='disable')
            btn_delete_partner.configure(state='disable')

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

        frame_to_show_results.column('#0',width=80, minwidth=80) #Arreglar: las etiquetas del cuadro no deben poder achicarse
        frame_to_show_results.column('#1',width=120, minwidth=120)
        frame_to_show_results.column('#2',width=120, minwidth=120)
        frame_to_show_results.column('#3',width=80, minwidth=80)
        #Agregar una barra de desplazamiento para el cuadro
        frame_to_show_results.place(x=10 , y=120 , width='400', height='300')
        frame_to_show_results.bind("<<TreeviewSelect>>", function_show_details)

        #boton edita
        btn_info_edit=ttkbootstrap.Button(partner_management_view_frame, state='disable',text='Editar', width='10')
        btn_info_edit.place(x=450 , y=200)

        #btn elimina
        btn_delete_partner=ttkbootstrap.Button(partner_management_view_frame, state='disable',text='Eliminar', width='10')
        btn_delete_partner.place(x=450, y=250) 

        #lista de labels y entrys para editar o crear un socio       

        lbl_partner_id=ttkbootstrap.Label(partner_management_view_frame, text='Identificador del socio', font='Helvetica')
        lbl_partner_id.place(x=540 ,y=60)
        var_ntry_id_partner=tkinter.IntVar() #Esta variable es solo para crear un socio
        ntry_id_partner=ttkbootstrap.Entry(partner_management_view_frame, state='readonly') #cambiar el Entry por un label que muestr el id
        ntry_id_partner.place(x=540 , y=90)
        
        lbl_partner_name=ttkbootstrap.Label(partner_management_view_frame , text='Nombre del asociado' , font='Helvetica')
        lbl_partner_name.place(x=540, y=130)
        
        var_ntry_partner_name=tkinter.StringVar()
        ntry_partner_name=ttkbootstrap.Entry(partner_management_view_frame , state='normal')
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
        

        btn_save_info=ttkbootstrap.Button(partner_management_view_frame, text='Guardar Cambios', width='20' )
        btn_save_info.place(x=570, y=370)
        


        return partner_management_view_frame
