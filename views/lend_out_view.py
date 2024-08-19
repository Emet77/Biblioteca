
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
                lbl_list_advice.configure(text="Lista de ejemplares")
                list_of_ids.append(seleccion_ejemplar['values'][2])#solo una lista
                frame_book_list.insert('',0,text=seleccion_ejemplar['text'], values=(seleccion_ejemplar['values'][2]))#cuadro treeview

        
        def func_btn_create_loan():
            if(list_of_ids==[]):
                lbl_list_advice.configure(text="Esta lista no debe estar vacia")
            else:
                lbl_list_advice.configure(text="Lista de ejemplares")
                if(var_course.get()=='' or var_sections.get()==''):
                    lbl_second_step.configure(text="Debe seleccionar curso y divicion")
                    
                else:
                    if(var_chkbox_home_loan.get()==1):
                        selected_partner=frame_search_partner.item(frame_search_partner.selection())
                        if(selected_partner['text']==''):
                            print("el array esta vacio")
                            lbl_second_step.configure(text="Debe buscar y elgir un socio")
                        elif(selected_partner['text'] != ''):
                            lbl_second_step.configure(text="")
                            curse=var_course.get()
                            section=var_sections.get()
                            id_curse=int(curse[0])  
                            id_section=int(section[0])
                            id_selected_partner=selected_partner['values'][1]
                            
                            # creado_prestamo=self.controlador.crear_prestamo(curso_id,divicion_id,id_socio,tipo_prestamo,lista_id_ejemplar_agrega)
                            created_loan=self.lend_out_driver.crear_prestamo(id_curse,id_section,id_selected_partner,1 ,list_of_ids )
                            if(created_loan==True):
                                #ARREGLAR : no se muestra el mensaje de prestamo exitoso!
                                function_btn_search()
                                eliminate_list=frame_book_list.get_children()
                                for e in eliminate_list:
                                    frame_book_list.delete(e)

                                eliminate_partner_list=frame_search_partner.get_children()
                                for element in eliminate_partner_list:
                                    frame_search_partner.delete(element)          
                                lbl_second_step.configure(text=f"prestamo realizado con exito")

                            else:
                                lbl_second_step.configure(text=f"Intente nuevamente")
                    else:
                        print("este seria un prestamo grupal")
                        curse=var_course.get()
                        section=var_sections.get()
                        id_curse=int(curse[0])
                        id_section=int(section[0])
                        group_loan=self.lend_out_driver.crear_prestamo(id_curse, id_section, None, 0 , list_of_ids)
                        if(group_loan==True):
                            interface_clean()
                            print("Prestamo grupal, creado con exito")
                        else:
                            print("Something went wrong")
      
        def interface_clean():
             lbl_second_step.configure(text="prestamo realizado con exitooo ")
             function_btn_search()
             func_btn_search_partner()
             eliminate_list=frame_book_list.get_children()
             for e in eliminate_list:
                frame_book_list.delete(e)
                                
             eliminate_partner_list=frame_search_partner.get_children()
             for element in eliminate_partner_list:
                frame_search_partner.delete(element)          


        def select_partner(s):
            selected_partner=frame_search_partner.item(frame_search_partner.selection())
            
            lbl_second_step.configure(text=f"El socio seleccionado es : {selected_partner['text']}")




        def function_btn_search():
            search_this=var_word_to_search_book.get()
            in_this_place=var_where_search.get()
            resultado_busqueda=self.lend_out_driver.buscar_ejemplares_prestamo(search_this, in_this_place)
            pprint(resultado_busqueda)
            
            delete_frame_search = frame_to_show_search.get_children()
            for element in delete_frame_search:
                frame_to_show_search.delete(element)
       
            resultado_busqueda.reverse()
            for elemento in resultado_busqueda:         
                frame_to_show_search.insert('',0,text=elemento[0],values=(elemento[1],elemento[2],elemento[3]) )


        def func_btn_search_partner():
            try:
                search_this_id=var_id_partner.get()
                clean_frame_partners=frame_search_partner.get_children()
                for element in clean_frame_partners:
                    frame_search_partner.delete(element)
        
                search_partner=self.lend_out_driver.verifica_id_socio(search_this_id)
                # pprint(search_partner)
    
                if(search_partner==[]):
                    lbl_num_socio_dni.configure(text='No se encontro coincidencia')
                else:
                    lbl_num_socio_dni.configure(text='Buscar por socio/DNI')
                    for element in search_partner:
                        frame_search_partner.insert('',0,text=element[0], values=(element[1],element[2]))
            except:
                pass          

       


        def func_on_off_home_loan():
            select_type=var_chkbox_home_loan.get()
            if(select_type==0):
                btn_search_partner.configure(state='disabled')
                ntry_socio.configure(state='disabled')
                ntry_socio.delete(0,tkinter.END)

       
            elif(select_type==1):
                btn_search_partner.configure(state='normal')
                ntry_socio.configure(state='normal')
                ntry_socio.delete(0,tkinter.END)
                 

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
        
        btn_search=ttk.Button(lend_out_frame, text='Buscar', command=function_btn_search)# command=funcion_btn_busca
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
#<-------------------------------------------ZONA BENEFICIARIO DEL PRESTAMO--------------------------------------------->

        lbl_second_step=ttk.Label(lend_out_frame, text='Beneficiario del prestamo',font='Helvetica')
        lbl_second_step.place(x=320 , y=250)

        lbl_course=ttk.Label(lend_out_frame, text='Curso')
        lbl_course.place(x=320,y=290, width='150')

        list_of_curses=self.lend_out_driver.cursos_disponibles()
        var_course=tkinter.StringVar()
        course_select=ttk.Combobox(lend_out_frame, state="readonly", values=list_of_curses,textvariable=var_course)#, values=lista_de_cursos
        course_select.place(x=320, y=310,width='100')

        lbl_sections=ttk.Label(lend_out_frame, text='Divicion')
        lbl_sections.place(x=440,y=290, width='150')

        list_of_sections=self.lend_out_driver.diviciones_disponibles()
        var_sections=tkinter.StringVar()
        section_select=ttk.Combobox(lend_out_frame, state="readonly", values=list_of_sections,textvariable=var_sections)#, values=lista_de_cursos
        section_select.place(x=440, y=310,width='100')

        var_chkbox_home_loan=tkinter.IntVar()
        chkbox_home_loan=tkinter.Checkbutton(lend_out_frame, text='Para llevar a casa',state='normal', var=var_chkbox_home_loan,onvalue=1, offvalue=0, command=func_on_off_home_loan)
        chkbox_home_loan.place(x=320, y=350)

        lbl_num_socio_dni=ttk.Label(lend_out_frame, text='Buscar por socio/DNI')
        lbl_num_socio_dni.place(x=320, y=380)    

        var_id_partner=tkinter.IntVar()
        var_id_to_create_loan=tkinter.IntVar()

        validate_entry = lambda text: text.isdecimal()
        ntry_socio=ttk.Entry(lend_out_frame,state='disabled',validate="key",validatecommand=(lend_out_frame.register(validate_entry), "%S"), textvariable=var_id_partner)#Validar para que solo se puedan ingresar numeros enteros positivos
        ntry_socio.place(x=320, y=400, width=80)
        
        btn_search_partner=ttk.Button(lend_out_frame , text="Buscar",state='disabled', command= func_btn_search_partner)
        btn_search_partner.place(x=130+300, y=400)
    

        frame_search_partner=ttk.Treeview(lend_out_frame, columns=('Nombre','DNI','id') )
        frame_search_partner.place(x=320 , y=440 , width=170, height=80)
        frame_search_partner.heading('#0', text='Nombre')
        frame_search_partner.heading('#1',text='DNI')
        frame_search_partner.heading('#2',text='id')
        frame_search_partner.column('#0', width=90, minwidth=90)
        frame_search_partner.column('#1', width=80, minwidth=80)
        frame_search_partner.column('#2', width=5, minwidth=5)

        frame_search_partner.bind("<<TreeviewSelect>>", select_partner)

        btn_create_loan=ttk.Button(lend_out_frame, text='Prestar' , command=func_btn_create_loan)
        btn_create_loan.place(x=580, y=350 )
        


        return lend_out_frame