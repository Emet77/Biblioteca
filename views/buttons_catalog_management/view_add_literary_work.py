import os
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
class view_add_literary_work():
    def __init__(self,contenedor):
        self.main_window=contenedor
    def view_add_literary_work_frame(self):
        self.controlador= catalog_driver.catalog_driver()
        def function_btn_add_cover():
            global img_tk
            filename = filedialog.askopenfilename(filetypes=(("Archivos de imagen",( "*.jpg","*.png" )),("Todos los archivos", "*.*")))
            var_link_cover.set(filename)
            img=Image.open(filename)
            print(frame_cover.winfo_geometry())
            img=img.resize(size=(300,200))#ajustar resize para que llene el cuadro
            img_tk = ImageTk.PhotoImage(img)    
            lbl_image= ttkbootstrap.Label(frame_cover,image=img_tk)
            lbl_image.grid(row=0,column=0,sticky='news')
            # self.catalog_driver.agregarportada_obra(var_link_cover.get(),var_id_literary_work.get() )
            # function_btn_search()
        def function_btn_cancel():
            ntry_author.delete(0,tkinter.END)
            ntry_editorial.delete(0,tkinter.END)
            ntry_book_copies.delete(0,tkinter.END)
            ntry_title.delete(0,tkinter.END)
            txt_summary_obra.delete('1.0',END)
            # var_summary_literary_work.set('No hay Resumen, Para esta obra')
            # txt_summary_obra.insert('1.0', var_summary_literary_work.get())

            function_btn_cancel_cover()
                        
        def function_btn_cancel_cover():
            #Para cancelar debemos eliminar el link guardado en el var anterior
            var_link_cover.set('NULL')#Con esto nos aseguramos que en la BD aparezca el valor null y se reemplaze la portada cuando la busqyen en el catalogo
            global img_tk
            actual_dir= os.getcwd()
            no_cover=f"{actual_dir}\\resources\\covers\\no_cover.PNG"
            img=Image.open(no_cover)
            img=img.resize(size=(300,200))#ajustar resize para que llene el cuadro
            img_tk = ImageTk.PhotoImage(img)  
            lbl_image2=ttkbootstrap.Label(frame_cover,image=img_tk)
            lbl_image2.grid(row=0,column=0,sticky='news')
            
        def function_btn_add_new_literary_work():
            if(var_title.get()=="" or var_author.get()=="" or var_editorial.get()==""):
                Messagebox.show_info(message='Los campos de Titulo, Autor o Editorial no deben estar vacios',title='Información')
            elif(var_book_copies.get()==""):
                Messagebox.show_info(message='El campo cantidad de ejemplares no deben estar vacio',title='Información')
            else:
                print("los datos estan completos, agregar la obra")
                #titulo,autor,editorial,resumen,portada,cantidad_ejemplares
                m=self.controlador.agregar_obra_nueva(var_title,var_author,var_editorial,txt_summary_obra,var_link_cover,var_book_copies)
                if(m==1):
                    Messagebox.show_info(message='¡obra agregada con exito!',title='Información')
                    function_btn_cancel()
            #Para agregar una obra existente neceito 
            #comprobar que el numero 'desde' sea mayor que 'Hasta'
            #Que los campos importantes esten llenos(Titulo,autor,editorial,'Desde' y 'hasta')
            #La validacion de los campos debe llevarse a cabo en el controlador, si algun dato falta mostrar advertencia.




        container_frame=ttkbootstrap.LabelFrame(self.main_window,text='Este es el cuadro que se devuelve')
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_columnconfigure(2,weight=1)
        # container_frame.grid_columnconfigure(3,weight=1)

        # container_frame.grid_rowconfigure(1,weight=1)
        container_frame.grid_rowconfigure(2,weight=1)
        # container_frame.grid_rowconfigure(2,weight=1)
        

        #<----------------------------------FRAME Cero------------------------>      

        frame_cero=ttkbootstrap.LabelFrame(container_frame,text='',bootstyle='info')
        frame_cero.grid(row=0,column=0,sticky='ew',columnspan=3,pady=5,padx=5)
        frame_cero.grid_columnconfigure(0,weight=1)

        lbl_title=ttkbootstrap.Label(frame_cero,text='Agregar una obra literaria que ya esta inventariada',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)
        #<----------------------------------FRAME One------------------------>      
        frame_one=ttkbootstrap.LabelFrame(container_frame,text='Entrys y label todo junto',bootstyle='info')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5)#,rowspan=3
        frame_one.grid_rowconfigure(0,weight=1)
        frame_one.grid_columnconfigure(0,weight=1)
        frame_one.grid_columnconfigure(1,weight=1)


        lbl_title=ttkbootstrap.Label(frame_one,text='Titulo de la obra',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='w',padx=3,pady=3)

        lbl_author=ttkbootstrap.Label(frame_one,text='Autor de la Obra',font='Helvetica',bootstyle='dark')
        lbl_author.grid(row=1,column=0,sticky='w',padx=3,pady=3)

        lbl_editorial=ttkbootstrap.Label(frame_one,text='Editorial de la Obra',font='Helvetica',bootstyle='dark')
        lbl_editorial.grid(row=2,column=0,sticky='w',padx=3,pady=3)

        var_title=tkinter.StringVar()
        ntry_title=ttkbootstrap.Entry(frame_one,textvariable=var_title)
        ntry_title.grid(row=0,column=1,padx=3,pady=3)

        var_author=tkinter.StringVar()
        ntry_author=ttkbootstrap.Entry(frame_one,textvariable=var_author)
        ntry_author.grid(row=1,column=1,padx=3,pady=3) 

        var_editorial=tkinter.StringVar()
        ntry_editorial=ttkbootstrap.Entry(frame_one,textvariable=var_editorial)
        ntry_editorial.grid(row=2,column=1,padx=3,pady=3) 
        #<----------------------------------FRAME Two------------------------>      
        frame_two=ttkbootstrap.LabelFrame(container_frame,text='Cantidad de ejemplares que posee la obra',bootstyle='info')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5,columnspan=3)#,rowspan=3
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_columnconfigure(1,weight=1)


        lbl_info=ttkbootstrap.Label(frame_two,text='Ingrese la cantidad de ejemplares que posee la obra',font='Helvetica',bootstyle='dark')
        lbl_info.grid(row=0,column=0,sticky='n',columnspan=3,padx=3,pady=3)

        lbl_from=ttkbootstrap.Label(frame_two,text='Cantidad' , font='Helvetica',bootstyle='dark')
        lbl_from.grid(row=1,column=0,sticky='nw',padx=3,pady=3)
        
        # lbl_until=ttkbootstrap.Label(frame_two,text='Hasta el numero de ejemplar : ' , font='Helvetica',bootstyle='dark')
        # lbl_until.grid(row=2,column=0,sticky='w',padx=3,pady=3)

        var_book_copies=tkinter.StringVar()#tkinter.IntVar() #Para evitar el error cuando el campo esta vacio le vamos a dejar el tipo string var y despues lo casteamos en el controlador
        validate_entry = lambda text: text.isdecimal()
        ntry_book_copies=ttkbootstrap.Entry(frame_two,font='Helvetica',state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_book_copies)
        ntry_book_copies.grid(row=1,column=1,sticky='nw',padx=3,pady=3)

        # var_until_id=tkinter.StringVar()
        # ntry_until_id=ttkbootstrap.Entry(frame_two,font='Helvetica',state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_until_id)
        # ntry_until_id.grid(row=2,column=1,sticky='w',padx=3,pady=3)


        #<----------------------------------agregar resumen de la obra------------------------>      
        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Botones',bootstyle='info')
        frame_three.grid(row=2,column=0,sticky='news',pady=5,padx=5)
        
        frame_three.grid_columnconfigure(0,weight=1)
        frame_three.grid_rowconfigure(0,weight=1)
        # var_summary_literary_work=tkinter.StringVar()
        txt_summary_obra=ttkbootstrap.Text(frame_three,padx=3,pady=3)
        txt_summary_obra.grid(row=0,column=0)
        # txt_summary_obra.insert('1.0', var_summary_literary_work)
        txt_summary_obra.configure(state='normal')
        var_link_cover=tkinter.StringVar()
        var_link_cover.set('NULL')
    #<----------------------------------FRAME Four------------------------>      
        frame_four=ttkbootstrap.LabelFrame(container_frame,text='Portada',bootstyle='info')
        frame_four.grid(row=2,column=1,sticky='news',pady=5,padx=5)
        frame_four.grid_rowconfigure(0,weight=1)
        frame_four.grid_rowconfigure(1,weight=1)

        frame_four.grid_columnconfigure(0,weight=1)

        frame_cover=ttkbootstrap.LabelFrame(frame_four,text='imagen de la portada')
        frame_cover.grid(row=0,column=0,sticky='news')
        frame_cover.grid_rowconfigure(0,weight=1)
        frame_cover.grid_columnconfigure(0,weight=1)

        # lbl_image= ttkbootstrap.Label(frame_cover)     
        # lbl_image.grid(row=0,column=0,sticky='news')
        # function_btn_cancel_cover()
        
        frame_buttons=ttkbootstrap.LabelFrame(frame_four,text='botones portada',bootstyle='info')
        frame_buttons.grid(row=1,column=0,sticky='sew',pady=5,padx=5)
        frame_buttons.columnconfigure(0,weight=1)
        frame_buttons.columnconfigure(1,weight=1)    

        btn_cancelar=ttkbootstrap.Button(frame_buttons,text='Cancelar',command=function_btn_cancel_cover)
        btn_cancelar.grid(row=0,column=0,sticky='n',padx=3,pady=3)

        btn_add_cover=ttkbootstrap.Button(frame_buttons,text='Agregar portada',command=function_btn_add_cover)
        btn_add_cover.grid(row=0,column=1,sticky='n',padx=3,pady=3)
        print('columnas y filas de frame cover, ', frame_cover.grid_size())

    #<----------------------------------FRAME Five------------------------>      
        frame_five=ttkbootstrap.LabelFrame(container_frame,text='botones para crear la obra lit',bootstyle='info')
        frame_five.grid(row=2,column=2,sticky='snew',pady=5,padx=5)
        frame_five.columnconfigure(0,weight=1)
        # frame_five.columnconfigure(1,weight=1)    
        frame_five.rowconfigure(0,weight=1)
        frame_five.rowconfigure(1,weight=1)

        
        btn_cancelar_literary_work=ttkbootstrap.Button(frame_five,text='Cancelar',bootstyle='danger',command=function_btn_cancel)
        btn_cancelar_literary_work.grid(row=1,column=0,sticky='nsew',padx=3,pady=3)

        btn_add_literary_work=ttkbootstrap.Button(frame_five,text='Agregar Obra',bootstyle='info',command=function_btn_add_new_literary_work)
        btn_add_literary_work.grid(row=0,column=0,sticky='nsew',padx=3,pady=3)
        

        # print(container_frame.grid_size())#(coulumna,Fila)

        return container_frame