from DB.sesion import SessionLocal
from models.modelsDB import User, Clientes, Productos, Proveedores, Pedidos, DetallesPedidos, EstadosPedidos, FechasAbastecimiento
from datetime import datetime, timedelta
import random

def poblar_datos():
    db = SessionLocal()

    # Usuarios
    for i in range(10):
        db.add(User(nombre=f"Usuario{i}", edad=20 + i, correo=f"usuario{i}@correo.com"))

    # Clientes
    for i in range(10):
        db.add(Clientes(
            nombre=f"Cliente{i}",
            email=f"cliente{i}@mail.com",
            telefono=f"555000{i}",
            direccion=f"Calle {i}",
            fecha_registro=datetime.now() - timedelta(days=i),
            pedidos=random.randint(0, 5),
            cliente_frecuente=bool(i % 2)
        ))

    # Proveedores
    for i in range(10):
        db.add(Proveedores(
            nombre=f"Proveedor{i}",
            contacto=f"Contacto{i}",
            telefono=f"555999{i}",
            direccion=f"Zona {i}"
        ))

    # Productos
    for i in range(10):
        db.add(Productos(
            nombre=f"Producto{i}",
            descripcion=f"Descripción del producto {i}",
            precio=round(random.uniform(10, 100), 2),
            stock=random.randint(1, 50),
            categoria_id=random.randint(1, 3),
            proveedor_id=random.randint(1, 10),
            editorial_id=random.randint(1, 5)
        ))

    # EstadosPedidos
    estados = ["Pendiente", "En camino", "Entregado", "Cancelado"]
    for i, estado in enumerate(estados):
        db.add(EstadosPedidos(id=i+1, estado=estado))

    # Pedidos
    for i in range(10):
        db.add(Pedidos(
            cliente_id=random.randint(1, 10),
            fecha=datetime.now() - timedelta(days=random.randint(1, 20)),
            estado_id=random.randint(1, len(estados))
        ))

    # DetallesPedidos
    for i in range(10):
        db.add(DetallesPedidos(
            pedido_id=random.randint(1, 10),
            producto_id=random.randint(1, 10),
            cantidad=random.randint(1, 5),
            precio_unitario=round(random.uniform(10, 100), 2)
        ))

    # FechasAbastecimiento
    for i in range(10):
        db.add(FechasAbastecimiento(
            producto_id=random.randint(1, 10),
            fecha_abastecimiento=datetime.now() - timedelta(days=random.randint(1, 30))
        ))

    db.commit()
    db.close()
