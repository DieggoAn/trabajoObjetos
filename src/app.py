from controllers.LogUser import presentacion_login
from controllers.menu_admin import menu_admin
from controllers.menu_gerente import menu_gerente
from controllers.menu_empleado import menu_empleado


usuario = presentacion_login()

if usuario is not None and usuario.rol == "Administrador":
    menu_admin(usuario)
elif usuario is not None and usuario.rol == "Gerente":
    menu_gerente(usuario)
elif usuario is not None and usuario.rol == "Empleado":
    menu_empleado(usuario)
else:
    pass