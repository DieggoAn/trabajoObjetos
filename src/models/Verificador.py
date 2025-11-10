class Autentificador:
    def __init__(self):
        self.rut_usuario = None

    def inicio_sesion(self, rut):
        self.rut_usuario = rut

    def cerrar_sesion(self):
        self.rut_usuario = None

    def obtener_datos(self):
        return {"rut": self.rut_usuario}
       