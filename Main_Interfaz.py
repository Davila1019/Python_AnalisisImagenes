from tkinter import messagebox, ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Histograma.Histograma import Histograma
from tkinter import filedialog
from PIL import ImageTk, Image
from Espacial.Espacial import Espacial

import tkinter as tk
import matplotlib.pyplot as plt
import cv2
import numpy as np


class Main_Interfaz:
    
    def __init__(self):
        self.root = tk.Tk()
        self.radio_frame = ttk.Frame(self.root, padding=10)
        self.plt = plt
        self.figure = self.plt.figure(figsize=(5,4))
        self.ax = self.figure.add_subplot(111)
        self.var_check = tk.StringVar()
        self.var_combo = tk.StringVar()
        self.frame_grafica = ttk.Frame(self.root, padding=10)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame_grafica)
        self.frame_imagen = ttk.Label(master=self.root)
        self.frame_imagen_filtro = ttk.Label(master=self.root)
        self.slide1 = tk.Scale(self.root, from_=0, to=255, orient=tk.HORIZONTAL)
        self.slide2 = tk.Scale(self.root, from_=0, to=255, orient=tk.HORIZONTAL)
        self.hist = None
        self.configurarInterfaz()

    def configurarInterfaz(self):
        options = ['Umbralización', 'Opción 2', 'Opción 3']
        ttk.Button(self.root, text="Abrir archivo", command=self.abrirArchivo).grid(row=0,column=0)
        ttk.Label(self.radio_frame,text="Selecciona el histograma").grid(row=0,column=3)
        ttk.Radiobutton(self.radio_frame, text="RGB",variable=self.var_check ,command=lambda: self.actualizarFrame(), value="1").grid(row=1, column=0)
        ttk.Radiobutton(self.radio_frame, text="Blue",variable=self.var_check ,command=lambda: self.actualizarFrame(), value="2").grid(row=1, column=1)
        ttk.Radiobutton(self.radio_frame, text="Green",variable=self.var_check ,command=lambda: self.actualizarFrame(), value="3").grid(row=1, column=2)
        ttk.Radiobutton(self.radio_frame, text="Red",variable=self.var_check ,command=lambda: self.actualizarFrame(), value="4").grid(row=1, column=3)
        ttk.Radiobutton(self.radio_frame, text="Gray",variable=self.var_check ,command=lambda: self.actualizarFrame(), value="5").grid(row=1, column=4)
        ttk.Combobox(self.root, textvariable=self.var_combo,values=options, state="readonly").grid(row=0, column=5)
        ttk.Button(self.root, text="Mostrar controles", command=self.actualizarControles).grid(row=1,column=5)
        self.radio_frame.grid(row=1,column=0)
        self.frame_grafica.grid(row=2,column=0, columnspan=1)
        self.frame_imagen.grid(row=2,column=1, columnspan=1)
        self.frame_imagen_filtro.grid(row=2,column=2, columnspan=1)
        self.canvas.get_tk_widget().pack()
        self.root.mainloop()
        
    def actualizarFrame(self):
        value = self.var_check.get()
        x = np.arange(256)
        try:
            if value == "1":
                y1 = self.hist.get_hist_b()
                y2 = self.hist.get_hist_g()
                y3 = self.hist.get_hist_r()
                self.ax.clear()
                self.ax.plot(x, y1, color='blue')
                self.ax.plot(x, y2, color='green')
                self.ax.plot(x, y3, color='red')
            elif value == "2":
                y = self.hist.get_hist_b()
                self.ax.clear()
                self.ax.plot(x, y, color='blue')
            elif value == "3":
                y = self.hist.get_hist_g()
                self.ax.clear()
                self.ax.plot(x, y, color='green')
            elif value == "4":
                y = self.hist.get_hist_r()
                self.ax.clear()
                self.ax.plot(x, y, color='red')
            elif value == "5":
                y = self.hist.get_hist_gray()
                self.ax.clear()
                self.ax.plot(x, y, color='gray')
        #Actualizar la gráfica en la interfaz
            self.canvas.draw()
        except:
            messagebox.showerror("Error", "Aún no haz abierto algún archivo!!!!")
            self.abrirArchivo()
        
    def abrirArchivo(self):
        try:
            dirimage = filedialog.askopenfilename(title="Abrir archivo",
                                            initialdir="C:Documents/")
            
            self.image = cv2.imread(dirimage)
            self.hist = Histograma(self.image)
            self.hist.calcularHistogramas()
            self.actualizarImagen(dirimage)
            self.actualizarFrame()
        except FileNotFoundError:
            messagebox.showerror("El archivo que seleccionaste no existe o está dañado")
            
    def actualizarImagen(self,dirimage):
        img_frame = Image.open(dirimage)
        img_frame = img_frame.resize((250, 250))
        img_frame = ImageTk.PhotoImage(img_frame)
        self.frame_imagen.config(image=img_frame)
        self.frame_imagen.image = img_frame   
       
    def atualizarImagenFiltro(self,u1,u2):
        esp = Espacial(self.image)
        u1 = (int)(u1)
        u2 = (int)(u2)
        if u1 < u2:
            img_seg = esp.segmentarImagen(u1,u2)
            img_frame_seg = img_seg.resize((250, 250))
            img_frame_seg = ImageTk.PhotoImage(img_frame_seg)
            self.frame_imagen_filtro.config(image=img_frame_seg)
            self.frame_imagen_filtro.image = img_frame_seg  
                
    def actualizarControles(self):
        option = self.var_combo.get()
        if option == 'Umbralización':
            ttk.Label(self.root,text="Umbral 1").grid(row=3,column=5)
            self.slide1.config(command=lambda val: self.atualizarImagenFiltro(val, self.slide2.get()))
            self.slide1.grid(row=4,column=5)
            ttk.Label(self.root,text="Umbral 2").grid(row=5,column=5)
            self.slide2.config(command=lambda val: self.atualizarImagenFiltro(self.slide1.get(), val))
            self.slide2.grid(row=6,column=5)
        
    
if __name__ == "__main__":
    main = Main_Interfaz()
