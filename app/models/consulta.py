from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Consulta(Base):
    __tablename__ = 'consultas'

    id: Mapped[int] = mapped_column(primary_key=True)
    paciente_nome: Mapped[str]
    medico_id: Mapped[int]
    data: Mapped[str]
    realizada: Mapped[bool]
    valor: Mapped[float]

    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
