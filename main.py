from sistema import registrar_cliente, crear_reserva
from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

print("=== SISTEMA SOFTWARE FJ ===")


# OPERACIÓN 1
registrar_cliente(
    "Carlos",
    "carlos@gmail.com",
    "3001234567"
)

# OPERACIÓN 2
registrar_cliente(
    "Lu",
    "correo_invalido",
    "abc"
)

# OPERACIÓN 3
cliente1 = Cliente(
    "Mariana",
    "mariana@gmail.com",
    "3112223344"
)

# OPERACIÓN 4
servicio1 = ReservaSala(
    "Sala Premium",
    100,
    3
)

# OPERACIÓN 5
crear_reserva(cliente1, servicio1)

# OPERACIÓN 6
servicio2 = AlquilerEquipo(
    "Computador Gamer",
    80,
    5
)

# OPERACIÓN 7
crear_reserva(cliente1, servicio2)

# OPERACIÓN 8
servicio3 = AsesoriaEspecializada(
    "Asesoría Python",
    200,
    "alta"
)

# OPERACIÓN 9
crear_reserva(cliente1, servicio3)

# OPERACIÓN 10
try:

    servicio_error = ReservaSala(
        "Sala inválida",
        -100,
        2
    )

except Exception as e:

    print("Error detectado:", e)
    