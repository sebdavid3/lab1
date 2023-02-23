import numpy as np
from tkinter import *
import base as bs

rootProductos = bs.Categoria(id = 10000, name="rootProductos",ruta=["rootProductos"])
rootClientes = bs.Categoria(id = 10000, name="rootClientes",ruta=["rootClientes"])
root = Tk()
root.title("Leve su arbolito personalizado")
root.resizable(TRUE,TRUE)
root.iconbitmap(default="arbolito.ico")
root.geometry("1080x720")

mainFrame = Frame(root)
mainFrame.pack(fill="both", expand=1)
mainFrame.config(bg="#453c5c")

dibujar = Frame(mainFrame)
dibujar.pack(side="left", fill="y")
dibujar.config(bg="#8acbb5", width= 720, height=440,relief="solid" ,borderwidth=2)

datosCliente = Frame(mainFrame)
datosCliente.pack(side="right", fill="y")
datosCliente.config(bg="#c9daa4", width= 720, height=440,relief="solid" ,borderwidth=2)










root.mainloop()