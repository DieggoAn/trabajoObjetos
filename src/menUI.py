import tkinter as tk
from tkinter import ttk, messagebox

# --- Plantilla para una Vista Individual (puedes crear muchas de estas) ---
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self):
        self.lift()

class VistaInicio(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = ttk.Label(self, text="Bienvenido al Gestor de Departamentos")
        label.pack(side="top", fill="both", expand=True)

# --- SUB-VISTAS PARA LAS ACCIONES DE DEPARTAMENTO ---

class SubVistaCrearDept(tk.Frame):
    """Frame con el formulario para crear un nuevo departamento."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Crear Nuevo Departamento", font=("Helvetica", 16)).pack(pady=20)
        
        # Aquí va tu formulario: labels, entries y botón de guardar
        ttk.Label(self, text="Nombre:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Label(self, text="Descripción:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Button(self, text="Guardar").pack(pady=20)

class SubVistaModificarDept(tk.Frame):
    """Frame para seleccionar y modificar un departamento existente."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Modificar Departamento", font=("Helvetica", 16)).pack(pady=20)
        
        # Aquí iría una lista desplegable o una tabla para seleccionar el depto a modificar
        ttk.Label(self, text="[Aquí irá la lista de departamentos para seleccionar]").pack()

class SubVistaEliminarDept(tk.Frame):
    """Frame para seleccionar y eliminar un departamento."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Eliminar Departamento", font=("Helvetica", 16)).pack(pady=20)
        
        # Similar a modificar, aquí seleccionas cuál eliminar
        ttk.Label(self, text="[Aquí irá la lista de departamentos para eliminar]").pack()

class VistaDept(Page):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # 1. Marco para los botones de sub-navegación (Crear, Modificar, Eliminar)
        sub_button_frame = ttk.Frame(self)
        sub_button_frame.pack(side="top", fill="x", pady=10, padx=10)

        # 2. Contenedor donde se mostrará la sub-vista activa
        sub_view_container = ttk.Frame(self)
        sub_view_container.pack(side="top", fill="both", expand=True)

        self.sub_views = {}

        # 3. Bucle para crear las sub-vistas y sus botones de forma automática
        for SubViewClass, text in [
            (SubVistaCrearDept, "Crear Departamento"),
            (SubVistaModificarDept, "Modificar Departamento"),
            (SubVistaEliminarDept, "Eliminar Departamento")
        ]:
            # Instancia la sub-vista
            view = SubViewClass(sub_view_container)
            self.sub_views[SubViewClass] = view
            
            # La apila en el contenedor
            view.place(x=0, y=0, relwidth=1, relheight=1)

            # Crea el botón que la mostrará
            button = ttk.Button(sub_button_frame, text=text, command=view.lift)
            button.pack(side="left", padx=5)

        # 4. Muestra la vista de "Crear" por defecto al entrar a esta sección
        self.sub_views[SubVistaCrearDept].lift()

# --- SUB-VISTAS PARA LAS ACCIONES DE EMPLEADO ---

class SubVistaCrearEmp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Crear Nuevo Empleado", font=("Helvetica", 16)).pack(pady=20)
        
        # Aquí va tu formulario: labels, entries y botón de guardar
        ttk.Label(self, text="Nombre:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Label(self, text="Apellido paterno:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Label(self, text="Apellido materno:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Button(self, text="Guardar").pack(pady=20)

class SubVistaModificarEmp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Modificar Empleado", font=("Helvetica", 16)).pack(pady=20)
        
        # Aquí iría una lista desplegable o una tabla para seleccionar el depto a modificar
        ttk.Label(self, text="[Aquí irá la lista de departamentos para seleccionar]").pack()

class SubVistaEliminarEmp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Eliminar empleado", font=("Helvetica", 16)).pack(pady=20)
        
        # Similar a modificar, aquí seleccionas cuál eliminar
        ttk.Label(self, text="[Aquí irá la lista de departamentos para eliminar]").pack()

class VistaEmpleado(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # 1. Marco para los botones de sub-navegación (Crear, Modificar, Eliminar)
        sub_button_frame = ttk.Frame(self)
        sub_button_frame.pack(side="top", fill="x", pady=10, padx=10)

        # 2. Contenedor donde se mostrará la sub-vista activa
        sub_view_container = ttk.Frame(self)
        sub_view_container.pack(side="top", fill="both", expand=True)

        self.sub_views = {}

        # 3. Bucle para crear las sub-vistas y sus botones de forma automática
        for SubViewClass, text in [
            (SubVistaCrearEmp, "Crear Empleado"),
            (SubVistaModificarEmp, "Modificar Empleado"),
            (SubVistaEliminarEmp, "Eliminar Empleado")
        ]:
            # Instancia la sub-vista
            view = SubViewClass(sub_view_container)
            self.sub_views[SubViewClass] = view
            
            # La apila en el contenedor
            view.place(x=0, y=0, relwidth=1, relheight=1)

            # Crea el botón que la mostrará
            button = ttk.Button(sub_button_frame, text=text, command=view.lift)
            button.pack(side="left", padx=5)

        # 4. Muestra la vista de "Crear" por defecto al entrar a esta sección
        self.sub_views[SubVistaCrearEmp].lift()

# --- SUB-VISTAS PARA LAS ACCIONES DE PROYECTO ---

class SubVistaCrearProy(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Crear Nuevo Proyecto", font=("Helvetica", 16)).pack(pady=20)
        
        # Aquí va tu formulario: labels, entries y botón de guardar
        ttk.Label(self, text="Nombre:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Label(self, text="Descripción:").pack(pady=5)
        ttk.Entry(self, width=40).pack()
        ttk.Button(self, text="Guardar").pack(pady=20)

class SubVistaModificarProy(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Modificar Proyecto", font=("Helvetica", 16)).pack(pady=20)
        
        # Aquí iría una lista desplegable o una tabla para seleccionar el depto a modificar
        ttk.Label(self, text="[Aquí irá la lista de proyectos]").pack()

class SubVistaEliminarProy(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="Eliminar Proyecto", font=("Helvetica", 16)).pack(pady=20)
        
        # Similar a modificar, aquí seleccionas cuál eliminar
        ttk.Label(self, text="[Aquí irá la lista de Prote para eliminar]").pack()

class VistaProy(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
            # 1. Marco para los botones de sub-navegación (Crear, Modificar, Eliminar)
        sub_button_frame = ttk.Frame(self)
        sub_button_frame.pack(side="top", fill="x", pady=10, padx=10)

        # 2. Contenedor donde se mostrará la sub-vista activa
        sub_view_container = ttk.Frame(self)
        sub_view_container.pack(side="top", fill="both", expand=True)

        self.sub_views = {}

        # 3. Bucle para crear las sub-vistas y sus botones de forma automática
        for SubViewClass, text in [
            (SubVistaCrearProy, "Crear Proyecto"),
            (SubVistaModificarProy, "Modificar Proyecto"),
            (SubVistaEliminarProy, "Eliminar Proyecto")
        ]:
            # Instancia la sub-vista
            view = SubViewClass(sub_view_container)
            self.sub_views[SubViewClass] = view
            
            # La apila en el contenedor
            view.place(x=0, y=0, relwidth=1, relheight=1)

            # Crea el botón que la mostrará
            button = ttk.Button(sub_button_frame, text=text, command=view.lift)
            button.pack(side="left", padx=5)

        # 4. Muestra la vista de "Crear" por defecto al entrar a esta sección
        self.sub_views[SubVistaCrearProy].lift()


# --- Estructura Principal de la Aplicación ---
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        # Contenedor para los botones de navegación
        button_frame = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        
        # Contenedor donde se mostrarán las vistas (páginas)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        views_to_create = [
            (VistaInicio, "Inicio"),
            (VistaDept, "Gestion departamentos"),
            (VistaEmpleado, "Gestion empleados"),
            (VistaProy, "Gestion proyectos")
        ]
        
        self.views = {} # Use a dictionary to store the created view instances

        for ViewClass, text in views_to_create:

            view = ViewClass(container)
            
            self.views[ViewClass] = view
            
            view.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            
            button = ttk.Button(button_frame, text=text, command=view.show)
            button.pack(side="left", padx=5, pady=5)

        initial_view = self.views[VistaInicio]
        initial_view.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Gestión de Departamentos")
    root.geometry("500x300")
    
    # Usar un tema más moderno
    style = ttk.Style()
    style.theme_use('clam') # Puedes probar 'alt', 'default', 'classic', 'vista'

    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()