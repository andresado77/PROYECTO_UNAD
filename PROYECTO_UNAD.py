from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
import sqlite3


# Conectamos a la base de datos
conexion = sqlite3.connect('usuarios.db')

# Creamos una tabla para almacenar los usuarios
conexion.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             usuario TEXT NOT NULL,
             contrasena TEXT NOT NULL);''')

# Cerramos la conexión a la base de datos
conexion.close()

def registrar_usuario():
    # Obtenemos la información almacenada en usuario y contra
    usuario_info = usuario.get()
    contra_info = contra.get()

    # Conectamos a la base de datos
    conexion = sqlite3.connect('usuarios.db')

    # Insertamos los datos del usuario en la tabla usuarios
    conexion.execute(f"INSERT INTO usuarios (usuario, contrasena) VALUES ('{usuario_info}', '{contra_info}');")

    # Cerramos la conexión a la base de datos
    conexion.commit()
    conexion.close()

    # Limpiamos los text variable
    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)

    # Ahora le decimos al usuario que su registro ha sido exitoso
    Label(pantalla1, text="Registro exitoso", fg="green", font=("Calibri", 11)).pack()




    
#------------------------Crearemos una funcion para asignar al boton registro --------------------------------
def registro():
    global usuario
    global contra  #Globalizamos las variables para usarlas en otras funciones
    global usuario_entrada
    global contra_entrada
    global pantalla1
    pantalla1 = Toplevel(pantalla) #Esta pantalla es de un nivel superior a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x450")  #Asignamos el tamaño de la ventana
    
    #--------- Empezaremos a crear las entradas ----------------------------------------
    
    usuario = StringVar()
    contra = StringVar()
    
    Label(pantalla1, text = "Registrarse: debe de asignar un usuario:").pack()
    #Label(pantalla1, text = "").pack()  #Dejamos un poco de espacio
    Label(pantalla1, text = "Registrarse: debe asignar usuario y contraseña:").pack()
    Label(pantalla1, text = "").pack()  #Dejamos un poco de espacio
    Label(pantalla1, text = "Usuario * ").pack()  #Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla1, textvariable = usuario) #Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()
    Label(pantalla1, text = "Contraseña * ").pack()  #Mostramos en la pantalla 1 la contraseña
    contra_entrada = Entry(pantalla1, textvariable = contra) #Creamos un text variable para que el usuario ingrese la contra
    contra_entrada.pack()
    Label(pantalla1, text = "").pack()  #Dejamos un espacio para la creacion del boton
    Button(pantalla1, text = "Registrarse", width = 15, height = 1, command = registrar_usuario).pack()  #Creamos el boton



#------------------------------------------- Funcion para verificar los datos ingresados al login ------------------------------------
def registrar_evento():
    # Obtenemos la información almacenada en las entradas de texto
    nombre_evento_info = nombre_evento.get()
    fecha_info = fecha.get()
    hora_info = hora.get()
    descripcion_info = descripcion.get()

    # Conectamos a la base de datos
    conexion = sqlite3.connect('eventos.db')

    # Creamos una tabla para almacenar los eventos
    conexion.execute('''CREATE TABLE IF NOT EXISTS eventos
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre_evento TEXT NOT NULL,
             fecha TEXT NOT NULL,
             hora TEXT NOT NULL,
             descripcion TEXT NOT NULL);''')

    # Insertamos los datos del evento en la tabla eventos
    conexion.execute(f"INSERT INTO eventos (nombre_evento, fecha, hora, descripcion) VALUES ('{nombre_evento_info}', '{fecha_info}', '{hora_info}', '{descripcion_info}');")

    # Cerramos la conexión a la base de datos
    conexion.commit()
    conexion.close()

    # Limpiamos los text variables
    nombre_evento.delete(0, END)
    fecha.delete(0, END)
    hora.delete(0, END)
    descripcion.delete(0, END)

    # Mostramos un mensaje de éxito
    Label(pantalla3, text="Evento registrado con éxito", fg="green", font=("Calibri", 11)).pack()



def verificacion_login():
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    # Conectamos a la base de datos
    conexion = sqlite3.connect('usuarios.db')

    # Buscamos al usuario en la tabla usuarios
    resultado = conexion.execute(f"SELECT usuario, contrasena FROM usuarios WHERE usuario='{log_usuario}' AND contrasena='{log_contra}';").fetchall()

    # Cerramos la conexión a la base de datos
    conexion.close()

    if len(resultado) > 0:
        print("Inicio de sesión exitoso")
        Label(pantalla2, text="Inicio de sesión exitoso", fg="green", font=("Calibri", 11)).pack()
    else:
        print("Usuario o contraseña incorrectos, ingrese de nuevo")
        Label(pantalla2, text="Usuario o contraseña incorrectos, ingrese de nuevo", fg="red", font=("Calibri", 11)).pack()




#------------------------Funcion que asignaremos al boton login -------------------------------------------------
        
def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2
    
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("300x350")   #Creamos la ventana
    Label(pantalla2, text = "Asignar un usuario:").pack()
    Label(pantalla2, text = "").pack()  #Dejamos un poco de espacio
    
    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()
    
    #---------------------------------- Ingresamos los datos --------------------------
    Label(pantalla2, text = "Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable = verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla2, text = "Contraseña * ").pack()
    contra_entrada2 = Entry(pantalla2, textvariable = verificacion_contra)
    contra_entrada2.pack()
    Label(pantalla2, text = "").pack()
    Button(pantalla2, text = "Inicio de Sesion", width = 20, height = 1, command = verificacion_login).pack()

           
#------------------------- Funcion de nuestra pantalla principal ------------------------------------------------
    
def pantalla_principal():
    global pantalla          #Globalizamos la variable para usarla en otras funciones
    pantalla = Tk()
    pantalla.geometry("400x350")  #Asignamos el tamaño de la ventana 
    pantalla.title("PROYECTO DE GRADO UNAD")       #Asignamos el titulo de la pantalla
    Label(text = "INGRESAR USUARIO", bg = "red", width = "300", height = "2", font = ("Verdana", 13)).pack() #Asignamos caracteristicas de la ventana
    
#------------------------- Vamos a Crear los Botones ------------------------------------------------------
    
    Label(text = "").pack()  #Creamos el espacio entre el titulo y el primer boton
    Button(text = "Iniciar Sesion", height = "2", width = "60", command = login).pack()
    Label(text = "").pack() #Creamos el espacio entre el primer boton y el segundo boton
    Button(text = "Registro", height = "2", width = "60", command = registro).pack()

    pantalla.mainloop()

pantalla_principal()
