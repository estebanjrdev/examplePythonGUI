from tkinter import *
from tkinter import messagebox
import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Función para centrar la ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x_ubicacion = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y_ubicacion = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x_ubicacion, y_ubicacion))

# Crear ventana
windows = Tk()
windows.geometry('800x500')
windows.title("GUI para resolver ecuaciones")
# Centrar ventana
centrar_ventana(windows)

# Label
txt = Label(windows,
               text="Sistema para encontrar raíces de una ecuación",
               font=("Arial", 18),
               bg ="yellow",
               fg="pink")
txt.pack(side=TOP, padx=5, pady=10)
a = Label(windows, text="a = ", font=("Arial", 20))
a.place(x= 20,y= 48)
b = Label(windows, text="b = ", font=("Arial", 20))
b.place(x= 20,y= 88)
c = Label(windows, text="c = ", font=("Arial", 20))
c.place(x= 20,y= 128)
x1_label = Label(windows, text="X1 = ?", font=("Arial", 20))
x1_label.place(x= 250,y= 48)
x2_label = Label(windows, text="X2 = ?", font=("Arial", 20))
x2_label.place(x= 250,y= 88)
# Campos de texto
a_entry = Entry(windows, font=("Arial", 20), width=10)
a_entry.place(x=70, y=48)
b_entry = Entry(windows, font=("Arial", 20), width=10)
b_entry.place(x=70, y=88)
c_entry = Entry(windows, font=("Arial", 20), width=10)
c_entry.place(x=70, y=128)
# ecuacion 
def solve_quadratic():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        
        # Calcular el discriminante
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            result = "No tiene soluciones reales"
            messagebox.showinfo(result)
        elif discriminant == 0:
            x = -b / (2*a)
            result = f"Una solución real: x = {x}"
            messagebox.showinfo(result)
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            x1_label.config(text="X1 = "+str(x1))
            x2_label.config(text="X2 = "+str(x2))
          
       
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Button
button = Button(windows, text="Resolver", font=("Arial", 14),command=solve_quadratic)
button.place(x= 250,y= 128)

def graficar():

 global a1,a2,a3,lienzo
 x = np.linspace(-50, 50, 50)
 #y = ecu_cuad(a1, b1, c1, x)
 y = (a1 * x ** 2) + (b1 * x) + c1
 fig = Figure(figsize=(5, 4), dpi=100)
 plot = fig.add_subplot(111)
 plot.plot(x, y)
 plot.axhline(0, color='black', linewidth=0.5)
 plot.axvline(0, color='black', linewidth=0.5)
 plot.grid(color='gray', linestyle='--', linewidth=0.5)
 plot.set_xlabel('x')
 plot.set_ylabel('y')
 if lienzo:
  lienzo.get_tk_widget().destroy() # Destruir el widget anterior si existe
  canvas = FigureCanvasTkAgg(fig, master=ventana)
  lienzo = canvas
  lienzo.get_tk_widget().place(x=200, y=200)

windows.mainloop()
