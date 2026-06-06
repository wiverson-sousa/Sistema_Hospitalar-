from pydantic import BaseModel
from typing import Optional, List


class ConsultaEntrada(BaseModel):
    paciente_nome: str
    medico_id: int
    data: str
    realizada: bool
    valor: float


class ConsultaSaida(BaseModel):
    id: int
    paciente_nome: str
    medico_id: int
    data: str
    realizada: bool
    valor: float

    model_config = {'from_attributes': True}


class ConsultaEdicao(BaseModel):
    paciente_nome: Optional[str] = None
    medico_id: Optional[int] = None
    data: Optional[str] = None
    realizada: Optional[bool] = None
    valor: Optional[float] = None


class ListaConsultas(BaseModel):
    consultas: List[ConsultaSaida]
