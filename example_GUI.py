from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Para usar Combobox
import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para centrar la ventana
def window_center(window):
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x_location = (window.winfo_screenwidth() // 2) - (window_width // 2)
    y_location = (window.winfo_screenheight() // 2) - (window_height // 2)
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_location, y_location))

# Crear ventana
windows = Tk()
windows.geometry('1000x600')
windows.resizable(False, False)
windows.title("GUI para resolver ecuaciones")
# Centrar ventana
window_center(windows)
# Label
txt = Label(windows,
            text="Sistema para encontrar raíces de una ecuación",
            font=("Arial", 18),
            bg="yellow",
            fg="pink")
txt.pack(side=TOP, padx=5, pady=10)

# Combobox para seleccionar el tipo de ecuación
equation_type = StringVar()
combobox = ttk.Combobox(windows, textvariable=equation_type, font=("Arial", 14), state="readonly")
combobox['values'] = ("Seleccione la ecuación", "ax² + bx + c = 0", "ax + b = 0")
combobox.current(0)  # Valor por defecto
combobox.place(x=50, y=58)

a_label = Label(windows, text="a = ", font=("Arial", 20))
a_label.place(x=50, y=98)
b_label = Label(windows, text="b = ", font=("Arial", 20))
b_label.place(x=50, y=138)
c_label = Label(windows, text="c = ", font=("Arial", 20))
c_label.place(x=50, y=178)
x1_label = Label(windows, text="", font=("Arial", 20))
x1_label.place(x=450, y=138)
x2_label = Label(windows, text="", font=("Arial", 20))
x2_label.place(x=600, y=138)
txt_type_label = Label(windows, text="Ecuación cuadrática", font=("Arial", 20))
txt_type_label.place_forget()
txt_Equation_label = Label(windows, text="ax² + bx + c = 0", font=("Arial", 20))
txt_Equation_label.place_forget()
# Campos de texto
a_entry = Entry(windows, font=("Arial", 20), width=10, state="disabled")
a_entry.place(x=100, y=98)
b_entry = Entry(windows, font=("Arial", 20), width=10, state="disabled")
b_entry.place(x=100, y=138)
c_entry = Entry(windows, font=("Arial", 20), width=10, state="disabled")
c_entry.place(x=100, y=178)

# Función para habilitar los campos de texto según la opción seleccionada
def enable_fields(event):
    seleccion = equation_type.get()
    if seleccion == "Seleccione la ecuación":
        a_entry.config(state="disabled")
        b_entry.config(state="disabled")
        c_entry.config(state="disabled")
        solve_button.config(state="disabled")
        clean_button.place_forget()
        c_entry.place(x=100, y=178)
        c_label.place(x=50, y=178)
    elif seleccion == "ax² + bx + c = 0":
        a_entry.config(state="normal")
        b_entry.config(state="normal")
        c_entry.config(state="normal")
        solve_button.config(state="normal")
        c_entry.place(x=100, y=178)
        c_label.place(x=50, y=178)
    elif seleccion == "ax + b = 0":
        a_entry.config(state="normal")
        b_entry.config(state="normal")
        c_entry.place_forget()
        c_label.place_forget()
        solve_button.config(state="normal")

combobox.bind("<<ComboboxSelected>>", enable_fields)

# Función para resolver la ecuación
def solve_equation():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get() if c_entry.cget("state") != "disabled" else 0)
        
        if equation_type.get() == "ax² + bx + c = 0":
            # Caso especial: a = 0, tratar como ecuación lineal
            if a == 0:
                if b == 0:
                    result = "No tiene soluciones" if c != 0 else "Infinitas soluciones"
                else:
                    x = -c / b
                    result = "Solución única: x = "+str(x)
                messagebox.showinfo("Resultado", result)
                txt_type_label.config(text="Ecuación lineal (a = 0)")
                txt_type_label.place(x=450, y=58)
                txt_Equation_label.config(text=str(b) + "x + " + str(c) + " = 0")
                txt_Equation_label.place(x=450, y=98)
                combobox.config(state="disabled")
                x1_label.config(text=result)
                x2_label.place_forget()
                graph_linear(b, c)
            else:
                # Resolver ecuación cuadrática
                discriminant = b**2 - 4*a*c
                
                if discriminant < 0:
                    txt_type_label.config(text="Ecuación cuadrática")
                    txt_type_label.place(x=450, y=58)
                    txt_Equation_label.config(text=str(a)+"x² + "+str(b)+"x + "+str(c)+" = 0")
                    txt_Equation_label.place(x=450, y=98)
                    combobox.config(state="disabled")
                    x2_label.place_forget()
                    x1_label.config(text="No tiene soluciones reales")
                elif discriminant == 0:
                    x = -b / (2*a)
                    result = f"Una solución real: x = {x}"
                    messagebox.showinfo("Resultado", result)
                    txt_type_label.config(text="Ecuación cuadrática")
                    txt_type_label.place(x=450, y=58)
                    combobox.config(state="disabled")
                    txt_Equation_label.config(text=str(a)+"x² + "+str(b)+"x + "+str(c)+" = 0")
                    txt_Equation_label.place(x=450, y=98)
                    x1_label.config(text="x = " + str(x))
                    x2_label.place_forget()
                else:
                    x1 = (-b + math.sqrt(discriminant)) / (2*a)
                    x2 = (-b - math.sqrt(discriminant)) / (2*a)
                    txt_type_label.config(text="Ecuación cuadrática")
                    txt_type_label.place(x=450, y=58)
                    combobox.config(state="disabled")
                    txt_Equation_label.config(text=str(a)+"x² + "+str(b)+"x + "+str(c)+" = 0")
                    txt_Equation_label.place(x=450, y=98)
                    x1_label.config(text="x1 = " + str(x1))
                    x2_label.config(text="x2 = " + str(x2))
                graph_quadratic(a, b, c)    
        
        elif equation_type.get() == "ax + b = 0":
            # Resolver ecuación lineal
            if a == 0:
                txt_type_label.config(text="Ecuación lineal")
                txt_type_label.place(x=450, y=58)
                txt_Equation_label.config(text=str(a)+"x + "+str(b)+" = 0")
                txt_Equation_label.place(x=450, y=98)
                combobox.config(state="disabled")
                result = "No tiene soluciones" if b != 0 else "Infinitas soluciones"
                messagebox.showinfo("Resultado", result)
                x1_label.place_forget()
                x2_label.place_forget()
            else:
                x = -b / a
                txt_type_label.config(text="Ecuación lineal")
                txt_type_label.place(x=450, y=58)
                txt_Equation_label.config(text=str(a)+"x + "+str(b)+" = 0")
                txt_Equation_label.place(x=450, y=98)
                combobox.config(state="disabled")
                x1_label.config(text="x = " + str(x))
                x2_label.place_forget()
            graph_linear(a, b)        
            
        clean_button.place(x=150, y=230)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Función para graficar la ecuación cuadrática
def graph_quadratic(a, b, c):
    x = np.linspace(-50, 50, 400)
    y = a * x**2 + b * x + c
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plot.axhline(0, color='black', linewidth=0.5)
    plot.axvline(0, color='black', linewidth=0.5)
    plot.grid(color='gray', linestyle='--', linewidth=0.5)
    plot.set_xlabel('x')
    plot.set_ylabel('y')
    plot.legend()

    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(fig, master=windows)
    canvas.draw()
    canvas.get_tk_widget().place(x=350, y=180)

# Función para graficar la ecuación lineal
def graph_linear(a, b):
    x = np.linspace(-50, 50, 400)
    y = a * x + b
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(x, y, label=f'{a}x + {b}')
    plot.axhline(0, color='black', linewidth=0.5)
    plot.axvline(0, color='black', linewidth=0.5)
    plot.grid(color='gray', linestyle='--', linewidth=0.5)
    plot.set_xlabel('x')
    plot.set_ylabel('y')
    plot.legend()

    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(fig, master=windows)
    canvas.draw()
    canvas.get_tk_widget().place(x=350, y=180)


# Función para limpiar los campos de texto y las etiquetas de resultado
def clean_fields():
    a_entry.delete(0, END)
    b_entry.delete(0, END)
    c_entry.delete(0, END)
    x1_label.config(text="")
    x2_label.config(text="")
    txt_Equation_label.place_forget()
    txt_type_label.place_forget()
    combobox.config(state="readonly")
    combobox.current(0)
    a_entry.config(state="disabled")
    b_entry.config(state="disabled")
    c_entry.config(state="disabled")
    if canvas:
        canvas.get_tk_widget().destroy()
    clean_button.place_forget()
    solve_button.config(state="disabled")

# Inicializar lienzo como None
canvas = None

# Botón
solve_button = Button(windows, text="Resolver", font=("Arial", 14), state="disabled", command=solve_equation)
solve_button.place(x=50, y=230)

clean_button = Button(windows, text="Limpiar", font=("Arial", 14), command=clean_fields)
clean_button.place_forget()

windows.mainloop()
