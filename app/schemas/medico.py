from pydantic import BaseModel
from typing import Optional, List


class MedicoEntrada(BaseModel):
    nome: str
    especialidade: str
    ativo: bool
    salario: float


class MedicoSaida(BaseModel):
    id: int
    nome: str
    especialidade: str
    ativo: bool
    salario: float

    model_config = {'from_attributes': True}


class MedicoEdicao(BaseModel):
    nome: Optional[str] = None
    especialidade: Optional[str] = None
    ativo: Optional[bool] = None
    salario: Optional[float] = None


class ListaMedicos(BaseModel):
    medicos: List[MedicoSaida]
