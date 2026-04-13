from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db


def criar_usuario(nome: str, email: str):
    user = usuario(nome.nome, email.email)
    db.criar_usuario(user)
    return user


def listar_usuarios():
    return db.listar_usuarios()


def criar_sala(nome: str, capacidade: int, bloco: str):
    sala = sala(nome.nome, capacidade.capacidade, bloco.bloco)
    db.criar_sala(sala)
    return sala


def listar_salas():
    return db.listar_salas()


def criar_reserva(usuario_id: int, sala_id: int, data: str, hora_inicio: str, hora_fim: str):
    reserva = reserva(usuario_id.usuario_id, sala_id.sala_id, data.data, hora_inicio.hora_inicio, hora_fim.hora_fim)
    db.criar_reserva(reserva)
    return reserva


def listar_reservas():
    return db.listar_reservas()


def listar_reservas_usuario(usuario_id: int):
    return db.listar_reservas_usuario(usuario_id)


def buscar_reserva(reserva_id: int):
    return db.buscar_reserva(reserva_id)


def cancelar_reserva(reserva_id: int):
    return db.cancelar_reserva(reserva_id)


def finalizar_reserva(reserva_id: int, hora_atual: str):
    finalizar = finalizar_reserva(reserva_id.reserva_id, hora_atual.hora_atual)
    db.finalizar_reserva(finalizar)
    return finalizar