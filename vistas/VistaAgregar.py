import tkinter
from tkinter import ttk ,Toplevel , Entry , messagebox
from controladores import ObraLiteraria

class VistaAgregar:
    def __init__(self,ventana_principal) -> None:
        self.ventana_principal = ventana_principal

    def ventana_agrega_obra(self):
        self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        
        def guardar():
            titulo=varTitulo.get()
            autor=varAutor.get()
            cantida=varCantidad.get()
            importancia=varImportacia.get()
            tituloM=titulo.upper()
            autorM=autor.upper() 
            tiene_titulo=len(tituloM)- tituloM.count(' ')
            
            if(tiene_titulo > 0):
                confirma = self.controladorObra.crear_obra( tituloM,autorM,importancia, cantida)
                if(confirma == True):
                    messagebox.showinfo('informacion', 'Una nueva obra fue agregada')
                    ventana_agrega_obra.destroy()
                else:
                    messagebox.showerror('Error','Esta obra ya existe :[')
                    ventana_agrega_obra.destroy()
            elif(tiene_titulo<=0):
               #messagebox.showwarning(title="Información", message="El campo 'Titulo' debe estar lleno :-]")
                messagebox.showerror(title="Información", message="El campo 'Titulo' debe estar lleno :-]")
        
       
            

        ventana_agrega_obra=Toplevel(self.ventana_principal)
        ventana_agrega_obra.geometry("250x250")
        ventana_agrega_obra.title('Agregar una obra literaria')
        lblTitulo = ttk.Label(ventana_agrega_obra,text="Titulo").place(x=10 , y=30, width =35 , height=20 )
        varTitulo=tkinter.StringVar()
        entryTitulo= Entry(ventana_agrega_obra,textvariable= varTitulo).place(x=55,y=30)
        
        lblAutor = ttk.Label(ventana_agrega_obra, text="Autor").place(x=10, y=60)
        varAutor=tkinter.StringVar()
        entryAutor= Entry(ventana_agrega_obra, textvariable=varAutor).place(x=55, y=60)
        
        lblCantidad= ttk.Label(ventana_agrega_obra, text="Cantidad de \n ejemplares").place(x=10, y=90, width=80, height=40)
        varCantidad=tkinter.IntVar() 
        validate_entry = lambda text: text.isdecimal()
        entryCantidad=ttk.Entry(ventana_agrega_obra , validate="key",validatecommand=(ventana_agrega_obra.register(validate_entry), "%S") , textvariable=varCantidad)
        entryCantidad.place(x=100 , y=90, width=40)     
    
        lblImportancia= ttk.Label(ventana_agrega_obra, text="¿Es una obra Importante?").place(x=10 , y=130)
        varImportacia=tkinter.StringVar()
        entryImportancia=ttk.Combobox(ventana_agrega_obra,state="readonly",values=["SI","NO"], textvariable=varImportacia)
        entryImportancia.place(x=150, y=130 , width=40)
        
        btnGuardar=ttk.Button(ventana_agrega_obra, text="Guardar" , command=guardar ).place(x=30 , y=170 , width=80 , height=60)
        btnSalir=ttk.Button(ventana_agrega_obra, text="Salir" , command= ventana_agrega_obra.destroy).place(x=130 , y=170 , width=80 , height=60)            
           
        
        
        
    def ventana_agrega_ejemplar(self, nombreObra , autor , cant , idObra):
     
        def agrega_ejem( ):
            cantida=varCant.get()
            c1=ObraLiteraria.ObraLiteraria('','',0)
            mensaje = c1.agrega_ejemplar(idObra , cantida)
            
            if(cantida>0):
                if(mensaje == True):
                    messagebox.showinfo('informacion', f'Nuevos ejemplares fueron agregados a la obra:  {nombreObra}'  )
                    ventana_agrega_ejemplar.destroy()
                else:
                    messagebox.showerror('Error','Algo salio mal :c \n contacte con el administrador ')
                    ventana_agrega_ejemplar.destroy()
            elif(cantida<=0):
                messagebox.showwarning(title="Información",message='La cantidad de ejemplares debe ser un entero mayor a 0 ' )    
              
            
                      
        ventana_agrega_ejemplar=Toplevel(self.ventana_principal)
        ventana_agrega_ejemplar.geometry("300x200")
        ventana_agrega_ejemplar.title("Agregar 'ejemplares' a una obra literaria")
        lblTitulo1=ttk.Label(ventana_agrega_ejemplar,text=f'Titulo:  ').place(x=10 , y=20)
        lblTitulo2=ttk.Label(ventana_agrega_ejemplar,text=nombreObra).place(x=50, y=20) 
             
        lblAutor1=ttk.Label(ventana_agrega_ejemplar , text='Autor: ').place(x=10, y=40)
        lblAutor2=ttk.Label(ventana_agrega_ejemplar , text=autor).place(x=50, y=40)
        
        lblCant1=ttk.Label(ventana_agrega_ejemplar,text='Cantidad de ejemplares: ').place(x=10, y=60)
        lblCant2=ttk.Label(ventana_agrega_ejemplar,text=cant).place(x=140, y=60)

        lblPregunta=ttk.Label(ventana_agrega_ejemplar, text='¿Cuantos ejemplares desea agregar a esta obra?').place(x=10 , y=80)
        varCant=tkinter.IntVar()
        entryCant=Entry(ventana_agrega_ejemplar, textvariable=varCant).place(x=60, y=110)
        
        btnGuardar=ttk.Button(ventana_agrega_ejemplar, text="Agregar" , command=agrega_ejem ).place(x=50 , y=140 , width=60 , height=40)
        btnSalir=ttk.Button(ventana_agrega_ejemplar, text="Salir" , command= ventana_agrega_ejemplar.destroy).place(x=150 , y=140 ,width=60 , height=40)         


    def ventana_edita_obra(self):
        #self.controladorObra =ObraLiteraria.ObraLiteraria('','',0)
        ventana_agrega_obra=Toplevel(self.ventana_principal)
        ventana_agrega_obra.geometry("400x300")
        ventana_agrega_obra.title('Agregar una obra literaria')
        lblTitulo = ttk.Label(ventana_agrega_obra,text="Titulo")
        lblTitulo.place(x=10 , y=30, width =35 , height=20 )
        prueba=("fasaa")
        varTitulo=tkinter.StringVar(value=prueba) #Este value y los demas deben ser reemplazados con un valor enviado
                                                #la ventana principal 
        entryTitulo= Entry(ventana_agrega_obra,textvariable= varTitulo).place(x=55,y=30 )        