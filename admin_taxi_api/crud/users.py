from sqlalchemy.orm import Session
from ..models import models, schemas


def create_usuario(db: Session, user: schemas.UsuarioCreate) -> models.Usuario:

    db_user = models.Usuario(
        cel=user.cel,
        nombre=user.nombre,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def create_administrador(
    db: Session, admin: schemas.AdministradorCreate
) -> models.Administrador:

    db_admin = models.Administrador(id=admin.id, placa=admin.placa)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return db_admin
