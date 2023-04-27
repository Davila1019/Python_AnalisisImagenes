import cv2
import matplotlib.pyplot as plt
import numpy as np

class Histograma:
    
    
    def __init__(self,image):
        self.plt = plt
        self.image = image
        self.hist_b = None
        self.hist_g = None
        self.hist_r = None
        self.hist_gray = None
        self.pix = np.arange(256)
        
    
    def calcularHistogramas(self):    
        img = cv2.split(self.image)
        self.hist_b = cv2.calcHist(img,[0],None,[256],[0,255])
        self.hist_g = cv2.calcHist(img,[1],None,[256],[0,255])
        self.hist_r = cv2.calcHist(img,[2],None,[256],[0,255])
        img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.hist_gray = cv2.calcHist(img_gray,[0],None,[256],[0,255])
        
    def get_hist_b(self):
        return self.hist_b
    
    def get_hist_g(self):
        return self.hist_g
    
    def get_hist_r(self):
        return self.hist_r
    
    def get_hist_gray(self):
        return self.hist_gray
        
    def graficarHistogramaRGB(self):
        fig, ax1 = self.plt.subplots()
        ax1.plot(self.pix,self.hist_b , 'b')
        ax2 = ax1.twinx()
        ax2.plot(self.pix,self.hist_g , 'g')
        ax3 = ax2.twinx()
        ax3.plot(self.pix,self.hist_r , 'r')
        print("Nada")
    
    def graficarHistBlue(self):
        fig, ax1 = self.plt.subplots()
        ax1.plot(self.pix,self.hist_b , 'b')
        
    
    def graficarHistGreen(self):
        fig, ax1 = self.plt.subplots()
        ax1.plot(self.pix,self.hist_g , 'g')
        
    
    def graficarHistRed(self):
        fig, ax1 = self.plt.subplots()
        ax1.plot(self.pix,self.hist_r , 'r')
    
    def graficarHistGray(self):
        fig, ax1 = self.plt.subplots()
        ax1.plot(self.pix,self.hist_gray, 'k')
     
    def mostrarHistogramas(self):
        self.plt.show()   
       