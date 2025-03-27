import tkinter as tk
from tkinter import messagebox, ttk

libros = []

def idEx(id):
    if not id.isdigit():
        messagebox.showerror("Error", "ID debe ser un número entero")
        return False
    for libro in libros:
        if libro['id'] == id:
            return True
    return False


def buscarLibro():
    idBuscar = txBuscar.get()
    for libro in libros:
        if libro['id'] == idBuscar:
            txId.config(state='normal')
            txTitulo.config(state='normal')
            txAutor.config(state='normal')
            txEditorial.config(state='normal')
            cbClasificacion.config(state='normal')
            txId.delete(0, tk.END)
            txTitulo.delete(0, tk.END)
            txAutor.delete(0, tk.END)
            txEditorial.delete(0, tk.END)
            txId.insert(tk.END, libro['id'])
            txTitulo.insert(tk.END, libro['titulo'])
            txAutor.insert(tk.END, libro['autor'])
            txEditorial.insert(tk.END, libro['editorial'])
            cbClasificacion.set(libro['clasificacion'])
            btnEditar.config(state='normal')
            btnEliminar.config(state='normal')
            txId.config(state='disabled')
            txId.delete(0, tk.END) 
            break


def nuevoL():
    limpiar()
    txId.config(state='normal')
    txTitulo.config(state='normal')
    txAutor.config(state='normal')
    txEditorial.config(state='normal')
    cbClasificacion.config(state='normal')
    txId.delete(0, tk.END)
    txTitulo.delete(0, tk.END)
    txAutor.delete(0, tk.END)
    txEditorial.delete(0, tk.END)
    txId.insert(tk.END, len(libros) + 1)
    txId.config(state='disabled') 
     
    btnNuevo.config(state='disabled')
    btnGuardar.config(state='normal')
    btnCancelar.config(state='normal')

def guardarL():
    id = txId.get()
    titulo = txTitulo.get()
    autor = txAutor.get()
    editorial = txEditorial.get()
    clasificacion = cbClasificacion.get()
    
    opciones_clasificacion = ["Novela", "Cuento", "Finanzas", "Economia", "Historia", "Geografia", "Ciencia", "Tecnologia", "Matematicas", "Biologia", "Quimica", "Fisica", "Arte", "Musica", "Deporte", "Fantasia", "Aventura", "Terror", "Suspenso", "Romance", "Drama", "Comedia", "Infantil", "Juvenil", "Adulto"]
    
    if not id or not titulo or not autor or not editorial or not clasificacion:
        messagebox.showerror("Error", "Deben estar todos los datos")
    elif not titulo.isalpha() or not autor.isalpha() or not editorial.isalpha():
        messagebox.showerror("Error", "El título, autor y editorial solo deben contener caracteres alfabéticos")
    elif clasificacion not in opciones_clasificacion:
        messagebox.showerror("Error", "La clasificación debe ser una de las siguientes opciones: " + ", ".join(opciones_clasificacion))
    elif idEx(id):
        messagebox.showerror("Error", "ID ya existe")
    else:
        libros.append({
            'id': id,
            'titulo': titulo,
            'autor': autor,
            'editorial': editorial,
            'clasificacion': clasificacion
        })
        limpiar()
        btnNuevo.config(state='normal')
        btnGuardar.config(state='disabled')
        btnCancelar.config(state='disabled')
        txId.config(state='normal') 
        txId.delete(0, tk.END)
        txId.config(state='disabled') 
        


def cancelar():
    limpiar()
    btnNuevo.config(state='normal')

def editarL():
    idEditar = txId.get()
    titulo = txTitulo.get()
    autor = txAutor.get()
    editorial = txEditorial.get()
    clasificacion = cbClasificacion.get()
    
    opciones_clasificacion = ["Novela", "Cuento", "Finanzas", "Economia", "Historia", "Geografia", "Ciencia", "Tecnologia", "Matematicas", "Biologia", "Quimica", "Fisica", "Arte", "Musica", "Deporte", "Fantasia", "Aventura", "Terror", "Suspenso", "Romance", "Drama", "Comedia", "Infantil", "Juvenil", "Adulto"]
    
    if not idEditar or not titulo or not autor or not editorial or not clasificacion:
        messagebox.showerror("Error", "Deben estar todos los datos")
    elif not titulo.isalpha() or not autor.isalpha() or not editorial.isalpha():
        messagebox.showerror("Error", "El título, autor y editorial solo deben contener caracteres alfabéticos")
    elif clasificacion not in opciones_clasificacion:
        messagebox.showerror("Error", "La clasificación debe ser una de las siguientes opciones: " + ", ".join(opciones_clasificacion))
    else:
        for libro in libros:
            if libro['id'] == idEditar:
                libro['titulo'] = titulo
                libro['autor'] = autor
                libro['editorial'] = editorial
                libro['clasificacion'] = clasificacion
                break
        limpiar()
        btnNuevo.config(state='normal')
        txId.config(state='normal') 
        txId.delete(0, tk.END)
        txId.config(state='disabled') 


def eliminarL():
    id_eliminar = txId.get()
    for libro in libros:
        if libro['id'] == id_eliminar:
            libros.remove(libro)
            break
    limpiar()
    btnNuevo.config(state='normal')

def limpiar():
    txId.delete(0, tk.END)
    txTitulo.delete(0, tk.END)
    txAutor.delete(0, tk.END)
    txEditorial.delete(0, tk.END)
    cbClasificacion.set('')
    txId.config(state='disabled')
    txTitulo.config(state='disabled')
    txAutor.config(state='disabled')
    txEditorial.config(state='disabled')
    cbClasificacion.config(state='disabled')
    btnEditar.config(state='disabled')
    btnEliminar.config(state='disabled')

root = tk.Tk()
root.config(width=500, height=400)
root.title("Biblioteca")
root.configure(bg='black')

tk.Label(root, text="Buscar ID:", bg='black', fg='gold').place(x=250, y=10)
txBuscar = tk.Entry(root)
txBuscar.place(x=360, y=10)

btnBuscar = tk.Button(root, text="Buscar", command=buscarLibro, bg='gold')
btnBuscar.place(x=310, y=10)

tk.Label(root, text="ID:", bg='black', fg='gold').place(x=10, y=10)
txId = tk.Entry(root, state='disabled')
txId.place(x=10, y=30)

tk.Label(root, text="Titulo Libro", bg='black', fg='gold').place(x=10, y=50)
txTitulo = tk.Entry(root, width=30, state='disabled')
txTitulo.place(x=10, y=70)

tk.Label(root, text="Autor", bg='black', fg='gold').place(x=10, y=90)
txAutor = tk.Entry(root, width=30, state='disabled')
txAutor.place(x=10, y=110)

tk.Label(root, text="Editorial", bg='black', fg='gold').place(x=10, y=130)
txEditorial = tk.Entry(root, width=30, state='disabled')
txEditorial.place(x=10, y=150)

tk.Label(root, text="Clasificacion:", bg='black', fg='gold').place(x=10, y=170)
cbClasificacion = ttk.Combobox(root, state='disabled', values=["Novela", "Cuento", "Finanzas", "Economia", "Historia", "Geografia", "Ciencia", "Tecnologia", "Matematicas", "Biologia", "Quimica", "Fisica", "Arte", "Musica", "Deporte", "Fantasia", "Aventura", "Terror", "Suspenso", "Romance", "Drama", "Comedia", "Infantil", "Juvenil", "Adulto"])
cbClasificacion.place(x=10, y=190)

# Los +10 son para ajustar la distancia por que de tanto movedero que estaba haciendo ya me estaba perdiendo al modificarlos, por lo que mejor aumente sumandole ya con el +
btnNuevo = tk.Button(root, text="Nuevo", command=nuevoL, bg='gold')
btnNuevo.place(x=150+10, y=220)

btnGuardar = tk.Button(root, text="Guardar", state='disabled', command=guardarL, bg='gold')
btnGuardar.place(x=200+10, y=220)

btnCancelar = tk.Button(root, text="Cancelar", state='disabled', command=cancelar, bg='gold')
btnCancelar.place(x=257+10, y=220)

btnEditar = tk.Button(root, text="Editar", state='disabled', command=editarL, bg='gold')
btnEditar.place(x=317+10, y=220)

btnEliminar = tk.Button(root, text="Eliminar", state='disabled', command=eliminarL, bg='gold')
btnEliminar.place(x=360+10, y=220)

root.mainloop()