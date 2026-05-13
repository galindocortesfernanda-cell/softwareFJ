from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, correo, telefono):

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar()

    def validar(self):

        if len(self.__nombre.strip()) < 3:
            raise ClienteError("El nombre del cliente es inválido")

        if "@" not in self.__correo:
            raise ClienteError("Correo inválido")

        if not self.__telefono.isdigit():
            raise ClienteError("El teléfono debe contener solo números")

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def mostrar_cliente(self):

        return f"Cliente: {self.__nombre} - {self.__correo}"
        