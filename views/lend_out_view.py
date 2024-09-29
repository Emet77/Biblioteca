
import tkinter  
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window
 

class lend_out_view():
 
    def __init__(self, contenedor) -> None:
        self.main_view=contenedor
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
            seleccion_ejemplar=frame_search.item(frame_search.selection())
            
            if(seleccion_ejemplar['values'][2] not in list_of_ids):
                # lbl_list_advice.configure(text="Lista de ejemplares")
                list_of_ids.append(seleccion_ejemplar['values'][2])#solo una lista
                frame_book_list.insert('',0,text=seleccion_ejemplar['text'], values=(seleccion_ejemplar['values'][2]))#cuadro treeview
  
        def func_btn_create_loan():
            if(list_of_ids==[]):
                lbl_general_information.configure(text="La lista de ejemplares no debe estar vacia")
            else:
                lbl_general_information.configure(text="¡Bienvenido al Programa!")
                if(var_course.get()=='' or var_sections.get()==''):
                    lbl_general_information.configure(text="<---Debe seleccionar Curso y División")
                    
                else:
                    if(var_chkbox_home_loan.get()==1):
                        selected_partner=frame_search_partner.item(frame_search_partner.selection())
                        if(selected_partner['text']==''):
                            print("el array esta vacio")
                            lbl_general_information.configure(text="<---Debe buscar y elgir un socio")
                        elif(selected_partner['text'] != ''):
                            lbl_general_information.configure(text="¡Bienvenido al Programa!")
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
                                lbl_general_information.configure(text="¡prestamo Personal, realizado con exito!")

                            else:
                                lbl_general_information.configure(text="Intente nuevamente")
                    else:
                        print("este seria un prestamo grupal")
                        curse=var_course.get()
                        section=var_sections.get()
                        id_curse=int(curse[0])
                        id_section=int(section[0])
                        group_loan=self.lend_out_driver.crear_prestamo(id_curse, id_section, None, 0 , list_of_ids)
                        # print(f"este es el curso: {curse}")
                        # print(f"este es la División: {section}")
                        # print(f"este es el id curso: {id_curse}")
                        # print(f"este es el id División: {id_section}")
                        if(group_loan==True):
                            interface_clean()
                            print("Prestamo grupal, creado con exito")
                            lbl_general_information.configure(text="¡Prestamo grupal, creado con exito!")
                        else:
                            print("Something went wrong")
                            lbl_general_information.configure(text="Algo salio Mal, :(")
      
        def interface_clean():
             
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

        def function_btn_search():
            lbl_general_information.configure(text="¡Bienvenido al Programa!")
            search_this=var_word_to_search_book.get()
            in_this_place=var_where_search.get()
            resultado_busqueda=self.lend_out_driver.buscar_ejemplares_prestamo(search_this, in_this_place)
            
            delete_frame_search = frame_search.get_children()
            for element in delete_frame_search:
                frame_search.delete(element)
       
            resultado_busqueda.reverse()
            for elemento in resultado_busqueda:         
                frame_search.insert('',0,text=elemento[0],values=(elemento[1],elemento[2],elemento[3]) )

        def func_btn_search_partner():
            try:
                search_this_id=var_id_partner.get()
                clean_frame_partners=frame_search_partner.get_children()
                for element in clean_frame_partners:
                    frame_search_partner.delete(element)
        
                search_partner=self.lend_out_driver.verifica_id_socio(search_this_id)
                # pprint(search_partner)
    
                if(search_partner==[]):
                    lbl_general_information.configure(text='No se encontro coincidencia')
                else:
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
                
        #lend_out_frame=ttkbootstrap.Frame(loan_frame_container, border=5, bootstyle='ligth' )
        #lend_out_frame.configure(width="990",height="560")
        loan_frame_container=ttkbootstrap.Frame(self.main_view ,border=5, bootstyle='ligth' )

        #Pesos de las columnas y filas del cuadro contenedor
        loan_frame_container.grid_columnconfigure(0,weight=1)
        loan_frame_container.grid_columnconfigure(1,weight=1)

        # loan_frame_container.grid_rowconfigure(0,weight=1)
        loan_frame_container.grid_rowconfigure(1,weight=1)
        loan_frame_container.grid_rowconfigure(2,weight=1)
        loan_frame_container.grid_rowconfigure(3,weight=1)
        loan_frame_container.grid_rowconfigure(4,weight=1)
        #<-----------------entry , combobox y boton------------------------------->
        frame_ntry_btn_search=ttkbootstrap.LabelFrame(loan_frame_container, text='Busque su ejemplar aquí',bootstyle='info')
        frame_ntry_btn_search.grid(row=0,column=0,sticky='new',columnspan=3)#,padx=10,pady=10

        frame_ntry_btn_search.grid_columnconfigure(0,weight=1)
        frame_ntry_btn_search.grid_columnconfigure(1,weight=1)
        frame_ntry_btn_search.grid_columnconfigure(2,weight=1)
        frame_ntry_btn_search.grid_columnconfigure(3,weight=1)
        frame_ntry_btn_search.grid_rowconfigure(0,weight=1)



        var_word_to_search_book=tkinter.StringVar()
        ntry_busca=ttkbootstrap.Entry(frame_ntry_btn_search)
        ntry_busca.grid(row=0,column=0,sticky='we',padx=5,pady=5)

        var_where_search=tkinter.StringVar()
        cmbox_where_search=ttk.Combobox(frame_ntry_btn_search ,state="readonly",values=('Titulo', 'Autor', 'Editorial','Identificador'), textvariable=var_where_search)
        cmbox_where_search.grid(row=0,column=1,padx=5,pady=5,sticky='we')

        btn_search=ttk.Button(frame_ntry_btn_search, text='Buscar',command=function_btn_search )
        btn_search.grid(row=0,column=2,padx=5,pady=5,sticky='we')

        lbl_separator=ttkbootstrap.Label(frame_ntry_btn_search,text='')#este label es solo para hacer espacio
        lbl_separator.grid(row=0,column=3,padx=5,pady=5,sticky='we',columnspan=2)
        #<-----------------entry , combobox y boton------------------------------->


        #<-----------------cuadros resultado busqueda y lista ejemplares------------------------------->
        frame_list_search_results=ttkbootstrap.LabelFrame(loan_frame_container, text='',bootstyle='info')
        frame_list_search_results.grid(row=1,column=0,sticky='nswe',columnspan=3,padx=10,pady=10)

        frame_list_search_results.grid_columnconfigure(0,weight=1)
        # frame_list_search_results.grid_columnconfigure(1,weight=1)
        frame_list_search_results.grid_columnconfigure(2,weight=1)
        frame_list_search_results.grid_rowconfigure(0,weight=1)

        frame_container_search=ttkbootstrap.LabelFrame(frame_list_search_results, text='Ejemplares Disponibles',bootstyle='dark')
        frame_container_search.grid(row=0,column=0,sticky='ew',padx=5,pady=5)
        frame_container_search.grid_rowconfigure(0,weight=1)
        frame_container_search.grid_columnconfigure(0,weight=1)
        frame_search=ttk.Treeview(frame_container_search, columns=('Titulo','Autor','Editorial') )
        frame_search.heading('#0', text='Titulo')
        frame_search.heading('#1', text='Autor')
        frame_search.heading('#2',text='Editorial')
        frame_search.heading('#3', text='Identificador')
        frame_search.column('#0',width=55,minwidth=55)
        frame_search.column('#1',width=55,minwidth=55)
        frame_search.column('#2',width=55,minwidth=55)
        frame_search.column('#3',width=55,minwidth=55)
        frame_search.bind("<Double-1>",add_book_to_list)
        frame_search.grid(row=0,column=0,sticky='nswe')#row=0,column=0,sticky='ew',padx=10,pady=10

        scrollbar_frame_search = ttk.Scrollbar(frame_list_search_results, orient=tkinter.VERTICAL, command=frame_search.yview)
        scrollbar_frame_search.grid(row=0,column=1,sticky='ns',padx=3,pady=1)

        frame_container_list=ttkbootstrap.LabelFrame(frame_list_search_results, text='Lista de Ejemplares',bootstyle='dark')
        frame_container_list.grid(row=0,column=2,sticky='ew',padx=5,pady=5)
        frame_container_list.grid_rowconfigure(0,weight=1)
        frame_container_list.grid_columnconfigure(0,weight=1)

        frame_book_list=ttk.Treeview(frame_container_list, columns=('Titulo'))
        frame_book_list.heading('#0', text='Titulo')
        frame_book_list.heading('#1', text='Identificador')
        frame_book_list.column('#0', width=100,minwidth=100)
        frame_book_list.column('#1', width=100,minwidth=100)
        frame_book_list.bind("<<TreeviewSelect>>",  remove_book_from_list)
        frame_book_list.grid(row=0,column=0,sticky='nsew')


        #<-----------------cuadros resultado socios y datos prestar ------------------------------->
        frame_data_create_loan=ttkbootstrap.LabelFrame(loan_frame_container, text='Seleccione a quien prestar el ejemplar',bootstyle='info')
        frame_data_create_loan.grid(row=2,column=0,sticky='we',padx=10,pady=10,rowspan=3)



        # frame_data_create_loan.grid_rowconfigure(0,weight=1)
        # frame_data_create_loan.grid_rowconfigure(1,weight=1)
        # frame_data_create_loan.grid_rowconfigure(2,weight=1)
        frame_data_create_loan.grid_rowconfigure(3,weight=1)
        # frame_data_create_loan.grid_columnconfigure(0,weight=1)
        frame_data_create_loan.grid_columnconfigure(1,weight=1)
        frame_course=ttkbootstrap.LabelFrame(frame_data_create_loan, text='Seleccione Curso y División',bootstyle='info')
        frame_course.grid(row=1,column=0,sticky='new',columnspan=3,padx=10,pady=10)
        frame_course.grid_columnconfigure(1,weight=1)
        frame_course.grid_columnconfigure(3,weight=1)

        lbl_course=ttk.Label(frame_course, text='Curso',font='Helvetica')
        lbl_course.grid(row=1,column=0,sticky='w',padx=2,pady=5)#anchor='center'

        list_of_curses=self.lend_out_driver.cursos_disponibles()
        var_course=tkinter.StringVar()
        course_select=ttk.Combobox(frame_course, state="readonly", values=list_of_curses,textvariable=var_course)#, values=lista_de_cursos
        course_select.grid(row=1,column=1,sticky='w',pady=5)

        lbl_sections=ttk.Label(frame_course, text='División',font='Helvetica')
        lbl_sections.grid(row=1,column=2,sticky='w',pady=5)#anchor='center'

        list_of_sections=self.lend_out_driver.diviciones_disponibles()
        var_sections=tkinter.StringVar()#self.lend_out_driver.cursos_disponibles()
        course_select=ttk.Combobox(frame_course, state="readonly", values=list_of_sections,textvariable=var_sections)#, values=lista_de_cursos
        course_select.grid(row=1,column=3,sticky='w',padx=5,pady=5)


        frame_home_loan=ttkbootstrap.LabelFrame(frame_data_create_loan, text='¿Es un prestamo para llevar fuera del colegio?',bootstyle='info')
        frame_home_loan.grid(row=2,column=0,sticky='new',columnspan=3,padx=10,pady=10)
        frame_home_loan.grid_columnconfigure(1,weight=1)
        # frame_home_loan.grid_columnconfigure(3,weight=1)

        var_chkbox_home_loan=tkinter.IntVar()
        chkbox_home_loan=tkinter.Checkbutton(frame_home_loan, text='¿Para llevar a casa?',font='Helvetica',state='normal', var=var_chkbox_home_loan,onvalue=1, offvalue=0, command=func_on_off_home_loan)#
        chkbox_home_loan.grid(row=0,column=0,padx=5,pady=5,sticky='w')

        var_id_partner=tkinter.IntVar()
        var_id_to_create_loan=tkinter.IntVar()
# 
        validate_entry = lambda text: text.isdecimal()
        ntry_socio=ttk.Entry(frame_home_loan,state='disabled',validate="key",validatecommand=(frame_home_loan.register(validate_entry), "%S"), textvariable=var_id_partner)#Validar para que solo se puedan ingresar numeros enteros positivos
        ntry_socio.grid(row=0,column=1,padx=5,pady=5,sticky='w')


        btn_search_partner=ttk.Button(frame_home_loan , text="Buscar",state='disable', command= func_btn_search_partner)#
        btn_search_partner.grid(row=0,column=2,padx=5,pady=5,sticky='w')


        frame_show_partner=ttkbootstrap.LabelFrame(frame_data_create_loan, text='Estos son los socios encontrados',bootstyle='info')
        frame_show_partner.grid(row=3,column=0,sticky='new',columnspan=3,padx=10,pady=10)

        frame_show_partner.grid_columnconfigure(0,weight=1)
        frame_show_partner.grid_rowconfigure(0,weight=1)

        frame_search_partner=ttk.Treeview(frame_show_partner, columns=('Nombre','DNI') )
        frame_search_partner.heading('#0', text='Nombre')
        frame_search_partner.heading('#1',text='DNI')
        frame_search_partner.heading('#2',text='id')
        frame_search_partner.column('#0', width=90, minwidth=90)
        frame_search_partner.column('#1', width=80, minwidth=80)
        frame_search_partner.column('#2', width=5, minwidth=5)

        frame_search_partner.bind("<<TreeviewSelect>>", select_partner)#

        frame_search_partner.grid(row=0,column=0,sticky='we',padx=10,pady=10)


        #<-----------------cuadro Información ------------------------------->
        frame_information=ttkbootstrap.LabelFrame(loan_frame_container,text='Informacion',bootstyle='dark')
        frame_information.grid(row=3,column=1,sticky='nwe',pady=10,padx=10)#row=2,column=0
        frame_information.grid_columnconfigure(0,weight=1)
        lbl_general_information=ttkbootstrap.Label(frame_information,text='¡Bienvenido al Programa!',bootstyle='danger',font='Helvetica')
        lbl_general_information.grid(row=0,column=0,sticky='n',columnspan=3,pady=10,padx=10)

        #<-----------------cuadro Boton prestar ------------------------------->
        frame_button=ttkbootstrap.LabelFrame(loan_frame_container,text='Para Finalizar, Oprima el boton',bootstyle='info')
        frame_button.grid(row=4,column=1,sticky='nsew',pady=10,padx=10)#row=2,column=0
        frame_button.grid_columnconfigure(0,weight=1)
        frame_button.grid_rowconfigure(0,weight=1)

        button_lend_out=ttkbootstrap.Button(frame_button,text='boton prestar',bootstyle='success', command=func_btn_create_loan)
        button_lend_out.grid(sticky='nsew',pady=10,padx=10)
        

        return loan_frame_container
