"""
Pydantic Models for database
admin_taxi_api/models/data_base/data_base.sql
"""

from datetime import date
from pydantic import BaseModel, SecretStr, Base64Bytes, ConfigDict


class SuperUserBase(BaseModel):
    """_"""

    cel: int
    usuario: str


class SuperUserCreate(SuperUserBase):
    """_"""

    password: str


class SuperUser(SuperUserBase):
    """_"""

    id: int

    model_config = ConfigDict(from_attributes=True)


class TaxiBase(BaseModel):
    """_"""

    placa: str
    lateral: str
    i_dia_corriente: float
    i_dia_festivo: float
    total_km: float
    inicial_km: float
    km_cambio_aceite: float
    estado: bool
    inicio_admin: date


class AdministradorBase(BaseModel):
    """_"""

    id: int
    placa: str


class AdministradorCreate(AdministradorBase):
    """_"""


class Administrador(AdministradorBase):
    """_"""

    model_config = ConfigDict(from_attributes=True)


class VisualizadorBase(BaseModel):
    """_"""

    id: int
    placa: str
    permisos: str


class VisualizadorCreate(VisualizadorBase):
    """_"""


class Visualizador(VisualizadorBase):
    """_"""

    model_config = ConfigDict(from_attributes=True)


class IngresoBase(BaseModel):
    """_"""

    placa: str
    fecha: date
    valor: float


class IngresoCreate(IngresoBase):
    """_"""


class Ingreso(IngresoBase):
    """_"""

    model_config = ConfigDict(from_attributes=True)


class FacturaBase(BaseModel):
    """_"""

    id_gasto: int
    imagen: Base64Bytes


class FacturaCreate(FacturaBase):
    """_"""


class Factura(FacturaBase):
    """_"""

    id: int
    model_config = ConfigDict(from_attributes=True)


class GastoBase(BaseModel):
    """_"""

    placa: str
    fecha: date
    valor: float
    tipo: str
    descripcion: str


class GastoCreate(GastoBase):
    """_"""


class Gasto(GastoBase):
    """_"""

    id_gasto: int
    facturas: list[Factura] = []

    model_config = ConfigDict(from_attributes=True)


class KilometrajeBase(BaseModel):
    """_"""

    placa: str
    fecha: str
    km: str
    estado: bool


class KilometrajeCreate(KilometrajeBase):
    """_"""


class Kilometraje(KilometrajeBase):
    """_"""

    model_config = ConfigDict(from_attributes=True)


class MantenimientoBase(BaseModel):
    """_"""

    placa: str
    total_km: float
    servicio: str
    vencido: bool


class MantenimientoCreate(MantenimientoBase):
    """_"""


class Mantenimiento(MantenimientoBase):
    """_"""

    model_config = ConfigDict(from_attributes=True)


class GpsTaxiBase(BaseModel):
    """_"""

    placa: str
    url_aplicacion: str
    usuario: SecretStr
    password: SecretStr


class GpsTaxiCreate(GpsTaxiBase):
    """_"""


class GpsTaxi(GpsTaxiBase):
    """_"""

    model_config = ConfigDict(from_attributes=True)


class UsuarioBase(BaseModel):
    """_"""

    cel: int
    nombre: str


class UsuarioCreate(UsuarioBase):
    """_"""


class Usuario(UsuarioBase):
    """_"""

    id: int
    administradores: list[Administrador] = []
    visualizadores: list[Visualizador] = []

    model_config = ConfigDict(from_attributes=True)


class Taxi(TaxiBase):
    """_"""

    administradores: list[Administrador] = []
    visualizadores: list[Visualizador] = []
    ingresos: list[Ingreso] = []
    gastos: list[Gasto] = []
    kilometraje: list[Kilometraje] = []
    mantenimientos: list[Mantenimiento] = []
    gps: GpsTaxi

    model_config = ConfigDict(from_attributes=True)
