import tkinter  
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window

class partner_management_view():
    def __init__(self, contenedor):
        self.main_window=contenedor
    def partner_management_view(self):
        partner_management_view_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth')
        partner_management_view_frame.configure(width="990",height="560")

        lbl_welcome_message = ttkbootstrap.Label(partner_management_view_frame,text="Gestion de socios", font='Helvetica')
        lbl_welcome_message.place(x=400 , y= 30)

        lbl_search_partner=ttkbootstrap.Label(partner_management_view_frame, text="Buscar socio por DNI o Numero de asociado", font='Helvetica')
        lbl_search_partner.place(x=10, y=50)

        ntry_search_partner=ttkbootstrap.Entry(partner_management_view_frame)
        ntry_search_partner.place(x=10 , y=80)

        btn_search_partner=ttkbootstrap.Button(partner_management_view_frame, text='Buscar :)')
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

        #boton edita
        btn_info_edit=ttkbootstrap.Button(partner_management_view_frame, text='Editar', width='10')
        btn_info_edit.place(x=450 , y=200)

        #btn elimina
        btn_delete_partner=ttkbootstrap.Button(partner_management_view_frame, text='Eliminar', width='10')
        btn_delete_partner.place(x=450, y=250) 

        #lista de labels y entrys para editar o crear un socio       

        lbl_partner_id=ttkbootstrap.Label(partner_management_view_frame, text='Identificador del socio', font='Helvetica')
        lbl_partner_id.place(x=540 ,y=60)
        var_ntry_id_partner=tkinter.IntVar()
        ntry_id_partner=ttkbootstrap.Entry(partner_management_view_frame, state='readonly')
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
