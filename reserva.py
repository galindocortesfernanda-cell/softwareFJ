from excepciones import ReservaError


class Reserva:

     def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

     def confirmar(self):

        if self.estado == "Confirmada":
            raise ReservaError("La reserva ya está confirmada")

        self.estado = "Confirmada"

     def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya está cancelada")
        self.estado = "Cancelada"

     def procesar_pago(self):

        try:

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ReservaError("Costo inválido")

            return f"Pago realizado correctamente: ${costo}"

        except Exception as e:
            raise ReservaError("Error al procesar pago") from e

     def mostrar_reserva(self):

        return (
            f"{self.cliente.get_nombre()} - "
            f"{self.servicio.descripcion()} - "
            f"Estado: {self.estado}"
        )