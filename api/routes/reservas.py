from fastapi import APIRouter
from typing import List
from schemas.reserva import ReservaCreate, ReservaOut
from services.reserva_service import service

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("", response_model=ReservaOut)
def criar_reserva_route(data: ReservaCreate):
    reserva = service.criar_reserva(usuario_id=data.usuario_id, sala_id=data.sala_id, data=data.data, hora_inicio=data.hora_inicio, hora_fim=data.hora_fim)
    return reserva


@router.get("", response_model=List[ReservaOut])
def listar_reservas_route():
    return service.listar_reservas()


@router.get("/usuario/{usuario_id}", response_model=List[ReservaOut])
def listar_reservas_usuario_route(usuario_id: int):
    return service.listar_reservas_usuario(usuario_id)


@router.get("/{reserva_id}", response_model=ReservaOut)
def buscar_reserva_route(reserva_id: int):
    return service.buscar_reserva(reserva_id)


@router.put("/{reserva_id}/cancelar", response_model=ReservaOut)
def cancelar_reserva_route(reserva_id: int):
    return service.cancelar_reserva(reserva_id)


@router.put("/{reserva_id}/finalizar", response_model=ReservaOut)
def finalizar_reserva_route(reserva_id: int, hora_atual: str):
    finalizar = service.finalizar_reserva(reserva_id, hora_atual)
    return finalizar