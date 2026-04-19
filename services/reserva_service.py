from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db
from typing import List

class ReservaService:
    def criar_usuario(nome: str, email: str):
        user = Usuario(id=db.next_usuario_id, nome=nome, email=email)
        db.usuarios[user.id] = user
        db.next_usuario_id += 1
        return user


    def listar_usuarios():
        return List(db.usuarios.values())


    def criar_sala(nome: str, capacidade: int, bloco: str):
        sala = Sala(id=db.next_sala_id, nome=nome, capacidade=capacidade, bloco=bloco)
        db.salas[sala.id] = sala
        db.next_sala_id += 1
        return sala


    def listar_salas():
        return List(db.salas.values())


    def criar_reserva(usuario_id: int, sala_id: int, data: str, hora_inicio: str, hora_fim: str):
        reserva = Reserva(id=db.next_reserva_id, usuario_id=usuario_id, sala_id=sala_id, data=data, hora_inicio=hora_inicio, hora_fim=hora_fim)
        db.reservas[reserva.id] = reserva
        db.next_reserva_id +=1
        return reserva


    def listar_reservas():
        return List(db.reservas.values())


    def listar_reservas_usuario(usuario_id: int):
        return [
            r for r in db.reservas.values()
            if r.usuario_id == usuario_id
        ]

    def buscar_reserva(reserva_id: int):
        reserva = db.reservas.get(reserva_id)
        return reserva


    def cancelar_reserva(reserva_id: int):
        reserva = db.reservas.get(reserva_id)
        reserva.cancelar()
        return reserva

    def finalizar_reserva(reserva_id: int, hora_atual: str):
        reserva = db.reservas.get(reserva_id)
        reserva.finalizar(hora_atual)
        return reserva
    
service = ReservaService()