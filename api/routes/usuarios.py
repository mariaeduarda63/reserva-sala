from fastapi import APIRouter
from schemas.usuario import UsuarioCreate, UsuarioOut

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("", response_model="UsuarioOut")
def criar_usuario_route(data: UsuarioCreate):
    user = usuario(nome=data.nome, email=data.email)
    db.criar_usuario.get(user)
    return user


@router.get("", response_model="UsuarioOut")
def listar_usuarios_route():
    return db.listar_usuarios()
