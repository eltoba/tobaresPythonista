# -*- coding: utf-8 -*-
from tkinter import *
root=Tk()
# con lo siguiente se hace que la ventana root inicie maximizada
toplevel = root.winfo_toplevel()
toplevel.wm_state('zoomed')

# dimenciones de la ventana principal
root.geometry("300x200") # en realidad esto no tiene mucho sentido si la ventana inicia maximizada
# titulo de la ventana
import getpass
usuarioPC=getpass.getuser() # con esto asignamos a la variable usuarioPC el nombre de usuario de la computadora
tituloVentanaRoot="un titulo para " + usuarioPC
root.title(tituloVentanaRoot)
# asignamos el color de fondo
root["background"]="#161805"
# logo
try:
    root.iconbitmap('logo.ico') # el icono DEBE ser .ico de lo contrario no funcionara
except TclError:
    print("ERROR: El icono de la ventana no pudo ser cargado") # imprime este mensaje si el icono no se encuentra o por alguna razon desconocida no pudo ser cargado
    pass

# Imagenes, nombres asociados:
imagen_salida=PhotoImage("salida", file="salida32x32.gif") # tamaño 32x32
imagen_menu_ayuda=PhotoImage("icono", file="iconoMenu.gif") # tamaño 32x32
imagen_menu_ayuda_quienes_somos=PhotoImage('quienes_somos_icono', file='quienes_somos_icono.gif') # esta imagen es de 48x48
# FUNCIONES:
# creamos la funcion necesaria para mostrar ventanas hijas de root
def mostrarventanaemergente(ventana):
    ventana.deiconify()
def ocultarventanaemergente(ventana):
    ventana.withdraw()
def ejecutar(f):
    root.after(200,f)

#-------------------------------------------------------------------------------
# creamos la ventana001 hija de root
#-------------------------------------------------------------------------------
def funcion_ayuda():
    texto='Esto es la seccion de ayuda'
    var_funcion_ayuda=Label(ventana001, text=texto).pack()
ventana001=Toplevel(root) # ventana001 es una ventana hija de root

#-------------------------------------------------------------------------------
# creamos la ventana002 hija de root
#-------------------------------------------------------------------------------
def funcion_licencia():
    texto="""Esto es un texto de licencia

    como se puede observar esta escrito en multiples lineas

    Es un texto demostrativo para saber que se puede crear un bloque de texto multilinea"""
    var_funcion_licencia=Label(ventana002, text=texto).pack()
ventana002=Toplevel(root) # ventana002 es una ventana hija de root

#-------------------------------------------------------------------------------
# creamos la ventana003 hija de root
#-------------------------------------------------------------------------------
def funcion_quienes_somos():
    texto='Esto es un texto para mostrar en quienes somos'
    var_funcion_quienes_somos=Label(ventana003, text=texto).pack()
ventana003=Toplevel(root) # ventana003 es una ventana hija de root

#-------------------------------------------------------------------------------
# caracteristicas de la ventana001
#-------------------------------------------------------------------------------
ventana001.title('AYUDA') # titulo de la ventana001
ventana001.config(bg='#161805') # color de fondo de la ventana001
ventana001.geometry('500x420') # tamaÃ±o de la ventana001
ventana001.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaÃ±o

#-------------------------------------------------------------------------------
# caracteristicas de la ventana002
#-------------------------------------------------------------------------------
ventana002.title('LICENCIA') # titulo de la ventana001
ventana002.config(bg='#161805') # color de fondo de la ventana001
ventana002.geometry('500x420') # tamaÃ±o de la ventana001
ventana002.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaÃ±o

#-------------------------------------------------------------------------------
# caracteristicas de la ventana003
#-------------------------------------------------------------------------------
ventana003.title('QUIENES SOMOS') # titulo de la ventana001
ventana003.config(bg='#161805') # color de fondo de la ventana001
ventana003.geometry('500x420') # tamaÃ±o de la ventana001
ventana003.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaÃ±o

#-------------------------------------------------------------------------------
# oculta las ventanas hijas
#-------------------------------------------------------------------------------
ventana001.withdraw() # oculta ventana001
ventana002.withdraw() # oculta ventana002
ventana003.withdraw() # oculta ventana003

def Funcion():
    print('Funcion Ejecutada por usuario usando el menu')

menu_general=LabelFrame(root, background="#161805", cursor='pirate', borderwidth=2) # el LabelFrame es necesario como base para apoyar los menus sobre el
menu_general.pack(side=TOP, fill=X)
menu_general.grid()

# explicacion:
# background es el color de fondo del boton
# foreground es el color de las letras en descanso
# activebackground es el color activo del botón al hacer paso de raton
# activeforeground es el color de la fuente al activarse el boton

# menu Archivos
boton_menu_archivo=Menubutton(menu_general, text="Archivo", background="#161805", foreground="#FFFFFF", activebackground="#505015", activeforeground="#F0F0F0") # creamos el boton del menu del cual despus desplegamos los menus
boton_menu_archivo.pack(side=LEFT) # ahora si es verdaderamente visible
menu_archivo=Menu(boton_menu_archivo, background="#161805", foreground="#FFFFFF", activebackground="#505015", activeforeground="#F0F0F0")
menu_archivo.add_command(label="UN MENU", image="icono", compound=LEFT, command=Funcion)
menu_archivo.add_command(label="OTRO MENU", image="icono", compound=LEFT, command=Funcion)
menu_archivo.add_command(label="OTRO MAS :D", image="icono", compound=LEFT, command=Funcion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", image="salida", compound=LEFT, command=root.destroy)
boton_menu_archivo["menu"]=menu_archivo

# menu ayuda
boton_menu_ayuda=Menubutton(menu_general, text="Ayuda", background="#161805", foreground="#FFFFFF", activebackground="#505015", activeforeground="#FFFFFF") # creamos el boton del menu del cual despus desplegamos los menus
boton_menu_ayuda.pack(side=LEFT) # ahora si es verdaderamente visible
menu_ayuda=Menu(boton_menu_ayuda, background="#161805", foreground="#FFFFFF", activebackground="#505050", activeforeground="#FFFFFF")
menu_ayuda.add_separator()
menu_ayuda.add_command(label="Ayuda", image="icono", compound=LEFT, command=lambda:ejecutar(mostrarventanaemergente(ventana001)) or funcion_ayuda())
menu_ayuda.add_command(label="Licencia", image="icono", compound=LEFT, command=lambda:ejecutar(mostrarventanaemergente(ventana002)) or funcion_licencia())
menu_ayuda.add_separator()
menu_ayuda.add_command(label="¿quienes somos?", image="quienes_somos_icono", compound=LEFT, command=lambda:ejecutar(mostrarventanaemergente(ventana003)) or funcion_quienes_somos())
boton_menu_ayuda["menu"]=menu_ayuda

# presentamos el programa
root.mainloop()
