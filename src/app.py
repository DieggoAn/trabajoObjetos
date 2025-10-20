from controllers.LogUser import *
from controllers.menu_admin import menu_admin


usuario = presentacion_login()

if usuario.rol == "Administrador":
    menu_admin(usuario)