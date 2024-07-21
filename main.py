import tkinter  
import ttkbootstrap  
from ttkbootstrap.constants import *
import ttkbootstrap.window
from views import catalog_view , lend_out_view

main_window=ttkbootstrap.Window(themename="litera")#Esta es la ventana principal que contiene todo
main_window.title("biblioteca 4-117")
main_window.geometry('1000x600')
main_window.resizable(0,0)
main_tabs= ttkbootstrap.Notebook(main_window , bootstyle="info")#pestañas que ordenaran el programa
main_tabs.place(x=0 , y=0)

obj_view_catalog=catalog_view.catalog_view(main_tabs)# objeto que permite crear las vistass
obj_lend_out_view= lend_out_view.lend_out_view(main_tabs)

frame_catalog=obj_view_catalog.catalog_view()#funcion que devuelve el un cuadro para agrearlo a las pestañas
frame_lend_out=obj_lend_out_view.lend_out_frame()

main_tabs.add(frame_catalog,text="catalogo")
main_tabs.add(frame_lend_out, text="Crear prestamo")




main_window.mainloop()
















# import tkinter  
# import ttkbootstrap  
# from ttkbootstrap.constants import *
# import ttkbootstrap.window

# main_window=ttkbootstrap.Window(themename="superhero")
# main_window.title("biblioteca 4-117")
# main_window.geometry('500x400')

# main_tabs= ttkbootstrap.Notebook(main_window , bootstyle="dark")
# main_tabs.pack()
# tab_catalog=ttkbootstrap.Frame(main_tabs)

# main_tabs.add(tab_catalog, text="Catalogo")


# main_window.mainloop()