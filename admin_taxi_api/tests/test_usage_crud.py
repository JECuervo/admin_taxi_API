from sqlalchemy.exc import IntegrityError

from ..models import models, schemas
from ..crud import users
from .resources.database import SessionLocal


DB = SessionLocal()


def test_create_usuario():

    user = schemas.UsuarioCreate(cel=3000000000, nombre="Carlos Mario")
    user_db = users.create_usuario(DB, user)

    assert user_db.id == 3
    assert True


def test_create_administrador():

    admin = schemas.AdministradorCreate(id=3, placa="TFH043")
    try:
        users.create_administrador(DB, admin)
        assert False

    except IntegrityError:
        DB.rollback()
        assert True

    admin = schemas.AdministradorCreate(id=3, placa="BBB111")
    admin_db = users.create_administrador(DB, admin)

    assert admin_db.taxi.placa == "BBB111"
    assert True
