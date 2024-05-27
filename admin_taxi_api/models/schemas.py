from pydantic import BaseModel, SecretStr, Base64Bytes, ConfigDict
from datetime import date


class SuperUserBase(BaseModel):
    cel: int
    usuario: str


class SuperUserCreate(SuperUserBase):
    password: str


class SuperUser(SuperUserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TaxiBase(BaseModel):
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
    id: int
    placa: str


class AdministradorCreate(AdministradorBase):
    pass


class Administrador(AdministradorBase):

    model_config = ConfigDict(from_attributes=True)


class VisualizadorBase(BaseModel):
    id: int
    placa: str
    permisos: str


class VisualizadorCreate(VisualizadorBase):
    pass


class Visualizador(VisualizadorBase):
    model_config = ConfigDict(from_attributes=True)


class IngresoBase(BaseModel):
    placa: str
    fecha: date
    valor: float


class IngresoCreate(IngresoBase):
    pass


class Ingreso(IngresoBase):
    model_config = ConfigDict(from_attributes=True)


class FacturaBase(BaseModel):
    id_gasto: int
    imagen: Base64Bytes


class FacturaCreate(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GastoBase(BaseModel):
    placa: str
    fecha: date
    valor: float
    tipo: str
    descripcion: str


class GastoCreate(GastoBase):
    pass


class Gasto(GastoBase):
    id_gasto: int
    facturas: list[Factura] = []

    model_config = ConfigDict(from_attributes=True)


class KilometrajeBase(BaseModel):
    placa: str
    fecha: str
    km: str
    estado: bool


class KilometrajeCreate(KilometrajeBase):
    pass


class Kilometraje(KilometrajeBase):
    model_config = ConfigDict(from_attributes=True)


class MantenimientoBase(BaseModel):
    placa: str
    total_km: float
    servicio: str
    vencido: bool


class MantenimientoCreate(MantenimientoBase):
    pass


class Mantenimiento(MantenimientoBase):
    model_config = ConfigDict(from_attributes=True)


class GpsTaxiBase(BaseModel):
    placa: str
    url_aplicacion: str
    usuario: SecretStr
    password: SecretStr


class GpsTaxiCreate(GpsTaxiBase):
    pass


class GpsTaxi(GpsTaxiBase):
    model_config = ConfigDict(from_attributes=True)


class UsuarioBase(BaseModel):
    cel: int
    nombre: str


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int
    administradores: list[Administrador] = []
    visualizadores: list[Visualizador] = []

    model_config = ConfigDict(from_attributes=True)


class Taxi(TaxiBase):

    administradores: list[Administrador] = []
    visualizadores: list[Visualizador] = []
    ingresos: list[Ingreso] = []
    gastos: list[Gasto] = []
    kilometraje: list[Kilometraje] = []
    mantenimientos: list[Mantenimiento] = []
    gps: GpsTaxi

    model_config = ConfigDict(from_attributes=True)
