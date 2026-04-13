from fastapi import APIRouter
from schemas.reserva import ReservaCreate, ReservaOut

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("", response_model="ReservaOut")
def criar_reserva_route(data: ReservaCreate):
    reserva = reserva(usuario_id=data.usuario_id, sala_id=data.sala_id, data=data.data, hora_inicio=data.hora_inicio, hora_fim=data.hora_fim)
    db.criar_reserva.get(reserva)
    return reserva


@router.get("", response_model="ReservaOut")
def listar_reservas_route():
    return db.listar_reservas.get()


@router.get("/usuario/{usuario_id}")
def listar_reservas_usuario_route(usuario_id: int):
    return db.listar_reservas_usuario.get(usuario_id)


@router.get("/{reserva_id}")
def buscar_reserva_route(reserva_id: int):
    return db.buscar_reserva.get()


@router.put("/{reserva_id}/cancelar")
def cancelar_reserva_route(reserva_id: int):
    return db.cancelar_reserva.get(reserva_id)


@router.put("/{reserva_id}/finalizar")
def finalizar_reserva_route(reserva_id: int, hora_atual: str):
    finalizar = finalizar_reserva(reserva_id.reserva_id, hora_atual.hora_atual, finalizar.finalizar)
    db.finalizar_reserva(finalizar)
    return finalizar