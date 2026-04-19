from fastapi import APIRouter
from typing import List
from schemas.sala import SalaCreate, SalaOut
from services.reserva_service import service

router = APIRouter(prefix="/salas", tags=["Salas"])


@router.post("", response_model=SalaOut)
def criar_sala_route(data: SalaCreate):
    sala = service.criar_sala(nome=data.nome, capacidade=data.capacidade, bloco=data.bloco)
    return sala

@router.get("", response_model=List[SalaOut])
def listar_salas_route():
    return service.listar_salas()