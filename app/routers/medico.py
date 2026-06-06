from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.medico import ListaMedicos, MedicoSaida, MedicoEntrada, MedicoEdicao
from app.models.medico import Medico
from app.core.database import get_session

router = APIRouter()


@router.get('/', response_model=ListaMedicos, status_code=status.HTTP_200_OK)
def listar_medicos(session: Session = Depends(get_session)):
    medicos = session.query(Medico).all()
    return {'medicos': medicos}


@router.post('/', response_model=MedicoSaida, status_code=status.HTTP_201_CREATED)
def criar_medico(medico: MedicoEntrada, session: Session = Depends(get_session)):
    novo_medico = Medico(**medico.model_dump())
    session.add(novo_medico)
    session.commit()
    session.refresh(novo_medico)
    return novo_medico


@router.put('/{id_medico}', response_model=MedicoSaida, status_code=status.HTTP_200_OK)
def editar_medico(id_medico: int, medico: MedicoEdicao, session: Session = Depends(get_session)):
    medico_db = session.get(Medico, id_medico)
    if not medico_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Médico não encontrado')

    for campo, valor in medico.model_dump(exclude_unset=True).items():
        setattr(medico_db, campo, valor)

    session.commit()
    session.refresh(medico_db)
    return medico_db


@router.delete('/{id_medico}', status_code=status.HTTP_200_OK)
def deletar_medico(id_medico: int, session: Session = Depends(get_session)):
    medico_db = session.get(Medico, id_medico)
    if not medico_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Médico não encontrado')

    session.delete(medico_db)
    session.commit()
    return {'mensagem': 'Médico removido com sucesso'}
