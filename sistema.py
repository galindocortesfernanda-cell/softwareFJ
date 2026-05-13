from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva

from excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)

import logging


logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


clientes = []
reservas = []


def registrar_cliente(nombre, correo, telefono):

    try:

        cliente = Cliente(nombre, correo, telefono)

    except ClienteError as e:

        logging.error(e)

        print("Error en cliente:", e)

    else:

        clientes.append(cliente)

        print("Cliente registrado correctamente")


def crear_reserva(cliente, servicio):

    try:

        reserva = Reserva(cliente, servicio)

        reserva.confirmar()

        print(reserva.procesar_pago())

        reservas.append(reserva)

    except ReservaError as e:

        logging.error(e)

        print("Error en reserva:", e)

    finally:

        print("Proceso de reserva finalizado")
        