import tkinter as tk
from tkinter import messagebox, Menu, simpledialog

# Clase Receta para almacenar nombre y lista de ingredientes
class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

# Clase GestorRecetas para gestionar las recetas
class GestorRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        except IndexError:
            return None

# Función para agregar una nueva receta
def agregar_receta():
    nombre = simpledialog.askstring("Agregar receta", "Ingrese el nombre de la receta:")
    ingredientes = simpledialog.askstring("Agregar ingredientes", "Ingrese los ingredientes (separados por coma):")
    
    if nombre and ingredientes:
        gestor.agregar_receta(nombre, ingredientes.split(","))
        listbox_recetas.insert(tk.END, nombre)
        messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente.")

# Función para mostrar los ingredientes de una receta seleccionada
def mostrar_ingredientes(event):
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        receta = gestor.recetas[indice]
        ingredientes = ", ".join(receta.ingredientes)
        messagebox.showinfo(f"Ingredientes de {receta.nombre}", f"{ingredientes}")

# Función para eliminar una receta seleccionada
def eliminar_receta(indice=None):
    if indice is None:
        seleccion = listbox_recetas.curselection()
        if seleccion:
            indice = seleccion[0]
        else:
            messagebox.showwarning("Error", "Seleccione una receta para eliminar.")
            return

    nombre_eliminar = gestor.eliminar_receta(indice)
    if nombre_eliminar:
        listbox_recetas.delete(indice)
        messagebox.showinfo("Receta eliminada", f"La receta '{nombre_eliminar}' ha sido eliminada.")
    else:
        messagebox.showerror("Error", "No se pudo eliminar la receta.")

# Función para manejar el clic derecho
def clic_derecho(event):
    eliminar_receta()

# Función para salir de la aplicación
def salir():
    if messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"):
        ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Recetas")
ventana.geometry("400x400")

# Instancia del gestor de recetas
gestor = GestorRecetas()

# Crear la barra de menú
menu_bar = Menu(ventana)

# Crear un menú de opciones
opciones_menu = Menu(menu_bar, tearoff=0)
opciones_menu.add_command(label="Agregar receta", command=agregar_receta)
opciones_menu.add_command(label="Eliminar receta", command=lambda: eliminar_receta())
opciones_menu.add_separator()  # Separador
opciones_menu.add_command(label="Salir", command=salir)

menu_bar.add_cascade(label="Opciones", menu=opciones_menu)

# Configurar la barra de menú en la ventana principal
ventana.config(menu=menu_bar)

# Etiqueta para el título de recetas
label_titulo = tk.Label(ventana, text="Recetas Agregadas", font=("Arial", 14))
label_titulo.pack(pady=10)

# Listbox para mostrar las recetas guardadas
listbox_recetas = tk.Listbox(ventana, width=50, height=15)
listbox_recetas.pack(padx=10, pady=10)

# Vínculo para mostrar ingredientes al seleccionar la receta
listbox_recetas.bind("<<ListboxSelect>>", mostrar_ingredientes)

# Vínculo para manejar el clic derecho
listbox_recetas.bind("<Button-3>", clic_derecho)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
