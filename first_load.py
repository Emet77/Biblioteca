import tkinter  
import ttkbootstrap  
from ttkbootstrap.constants import *
import ttkbootstrap.window

from views import buttons_catalog_management
from views.buttons_catalog_management import view_add_legacy_literary_work

first_load_window=ttkbootstrap.Window(themename="litera")

object_add_legacy_literary_wrk=view_add_legacy_literary_work.view_add_legacy_literary_work(first_load_window)
frame_add_legacy_literary_wrk=object_add_legacy_literary_wrk.legacy_literary_work_frame()
frame_add_legacy_literary_wrk.grid(row=0,column=0,sticky='news')

first_load_window.mainloop()