from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.consulta import ListaConsultas, ConsultaSaida, ConsultaEntrada, ConsultaEdicao
from app.models.consulta import Consulta
from app.core.database import get_session

router = APIRouter()


@router.get('/', response_model=ListaConsultas, status_code=status.HTTP_200_OK)
def listar_consultas(session: Session = Depends(get_session)):
    consultas = session.query(Consulta).all()
    return {'consultas': consultas}


@router.post('/', response_model=ConsultaSaida, status_code=status.HTTP_201_CREATED)
def criar_consulta(consulta: ConsultaEntrada, session: Session = Depends(get_session)):
    nova_consulta = Consulta(**consulta.model_dump())
    session.add(nova_consulta)
    session.commit()
    session.refresh(nova_consulta)
    return nova_consulta


@router.put('/{id_consulta}', response_model=ConsultaSaida, status_code=status.HTTP_200_OK)
def editar_consulta(id_consulta: int, consulta: ConsultaEdicao, session: Session = Depends(get_session)):
    consulta_db = session.get(Consulta, id_consulta)
    if not consulta_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Consulta não encontrada')

    for campo, valor in consulta.model_dump(exclude_unset=True).items():
        setattr(consulta_db, campo, valor)

    session.commit()
    session.refresh(consulta_db)
    return consulta_db


@router.delete('/{id_consulta}', status_code=status.HTTP_200_OK)
def deletar_consulta(id_consulta: int, session: Session = Depends(get_session)):
    consulta_db = session.get(Consulta, id_consulta)
    if not consulta_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Consulta não encontrada')

    session.delete(consulta_db)
    session.commit()
    return {'mensagem': 'Consulta removida com sucesso'}
