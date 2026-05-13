from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if precio_base <= 0:
            raise ServicioError("El precio debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):

        super().__init__(nombre, precio_base)

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores que cero")

        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):

        super().__init__(nombre, precio_base)

        if dias <= 0:
            raise ServicioError("Los días deben ser válidos")

        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, nivel):

        super().__init__(nombre, precio_base)

        self.nivel = nivel

    def calcular_costo(self):

        if self.nivel == "alta":
            return self.precio_base * 2

        return self.precio_base

    def descripcion(self):
        return f"Asesoría especializada nivel {self.nivel}"