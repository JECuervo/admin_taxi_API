from sqlalchemy.orm import Session
from ..models import models, schemas


def create_user(db: Session, user: schemas.UsuarioCreate):

    db_user = models.Usuario(
        cel=user.cel,
        nombre=user.nombre,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
