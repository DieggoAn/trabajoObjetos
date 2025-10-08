from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico):
        
        self.nombres = nombres
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.direccion = direccion
        self.fechaNacimiento = fechaNacimiento
        self.fechaInicioContrato = fechaInicioContrato
        self.salario = salario
        self.numeroTelefonico = numeroTelefonico

    def __str__(self):
        return (f"Los datos son los siguientes:\n"
                f"Nombres: {self.nombres}\n"
                f"Apellido paterno: {self.apellidoPaterno}\n"
                f"Apellido materno: {self.apellidoMaterno}\n"
                f"Dirección: {self.direccion}\n"
                f"Fecha de nacimiento: {self.fechaNacimiento}\n"
                f"Fecha de inicio del contrato: {self.fechaInicioContrato}\n"
                f"Salario: {self.salario}\n"
                f"Número telefónico: {self.numeroTelefonico}")

    @abstractmethod
    def mostrar_rol(self):
        pass