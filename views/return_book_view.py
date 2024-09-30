import tkinter  
from drivers import catalog_driver,  lend_out_driver
from pprint import *
import ttkbootstrap  as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.window


class return_book_view():

    def __init__(self, contenedor):
        self.main_window=contenedor
    def return_book_frame(self):
        self.return_book_driver=lend_out_driver.lend_out_driver()


        def function_btn_return():
            num_book=var_id_book_to_return.get()
            if(num_book != 0):
                is_it_returned=self.return_book_driver.devuelve_ejemplar(num_book)
                ntry_id_return_book.delete(0,tkinter.END)
                var_id_book_to_return.set([])
                
                if(is_it_returned==True):
                    lbl_title_info.configure(text="Libro devuelto con exito",bootstyle='success')
                elif(is_it_returned==False):
                    lbl_title_info.configure(text="El libro ya fue devuelto",bootstyle='danger')
            elif(num_book==0):
                lbl_title_info.configure(text="Ingrese un numero diferente de 0",bootstyle='danger')


        def function_btn_search_loan():
            function_clean_interface(1)
            search_this=var_where_i_search.get()
            loan_list=self.return_book_driver.busca_prestamo(search_this)
            clean_frame=frame_to_show_loans.get_children()
            for i in clean_frame:
                frame_to_show_loans.delete(i)
            
            for e in loan_list:
                frame_to_show_loans.insert('',0, text=f"{e[0]} ,{e[1]} ,{e[2]}",values=(e[3],e[4],e[5]))



        def function_btn_detail(s):
            select_loan=frame_to_show_loans.item(frame_to_show_loans.selection())
            loan_id=select_loan['values'][2]
            loan_details=self.return_book_driver.busca_detalle_prestamo(loan_id)

            inf= details_frame_loan.get_children()
            for i in inf:
                details_frame_loan.delete(i)

            for element in loan_details:
                details_frame_loan.insert('',0,text=element[0],values=(element[1],element[2],element[3])) 
        def function_clean_interface(s):
            lbl_title_info.configure(text="Ingrese el identificador del libro a devolver",bootstyle='dark')
            ntry_id_return_book.delete(0,tkinter.END)

        return_book_frame=ttkbootstrap.Frame(self.main_window)     
        return_book_frame.grid_columnconfigure(0,weight=1)
        return_book_frame.grid_columnconfigure(1,weight=1)

        #

        # return_book_frame.grid_rowconfigure(0,weight=1)
        # return_book_frame.grid_rowconfigure(1,weight=1)
        # return_book_frame.grid_rowconfigure(2,weight=1)
        # return_book_frame.grid_rowconfigure(3,weight=1)
        # return_book_frame.grid_rowconfigure(4,weight=1)
        return_book_frame.grid_rowconfigure(6,weight=1)

        frame_cero=ttkbootstrap.Frame(return_book_frame)
        frame_cero.grid(row=0,column=0,sticky='new',padx=5,pady=5,columnspan=2)
        frame_cero.grid_rowconfigure(0,weight=1)
        frame_cero.grid_columnconfigure(0,weight=1)
        lbl_title=ttkbootstrap.Label(frame_cero,text='Devolución de Libros',font='Helvetica')
        lbl_title.grid(row=0,column=0,sticky='n',columnspan=2)

        frame_separator=ttkbootstrap.Frame(return_book_frame)#este separa con la derecha
        frame_separator.grid(row=1,column=1,sticky='wns',rowspan=3,columnspan=3,padx=5,pady=5)

        frame_one=ttkbootstrap.Frame(return_book_frame)
        frame_one.grid(row=2,column=0,sticky='news',padx=5,pady=5)#,columnspan=3
        frame_one.grid_rowconfigure(0,weight=1)
        frame_one.grid_columnconfigure(0,weight=1)
        lbl_title_info=ttkbootstrap.Label(frame_one,text='Ingrese el identificador del libro a devolver',font='Helvetica')
        lbl_title_info.grid(row=0,column=0,sticky='w')

        frame_two=ttkbootstrap.LabelFrame(return_book_frame,text='entry y boton devolver', bootstyle='info')
        frame_two.grid(row=3,column=0,sticky='news',padx=5,pady=5)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_columnconfigure(1,weight=1)
        #asignar un text variable
        var_id_book_to_return=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_id_return_book=ttk.Entry(frame_two,state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_id_book_to_return)
        ntry_id_return_book.grid(row=0,column=0,padx=3,pady=3,sticky='ew')
        btn_return_book=ttkbootstrap.Button(frame_two, text='Devolver', command=function_btn_return)
        btn_return_book.grid(row=0,column=1,padx=3,pady=3,sticky='w')


        frame_three=ttkbootstrap.Frame(return_book_frame)#text='info , devolver libro',
        frame_three.grid(row=4,column=0,sticky='news',padx=5,pady=5,columnspan=3)
        frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_columnconfigure(0,weight=1)
        lbl_search_loan=ttkbootstrap.Label(frame_three,text='Buscar Prestamos',font='Helvetica')
        lbl_search_loan.grid(row=0,column=0,sticky='w',columnspan=2)

        frame_four=ttkbootstrap.LabelFrame(return_book_frame,text='cmbox y boton buscar', bootstyle='info')
        frame_four.grid(row=5,column=0,sticky='news',padx=5,pady=5)
        frame_four.grid_rowconfigure(0,weight=1)
        frame_four.grid_columnconfigure(0,weight=1)
        frame_four.grid_columnconfigure(1,weight=1)
        var_where_i_search=tkinter.StringVar()
        cmbox_where_i_search=ttkbootstrap.Combobox(frame_four, state='readonly', values=('Finalizado', 'Sin finalizar', 'Grupal','Personal'), textvariable=var_where_i_search)
        # cmbox_where_I_search=ttkbootstrap.Combobox(frame_four)
        cmbox_where_i_search.grid(row=0,column=0,padx=3,pady=3,sticky='nwe')
        btn_search_loan=ttkbootstrap.Button(frame_four,text='Buscar :)',command=function_btn_search_loan)
        btn_search_loan.grid(row=0,column=1,padx=3,pady=3,sticky='nw')


        #<------------------------por cada cuadro un frame que los contenga----------------->
        frame_five=ttkbootstrap.LabelFrame(return_book_frame,text='cuadros de resultados', bootstyle='info')#este los contiene a los demas
        frame_five.grid(row=6,column=0,sticky='news',padx=5,pady=5,columnspan=2)
        frame_five.grid_rowconfigure(0,weight=1)
        frame_five.grid_columnconfigure(0,weight=1)
        frame_five.grid_columnconfigure(2,weight=1)
        # frame_six.grid_columnconfigure(1,weight=1)


        container_frame_search=ttkbootstrap.LabelFrame(frame_five,text='cuadros de resultados,Prestamos', bootstyle='info')#este los contiene a los demas
        container_frame_search.grid(row=0,column=0,sticky='news',padx=5,pady=5)
        container_frame_search.grid_columnconfigure(0,weight=1)
        container_frame_search.grid_rowconfigure(0,weight=1)
        frame_to_show_loans=ttk.Treeview(container_frame_search, columns=('Responsable','Fecha Inicio','Fecha Finaliza') )
        frame_to_show_loans.grid(row=0,column=0,sticky='news',padx=5,pady=5)
        frame_to_show_loans.heading('#0', text='Responsable')
        frame_to_show_loans.heading('#1', text='Fecha Inicio')
        frame_to_show_loans.heading('#2', text='Fecha Finaliza')
        frame_to_show_loans.heading('#3', text='id')

        frame_to_show_loans.column('#0',width=55,minwidth=55)
        frame_to_show_loans.column('#1', width=55,minwidth=55)
        frame_to_show_loans.column('#2', width=55,minwidth=55)
        frame_to_show_loans.column('#3', width=55,minwidth=55)
        frame_to_show_loans.bind("<<TreeviewSelect>>", function_btn_detail)

        scrollbar_frame_loans = ttk.Scrollbar(frame_five, orient=tkinter.VERTICAL, command=frame_to_show_loans.yview)
        scrollbar_frame_loans.grid(row=0,column=1,sticky='ns')

        container_frame_details=ttkbootstrap.LabelFrame(frame_five,text='cuadros de resltados,lista de ejemplares', bootstyle='info')
        container_frame_details.grid(row=0,column=2,sticky='news',padx=5,pady=5)
        container_frame_details.grid_columnconfigure(0,weight=1)
        container_frame_details.grid_rowconfigure(0,weight=1)
        details_frame_loan=ttk.Treeview(container_frame_details, columns=('Titulos','Identificadores','Fecha Prestado') )
        details_frame_loan.grid(row=0,column=0,sticky='news',padx=5,pady=5)

        details_frame_loan.heading('#0', text='Titulo')
        details_frame_loan.heading('#1', text='Identificador')
        details_frame_loan.heading('#2', text='Fecha Prestado')#\n
        details_frame_loan.heading('#3', text='Fecha Devuelto')

        details_frame_loan.column('#0', width=55,minwidth=55)
        details_frame_loan.column('#1', width=55,minwidth=55,anchor='center')
        details_frame_loan.column('#2', width=55,minwidth=55)
        details_frame_loan.column('#3', width=55,minwidth=55)   
        details_frame_loan.bind("<<TreeviewSelect>>", function_clean_interface)

        scrollbar_frame_loans = ttk.Scrollbar(frame_five, orient=tkinter.VERTICAL, command=details_frame_loan.yview)
        scrollbar_frame_loans.grid(row=0,column=3,sticky='ns')



        return return_book_frame




        # return_book_frame=ttkbootstrap.Frame(self.main_window, border=5, bootstyle='ligth')
        # return_book_frame.configure(width="990",height="560")

        # lbl_welcome_message = ttkbootstrap.Label(return_book_frame,text="Devolución de libros", font='Helvetica')
        # lbl_welcome_message.place(x=400 , y= 30)

        # lbl_return = ttkbootstrap.Label(return_book_frame , text="Ingrese el identificador del libro a devolver", font='Helvetica')
        # lbl_return.place(x=30, y=50)

        # var_id_book_to_return=tkinter.IntVar()
        # validate_entry = lambda text: text.isdecimal()
        # ntry_id_book_to_return=ttk.Entry(return_book_frame,state='normal',validate="key",validatecommand=(return_book_frame.register(validate_entry), "%S"), textvariable=var_id_book_to_return)
        # ntry_id_book_to_return.place(x=30, y=80)

        # btn_return_book=ttkbootstrap.Button(return_book_frame, text="Devolver", command=function_btn_return)
        # btn_return_book.place(x=130, y=80)

        # lbl_show_info=ttkbootstrap.Label(return_book_frame, text="este label muestra informacion", font='Helvetica')
        # lbl_show_info.place(x=210, y=85)

        # lbl_search_loan=ttkbootstrap.Label(return_book_frame, text="Buscar prestamos", font='Helvetica')
        # lbl_search_loan.place(x=30, y=130)

        # var_where_i_search=tkinter.StringVar()
        # cmbox_where_i_search=ttkbootstrap.Combobox(return_book_frame, state='readonly', values=('Finalizado', 'Sin finalizar', 'Grupal','Personal'), textvariable=var_where_i_search)
        # cmbox_where_i_search.place(x=30, y=160,width=100 , height=30)

        # btn_search_loans=ttkbootstrap.Button(return_book_frame, text='Buscar' , command=function_btn_search_loan)
        # btn_search_loans.place(x=150, y=160)

        # frame_to_show_loans=ttk.Treeview(return_book_frame, columns=('Responsable','Fecha Inicio','Fecha Finaliza','id') )
        # frame_to_show_loans.place(x=30, y=200,width="450" , height="150")
        # frame_to_show_loans.heading('#0', text='Responsable')
        # frame_to_show_loans.heading('#1', text='Fecha\nInicio')
        # frame_to_show_loans.heading('#2', text='Fecha\nFinaliza')
        # frame_to_show_loans.heading('#3', text='id')
        
        # frame_to_show_loans.column('#0',width=230, minwidth=230)
        # frame_to_show_loans.column('#1', width=100, minwidth=100)
        # frame_to_show_loans.column('#2', width=115, minwidth=110)
        # frame_to_show_loans.column('#3', width=20, minwidth=20)
        # frame_to_show_loans.bind("<<TreeviewSelect>>", function_btn_detail)
        # #Agregar un bind para que cada vez que selecciona algo del cuadro se muestren los detalles
        # scrollbar_frame_loans = ttk.Scrollbar(return_book_frame, orient=tkinter.VERTICAL, command=frame_to_show_loans.yview)
        # scrollbar_frame_loans.place(x=480 , y=200 ,height="150")


        # details_frame_loan=ttk.Treeview(return_book_frame, columns=('Titulos','Identificadores','Fecha Prestado','Fecha Devuelto') )
        # details_frame_loan.place(x=580, y=200,width="380" , height="150")
        
        # details_frame_loan.heading('#0', text='Titulo')
        # details_frame_loan.heading('#1', text='Identificador')
        # details_frame_loan.heading('#2', text='Fecha\nPrestado')
        # details_frame_loan.heading('#3', text='Fecha\nDevuelto')
        
        # details_frame_loan.column('#0', width=150, minwidth=160)
        # details_frame_loan.column('#1', width=90, minwidth=90)
        # details_frame_loan.column('#2', width=70, minwidth=70)
        # details_frame_loan.column('#3', width=70, minwidth=70)   

        
         
        # scrollbar_details_frame_loan = ttk.Scrollbar(return_book_frame, orient=tkinter.VERTICAL, command=details_frame_loan.yview)
        # scrollbar_details_frame_loan.place(x=957 , y=200 ,height="150")

   
        

        # return return_book_frame
    