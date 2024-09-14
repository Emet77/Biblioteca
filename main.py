import tkinter  
import ttkbootstrap  
from ttkbootstrap.constants import *
import ttkbootstrap.window
from views import catalog_view , lend_out_view, partner_management_view, return_book_view , catalog_management_view

main_window=ttkbootstrap.Window(themename="litera")##Esta es la ventana principal que contiene todo
#podria agregar un selector deslizante para cambiar entre modo obscuro y claro#
main_window.title("biblioteca 4-117")
main_window.geometry('1000x600')
main_window.resizable(0,0)
main_tabs= ttkbootstrap.Notebook(main_window , bootstyle="info")#pestañas que ordenaran el programa
main_tabs.place(x=0 , y=0)

obj_view_catalog=catalog_view.catalog_view(main_tabs)# objeto que permite crear las vistass
frame_catalog=obj_view_catalog.catalog_view()#funcion que devuelve el un cuadro para agrearlo a las pestañas

obj_lend_out_view= lend_out_view.lend_out_view(main_tabs)#crear objeto
frame_lend_out=obj_lend_out_view.lend_out_frame()#objeto devuelve un cuadro

obj_frame_return_book=return_book_view.return_book_view(main_tabs)
frame_return_book=obj_frame_return_book.return_book_frame()

obj_management_view=partner_management_view.partner_management_view(main_tabs)
frame_partner_management_view = obj_management_view.partner_management_view()

obj_catalog_management= catalog_management_view.catalog_magement_view(main_tabs)
frame_catalog_management_view= obj_catalog_management.catalog_management_view() 

main_tabs.add(frame_catalog,text="Catalogo")#implementacion del cuadro a las pesañas
main_tabs.add(frame_lend_out, text="Crear prestamo")
main_tabs.add(frame_return_book, text="Devolver libro")
main_tabs.add(frame_partner_management_view, text="Gestion de socios")
main_tabs.add(frame_catalog_management_view , text="Gestion de obras")



main_window.mainloop()















