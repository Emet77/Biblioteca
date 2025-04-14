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

class view_btn_edit_literary_work():
    def __init__(self,contenedor):
        self.main_window=contenedor
    

    def view_btn_edit_literary_work_frame(self):
        self.literary_work_driver=catalog_driver.catalog_driver()
        #CONTINUAR:
        #se debe agregar el cuadro para cambiar la portada de la obra literaria(listo)
        #en lugar del boton cancelar deberia ser el boton eliminar(listo)
        #deberiamos leer tambien la portada de la obra seleccionada y el resumen para poder edtar ambas cosas(listo)
        # cambiar el tamaño de la imagen de portada en la parte de catalogo y tambien en la parte de editar obra(listo pero puede mejorar)
        #asegurarse que no se pueda usar el boton de cambios  de obra amenos que exista una obra seleccionada, desabilitar el boton(listo)
        #guardar los cambios hechos a la obra
        #al guardar los datos debemos eliminar el archivo de la portada anterior para no tener archivos basura
        #problema al guardar los cambios, creo que el tipo de dato del resumen que eviamos al controlador esta mal 

        
        def btn_search_literary_work():
            search_this= var_search_literary_work.get()
            #in_this_place=var_combobox_where_I_search.get()

            search_results=self.literary_work_driver.buscar_obra_catalogo(search_this, 'edit')
            pprint(search_results)
            eliminar = frame_books_list.get_children()
            for elemento in eliminar:
                frame_books_list.delete(elemento)
        
            search_results.reverse()
            for element in search_results:  
                frame_books_list.insert('',0,text=element[0],values=(element[1],element[2],element[3]) )
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
        def function_select_literary_work(s):
            function_clean_interface()
            btn_save_changes.configure(state=NORMAL)
            global img_tk
            lbl_title.configure(text='Editar Datos de Socio',bootstyle='dark')
            selected_book= frame_books_list.item(frame_books_list.selection())
            id=selected_book['values'][2]
            print("el id de esta obra es: ", id)
            summary=self.literary_work_driver.leer_resumen(id)
            cover=self.literary_work_driver.mostrar_portada(id)
            title=selected_book['text']
            author=selected_book['values'][0]
            editorial=selected_book['values'][1]

            ntry_title.insert( 0, string=title)
            ntry_author.insert(0,string=author)
            ntry_editorial.insert(0,string=editorial)
            ntry_id.insert(0,id)
            txt_summary_obra.configure(state='normal')
            txt_summary_obra.delete('1.0',END)
            txt_summary_obra.insert('1.0', summary)
            txt_summary_obra.configure(state='normal')
            
            if(cover==None or cover=='' or cover=='NULL'):
                actual_dir= os.getcwd()
                no_cover=f"{actual_dir}\\resources\\covers\\no_cover.PNG"
                img=Image.open(no_cover)
                img=img.resize(size=(300,200))#ajustar resize para que llene el cuadro
                img_tk = ImageTk.PhotoImage(img)  
                lbl_image=ttkbootstrap.Label(frame_cover,image=img_tk)
                lbl_image.place(x=0,y=0)
                lbl_image.grid(row=0,column=0,sticky='news')                               
            else:
                # print(book_cover_label)
                img=Image.open(cover )
                img=img.resize(size=(400,400))#ajustar resize para que llene el cuadro
                img_tk = ImageTk.PhotoImage(img)    
                lbl_image= ttkbootstrap.Label(frame_cover,image=img_tk)
                lbl_image.place(x=0,y=0)
                lbl_image.grid(row=0,column=0,sticky='news')
          

        def function_clean_interface():
            btn_save_changes.configure(state=DISABLED)
            ntry_id.delete(0,tkinter.END)
            ntry_title.delete(0,tkinter.END)
            ntry_author.delete(0,tkinter.END)
            ntry_editorial.delete(0,tkinter.END)
            ntry_search_id_literary_work.delete(0,tkinter.END)    
            var_literary_wrk_id.set(0)        

        def function_save_changes():
            titulo=var_title.get()
            autor=var_author.get()
            editorial=var_editorial.get()
            id=var_literary_wrk_id.get() 
            resumen=txt_summary_obra
            portada=var_link_cover.get()
            self.literary_work_driver.guardar_datos(id,titulo,autor,editorial,resumen,portada)
            # print("las variables que vamos a guardar son las siquientes")
            # print("titulo: ", t)
            # print("autor", a)
            # print("editorial", e)
            # print("texto: " , s)
            # print("portada: ", p)
            # print("este es el ide de la obra afectada: ", i)
            


 
 
        container_frame=ttkbootstrap.LabelFrame(self.main_window,text='datos a editar obra')
        container_frame.grid(row=0,column=0)

        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_columnconfigure(2,weight=1)
        container_frame.grid_rowconfigure(2,weight=1)

        frame_cero=ttkbootstrap.LabelFrame(container_frame,text='frame_titulo',bootstyle='info')
        frame_cero.grid(row=0,column=0,sticky='ew',columnspan=3,pady=5,padx=5)
        frame_cero.grid_columnconfigure(0,weight=1)

        lbl_title=ttkbootstrap.Label(frame_cero,text='Editar Datos de Obra',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)

        frame_one=ttkbootstrap.LabelFrame(container_frame,text='Buscar por titulo/autor',bootstyle='info')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5)
        frame_one.grid_columnconfigure(0,weight=1)
        frame_one.grid_columnconfigure(1,weight=1)
        frame_one.grid_rowconfigure(0,weight=1)

       
        var_search_literary_work=tkinter.StringVar()
        ntry_search_id_literary_work=ttkbootstrap.Entry(frame_one,state='normal',textvariable=var_search_literary_work)
        ntry_search_id_literary_work.grid(row=0,column=0,sticky='news',pady=3,padx=3)

        btn_search=ttkbootstrap.Button(frame_one,text='Buscar', command=btn_search_literary_work) 
        btn_search.grid(row=0,column=1)

        frame_books_list=ttkbootstrap.Treeview(frame_one,columns=('titulo','autor','editorial'),displaycolumns=('titulo','autor','editorial'))#titulo autor editorial
        frame_books_list.grid(row=1,column=0,sticky='news',columnspan=2,pady=3,padx=3)
        frame_books_list.heading('#0',text='Titulo')
        frame_books_list.heading('#1',text='Autor')
        frame_books_list.heading('#2',text='Editorial')
        frame_books_list.heading('#3',text='N° Obra')

        frame_books_list.column('#0',width=25,minwidth=25)   
        frame_books_list.column('#1',width=55,minwidth=55)    
        frame_books_list.column('#2',width=55,minwidth=55)     
        frame_books_list.column('#3',width=0,minwidth=0)     

        frame_books_list.bind("<Double-1>",function_select_literary_work)

        frame_two=ttkbootstrap.LabelFrame(container_frame,text='frame Labels',bootstyle='info')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5)

        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_rowconfigure(1,weight=1)
        frame_two.grid_rowconfigure(2,weight=1)

        lbl_name=ttkbootstrap.Label(frame_two,text='Titulo',font='Helvetica',bootstyle='dark')
        lbl_name.grid(row=0,column=0,sticky='w',pady=3,padx=3)

        lbl_cellphone=ttkbootstrap.Label(frame_two,text='Autor',font='Helvetica',bootstyle='dark')
        lbl_cellphone.grid(row=1,column=0,sticky='w',pady=3,padx=3)

        lbl_dni=ttkbootstrap.Label(frame_two,text='Editorial',font='Helvetica',bootstyle='dark')
        lbl_dni.grid(row=2,column=0,sticky='w',pady=3,padx=3)
#<------------------------configurar los entrys para que acepten datos de tipo string------------------------>

        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Entrys ',bootstyle='danger')
        frame_three.grid(row=1,column=2,sticky='news',pady=5,padx=5)
        frame_three.grid_rowconfigure(0,weight=1)
        frame_three.grid_rowconfigure(1,weight=1)
        frame_three.grid_rowconfigure(2,weight=1)

        frame_three.grid_columnconfigure(0,weight=1)

        var_literary_wrk_id=tkinter.IntVar()
        ntry_id=ttkbootstrap.Entry(frame_three,textvariable=var_literary_wrk_id)#esta variable se coloca en el frame pero no se muestra 

        var_title=tkinter.StringVar()
        ntry_title=ttkbootstrap.Entry(frame_three, font='Helvetica',textvariable=var_title)
        ntry_title.grid(row=0,column=0,sticky='we',pady=3,padx=3) 

        var_author=tkinter.StringVar()
        ntry_author=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal', textvariable=var_author)  
        ntry_author.grid(row=1,column=0,sticky='we',pady=3,padx=3)

        var_editorial=tkinter.StringVar()
        ntry_editorial=ttkbootstrap.Entry(frame_three,font='Helvetica',state='normal', textvariable=var_editorial)
        ntry_editorial.grid(row=2,column=0,sticky='we',pady=3,padx=3)

#<------------------------Cambiar portada------------------------>
        frame_four=ttkbootstrap.LabelFrame(container_frame,text='edita portada', bootstyle='success')
        frame_four.grid(row=2,column=1,sticky='news',columnspan=2)
        frame_four.grid_rowconfigure(0,weight=1)
        #frame_four.grid_rowconfigure(1,weight=1)

        frame_four.grid_columnconfigure(0,weight=1)
        frame_four.grid_columnconfigure(1,weight=1)

        frame_cover=ttkbootstrap.LabelFrame(frame_four,text='imagen de la portada')
        frame_cover.grid(row=0,column=0,sticky='news')
        frame_cover.grid_rowconfigure(0,weight=1)
        frame_cover.grid_columnconfigure(0,weight=1)

        # lbl_image= ttkbootstrap.Label(frame_cover)     
        # lbl_image.grid(row=0,column=0,sticky='news')
        # function_btn_cancel_cover()
        
        frame_buttons=ttkbootstrap.LabelFrame(frame_four,text='botones portada',bootstyle='info')
        frame_buttons.grid(row=0,column=1,sticky='ne',pady=5,padx=5)#'sew'
        frame_buttons.columnconfigure(0,weight=1)
        frame_buttons.columnconfigure(1,weight=1)    

        btn_cancelar=ttkbootstrap.Button(frame_buttons,text='Eliminar',bootstyle='danger',command=function_btn_cancel_cover)
        btn_cancelar.grid(row=0,column=0,sticky='n',padx=3,pady=3)

        btn_add_cover=ttkbootstrap.Button(frame_buttons,text='Agregar portada',command=function_btn_add_cover)
        btn_add_cover.grid(row=0,column=1,sticky='n',padx=3,pady=3)
#<------------------------Cambiar resumen------------------------>
        frame_summary=ttkbootstrap.LabelFrame(container_frame,text='Resumen obra',bootstyle='info')
        frame_summary.grid(row=2,column=0,sticky='news',pady=5,padx=5)
        
        frame_summary.grid_columnconfigure(0,weight=1)
        frame_summary.grid_rowconfigure(0,weight=1)
        # var_summary_literary_work=tkinter.StringVar()
        txt_summary_obra=ttkbootstrap.Text(frame_summary,padx=3,pady=3)
        txt_summary_obra.grid(row=0,column=0)
        # txt_summary_obra.insert('1.0', var_summary_literary_work)
        txt_summary_obra.configure(state='normal')
        var_link_cover=tkinter.StringVar()
        var_link_cover.set('NULL')        
#<------------------------area botones------------------------>
        frame_five=ttkbootstrap.LabelFrame(container_frame,text='Boton crear ',bootstyle='danger')
        frame_five.grid(row=3,column=0,sticky='new',pady=5,padx=5,columnspan=3,rowspan=2)
        frame_five.grid_columnconfigure(0,weight=1)
        

        btn_cancell=ttkbootstrap.Button(frame_five,text='Cancelar',bootstyle='info',command=function_clean_interface)
        btn_cancell.grid(row=0,column=0,sticky='e',pady=3,padx=3)

        btn_save_changes=ttkbootstrap.Button(frame_five,state=DISABLED,text='Guardar Cambios',bootstyle='success',command=function_save_changes)
        btn_save_changes.grid(row=0,column=1,sticky='e',pady=3,padx=3)

       




        return container_frame        