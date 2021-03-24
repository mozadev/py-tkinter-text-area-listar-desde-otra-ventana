
'''
grupo 07
MOZA REYES CESAR OSWALDO
TEJADA MORALES TERRY
TERRAZAS HUAMANI JORGE
REYNA MIÑANO RONALDO
QUISPE TICLLASUCA KEVIN

'''


import tkinter

from tkinter import messagebox
import tkinter as tk
from tkinter.font import Font

lista_nombre=[]
lista_apellido=[]
lista_dni=[]

class FrmListado(tkinter.Frame):


    def __init__(self):

        def abrirventana():
            obj_ventana.destroy()
            nuevaventana = FrmLogin()
            nuevaventana.mainloop()

        obj_ventana = tkinter.Tk()
        super().__init__(obj_ventana)
        obj_ventana.title(" Ventana de Listado  !!!!")
        obj_ventana.geometry("400x300")

        e3 = tk.Label(obj_ventana, text='        Listado de Usuario')
        e3.pack(padx=10, pady=5, ipadx=5, ipady=5, fill=tk.X)

        btn_font = Font(family="Roboto Cn", size=14)
        area = tkinter.Text(obj_ventana)
        area.config(width=30, height=10)
        area.place(x=70, y=40)

        boton2 = tk.Button(obj_ventana, bg="silver", text=' Regresar ', font=btn_font, width=12, relief="raised",
                           command=abrirventana)
        boton2.place(x=113, y=230)
        for i in range(len(lista_dni)):

           area.insert(1.0, "\nNombre: "+str(lista_nombre[i]))
           area.insert(1.0, "\nApellido: " + str(lista_apellido[i]))
           area.insert(1.0, "\nDni: "+ str(lista_dni[i]))
           area.insert(1.0, f"\n----------Persona{i + 1}---------")

class FrmRegistro(tkinter.Frame):


    def __init__(self):
        def abrirventana():
            obj_ventana.destroy()
            nuevaventana = FrmLogin()
            nuevaventana.mainloop()

        def GRABAR(nombre, apellido, dni):
            lista_nombre.append(nombre)
            lista_apellido.append(apellido)
            lista_dni.append(dni)

        def grabar():
            messagebox.showinfo(message="Grabado exitósamente", title="Confirmación")

        obj_ventana = tkinter.Tk()
        super().__init__(obj_ventana)
        obj_ventana.title(" Ventana de Registro  !!!!")
        obj_ventana.geometry("400x300")
        apellido = tkinter.StringVar()
        nombre = tkinter.StringVar()
        dni = tkinter.StringVar()

        e3 = tk.Label(obj_ventana, text='        Registro de Usuario'  )
        e3.pack(padx=10, pady=5, ipadx=5, ipady=5, fill=tk.X)
        lblnombre = tkinter.Label(obj_ventana, text="Nombre :")
        lblnombre.place(x=70, y=60)
        self.txtnombre = tkinter.Entry(obj_ventana, width=30,textvariable=nombre)
        self.txtnombre.place(x=150, y=60)
        lblapellido = tkinter.Label(obj_ventana, text="Apellido :")
        lblapellido.place(x=70, y=90)
        self.txtapellido = tkinter.Entry(obj_ventana, width=30,textvariable=apellido)
        self.txtapellido.place(x=150, y=90)
        lbldni = tkinter.Label(obj_ventana, text="Dni :")
        lbldni.place(x=70, y=120)
        self.txtdni = tkinter.Entry(obj_ventana, width=30,textvariable=dni)
        self.txtdni.place(x=150, y=120)
        btn_font = Font(family="Roboto Cn", size=14)
        boton2 = tk.Button(obj_ventana, bg="silver", text=' Regresar ',font=btn_font, width=12, relief="raised", command=abrirventana)
        boton2.place(x=225, y=200)

        button = tk.Button(obj_ventana,
                           text='Grabar', bg="silver",font=btn_font, width=12, relief="raised",
                           command=lambda: [GRABAR(nombre.get(), apellido.get(), dni.get()), grabar()])
        button.place(x=50, y=200)


class FrmLogin(tkinter.Frame):
    def __init__(self):
        global obj_ventana
        obj_ventana = tkinter.Tk()
        super().__init__(obj_ventana)
        obj_ventana.title("Menú de Listado  !!!!")
        obj_ventana.geometry("300x200")
        self.iniciarComponentes()

    def iniciarComponentes(self):
        btn_font = Font(family="Roboto Cn", size=14)
        btnregistrar = tkinter.Button(obj_ventana, text="Registrar", font=btn_font,width=12,relief="raised", command=self.registrar)
        btnregistrar.place(x=80, y=30)
        btnlistar = tkinter.Button(obj_ventana, text="Listar", font=btn_font, width=12, relief="raised",command=self.listar)
        btnlistar.place(x=80, y=100)


    def registrar(self):


        cerrarventana()

        nuevaventana = FrmRegistro()
        nuevaventana.mainloop()
    def listar(self):


        cerrarventana()
        nuevaventana = FrmListado()
        nuevaventana.mainloop()



def cerrarventana():
    obj_ventana.destroy()


objeto = FrmLogin()
objeto.mainloop()