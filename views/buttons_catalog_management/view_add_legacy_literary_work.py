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
class view_add_legacy_literary_work():
    def __init__(self,contenedor):
        self.main_window=contenedor
    def legacy_literary_work_frame(self):
        def function_btn_add_cover():
            global img_tk
            filename = filedialog.askopenfilename(filetypes=(("Archivos de imagen",( "*.jpg","*.png" )),("Todos los archivos", "*.*")))
            var_link_cover.set(filename)
            img=Image.open(filename)
            print(frame_cover.winfo_geometry())
            img=img.resize(size=(200,200))#ajustar resize para que llene el cuadro
            img_tk = ImageTk.PhotoImage(img)    
            lbl_image= ttkbootstrap.Label(frame_cover,image=img_tk)
            lbl_image.grid(row=0,column=0,sticky='news')
            # self.catalog_driver.agregarportada_obra(var_link_cover.get(),var_id_literary_work.get() )
            # function_btn_search()

        container_frame=ttkbootstrap.Frame(self.main_window)
        container_frame.grid(row=0,column=0)
        container_frame.grid_columnconfigure(0,weight=1)
        container_frame.grid_columnconfigure(1,weight=1)
        container_frame.grid_columnconfigure(2,weight=1)
        # container_frame.grid_columnconfigure(3,weight=1)

        # container_frame.grid_rowconfigure(1,weight=1)
        # container_frame.grid_rowconfigure(2,weight=1)
        # container_frame.grid_rowconfigure(2,weight=1)
        


        frame_cero=ttkbootstrap.LabelFrame(container_frame,text='',bootstyle='info')
        frame_cero.grid(row=0,column=0,sticky='ew',columnspan=4,pady=5,padx=5)
        frame_cero.grid_columnconfigure(0,weight=1)

        lbl_title=ttkbootstrap.Label(frame_cero,text='Agregar una obra literaria que ya esta inventariada',font='Helvetica',bootstyle='dark')
        lbl_title.grid(row=0,column=0,sticky='n', padx=3,pady=3)

        frame_one=ttkbootstrap.LabelFrame(container_frame,text='Entrys y label todo junto',bootstyle='info')
        frame_one.grid(row=1,column=0,sticky='news',pady=5,padx=5,rowspan=3)
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

        frame_two=ttkbootstrap.LabelFrame(container_frame,text='area rango indice anterior',bootstyle='info')
        frame_two.grid(row=1,column=1,sticky='news',pady=5,padx=5,rowspan=3)
        frame_two.grid_rowconfigure(0,weight=1)
        frame_two.grid_columnconfigure(0,weight=1)
        frame_two.grid_columnconfigure(1,weight=1)


        lbl_info=ttkbootstrap.Label(frame_two,text='Ingrese el rango de numeros de ejemplar que ocupa la obra',font='Helvetica',bootstyle='dark')
        lbl_info.grid(row=0,column=0,sticky='n',columnspan=3,padx=3,pady=3)

        lbl_from=ttkbootstrap.Label(frame_two,text='Desde el numero de ejemplar : ' , font='Helvetica',bootstyle='dark')
        lbl_from.grid(row=1,column=0,sticky='nw',padx=3,pady=3)
        
        lbl_until=ttkbootstrap.Label(frame_two,text='Hasta el numero de ejemplar : ' , font='Helvetica',bootstyle='dark')
        lbl_until.grid(row=2,column=0,sticky='w',padx=3,pady=3)

        var_from_id=tkinter.IntVar()
        validate_entry = lambda text: text.isdecimal()
        ntry_from_id=ttkbootstrap.Entry(frame_two,font='Helvetica',state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_from_id)
        ntry_from_id.grid(row=1,column=1,sticky='w',padx=3,pady=3)

        var_until_id=tkinter.IntVar()
        ntry_until_id=ttkbootstrap.Entry(frame_two,font='Helvetica',state='normal',validate="key",validatecommand=(frame_two.register(validate_entry), "%S"), textvariable=var_until_id)
        ntry_until_id.grid(row=2,column=1,sticky='w',padx=3,pady=3)

        var_link_cover=tkinter.StringVar()
        frame_three=ttkbootstrap.LabelFrame(container_frame,text='Portada',bootstyle='info')
        frame_three.grid(row=1,column=2,sticky='news',pady=5,padx=5)

        frame_four=ttkbootstrap.LabelFrame(container_frame,text='botones',bootstyle='info')
        frame_four.grid(row=2,column=2,sticky='news',pady=5,padx=5)
        # frame_three.grid_columnconfigure(0,weight=1)
        # frame_three.grid_rowconfigure(0,weight=1)
        # var_summary_literary_work=tkinter.StringVar()
        # txt_summary_obra=ttkbootstrap.Text(frame_three,padx=3,pady=3)
        # txt_summary_obra.grid(row=0,column=0)
        # txt_summary_obra.insert('1.0', var_summary_literary_work)
        # txt_summary_obra.configure(state='disable')
        



        # frame_cover=ttkbootstrap.LabelFrame(container_frame,text='imagen de la portada')
        # frame_cover.grid(row=1,column=2,sticky='news',columnspan=2)

        # btn_cancelar=ttkbootstrap.Button(frame_three,text='Cancelar')
        # btn_cancelar.grid(row=1,column=0,sticky='we',padx=3,pady=3)

        # btn_add_cover=ttkbootstrap.Button(frame_three,text='Agregar portada',command=function_btn_add_cover)
        # btn_add_cover.grid(row=1,column=1,sticky='we',padx=3,pady=3)

        return container_frame