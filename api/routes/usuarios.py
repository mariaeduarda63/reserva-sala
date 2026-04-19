from fastapi import APIRouter
from typing import List
from schemas.usuario import UsuarioCreate, UsuarioOut
from services.reserva_service import service

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("", response_model=UsuarioOut)
def criar_usuario_route(data: UsuarioCreate):
    user = service.criar_usuario(nome=data.nome, email=data.email)
    return user

@router.get("", response_model=List[UsuarioOut])
def listar_usuarios_route():
    return service.listar_usuarios()
