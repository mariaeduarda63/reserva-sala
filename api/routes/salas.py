from fastapi import APIRouter
from schemas.sala import SalaCreate, SalaOut

router = APIRouter(prefix="/salas", tags=["Salas"])


@router.post("", response_model="SalaOut")
def criar_sala_route(data: SalaCreate):
    sala = sala(nome=data.nome, capacidade=data.capacidade, bloco=data.bloco)
    db.criar_sala.get(sala)
    return sala


@router.get("", response_model="SalaOut")
def listar_salas_route():
    return db.listar_salas()