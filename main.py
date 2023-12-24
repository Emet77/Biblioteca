from controladores import ObraLiteraria
from vistas import MenuPrincipal

def main():
    
    libro1 = ObraLiteraria.ObraLiteraria('','',0)
    menu_de_inicio = MenuPrincipal.MenuPrincipal(libro1)
    menu_de_inicio.ventana_principal()
        


    

if __name__ == '__main__':
    main()
    
