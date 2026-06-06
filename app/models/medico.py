from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Medico(Base):
    __tablename__ = 'medicos'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    especialidade: Mapped[str]
    ativo: Mapped[bool]
    salario: Mapped[float]

    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
