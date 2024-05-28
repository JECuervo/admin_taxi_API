from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Date,
    BLOB,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import relationship
from .data_base.database import Base


class AppAdmin(Base):
    __tablename__ = "app_admin"

    id = Column(Integer, primary_key=True)
    cel = Column(Integer, unique=True)
    usuario = Column(String, unique=True)
    password = Column(String)


class Taxi(Base):
    __tablename__ = "taxis"

    placa = Column(String, primary_key=True)
    lateral = Column(String, unique=True)
    i_dia_corriente = Column(Float)
    i_dia_festivo = Column(Float)
    total_km = Column(Float)
    inicial_km = Column(Float)
    km_cambio_aceite = Column(Float)
    estado = Column(Boolean, ForeignKey("binaria.valor"))
    inicio_admin = Column(Date)

    administradores = relationship("Administrador", back_populates="taxi")
    visualizadores = relationship("Visualizador", back_populates="taxi")
    ingresos = relationship("Ingreso", back_populates="taxi")
    gastos = relationship("Gasto", back_populates="taxi")
    kilometraje = relationship("Kilometraje", back_populates="taxi")
    mantenimientos = relationship("Mantenimiento", back_populates="taxi")
    gps = relationship("GpsTaxi", back_populates="taxi")


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    cel = Column(Integer, unique=True)
    nombre = Column(String)

    administradores = relationship("Administrador", back_populates="usuario")
    visualizadores = relationship("Visualizador", back_populates="usuario")


class Administrador(Base):
    __tablename__ = "administradores"

    id = Column(Integer, ForeignKey("usuarios.id"))
    placa = Column(String, ForeignKey("taxis.placa"))

    __table_args__ = (PrimaryKeyConstraint("id", "placa", name="pk"),)

    taxi = relationship("Taxi", back_populates="administradores")
    usuario = relationship("Usuario", back_populates="administradores")


class Visualizador(Base):
    __tablename__ = "visualizadores"

    id = Column(Integer, ForeignKey("usuarios.id"))
    placa = Column(String, ForeignKey("taxis.placa"))
    permisos = Column(String, ForeignKey("permisos.valor"))

    __table_args__ = (PrimaryKeyConstraint("id", "placa", name="pk"),)

    taxi = relationship("Taxi", back_populates="visualizadores")
    usuario = relationship("Usuario", back_populates="visualizadores")


class Ingreso(Base):
    __tablename__ = "ingresos"

    placa = Column(String, ForeignKey("taxis.placa"))
    fecha = Column(Date)
    valor = Column(Float)

    __table_args__ = (PrimaryKeyConstraint("placa", "fecha", name="pk"),)

    taxi = relationship("Taxi", back_populates="ingresos")


class Gasto(Base):
    __tablename__ = "gastos"

    id_gasto = Column(Integer, primary_key=True)
    placa = Column(String, ForeignKey("taxis.placa"))
    fecha = Column(Date)
    valor = Column(Float)
    tipo = Column(String, ForeignKey("tipos_gastos.tipo"))
    descripcion = Column(String)

    taxi = relationship("Taxi", back_populates="gastos")
    facturas = relationship("Factura", back_populates="gasto")


class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True)
    id_gasto = Column(Integer, ForeignKey("gastos.id_gasto"))
    imagen = Column(BLOB)

    gasto = relationship("Gasto", back_populates="facturas")


class Kilometraje(Base):
    __tablename__ = "kilometraje"

    placa = Column(String, ForeignKey("taxis.placa"))
    fecha = Column(Date)
    km = Column(Float)
    estado = Column(Boolean, ForeignKey("binaria.valor"))

    __table_args__ = (PrimaryKeyConstraint("placa", "fecha", name="pk"),)

    taxi = relationship("Taxi", back_populates="kilometraje")


class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    placa = Column(String, ForeignKey("taxis.placa"))
    total_km = Column(Float)
    servicio = Column(String, primary_key=True)
    vencido = Column(Boolean, ForeignKey("binaria.valor"))

    taxi = relationship("Taxi", back_populates="mantenimientos")


class GpsTaxi(Base):
    __tablename__ = "gps_taxis"

    placa = Column(String, ForeignKey("taxis.placa"), primary_key=True)
    url_aplicacion = Column(String)
    usuario = Column(String)
    password = Column(String)

    taxi = relationship("Taxi", back_populates="gps")
