from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db

class ReservaService:
    def criar_usuario(self,nome: str, email: str):
        user = Usuario(id=db.next_usuario_id, nome=nome, email=email)
        db.usuarios[user.id] = user
        db.next_usuario_id += 1
        return user


    def listar_usuarios(self):
        return list(db.usuarios.values())


    def criar_sala(self,nome: str, capacidade: int, bloco: str):
        sala = Sala(id=db.next_sala_id, nome=nome, capacidade=capacidade, bloco=bloco)
        db.salas[sala.id] = sala
        db.next_sala_id += 1
        return sala


    def listar_salas(self):
        return list(db.salas.values())


    def criar_reserva(self, usuario_id: int, sala_id: int, data: str, hora_inicio: str, hora_fim: str):
        reserva = Reserva(id=db.next_reserva_id, usuario_id=usuario_id, sala_id=sala_id, data=data, hora_inicio=hora_inicio, hora_fim=hora_fim)
        db.reservas[reserva.id] = reserva
        db.next_reserva_id +=1
        return reserva


    def listar_reservas(self):
        return list(db.reservas.values())


    def listar_reservas_usuario(self, usuario_id: int):
        return [
            r for r in db.reservas.values()
            if r.usuario_id == usuario_id
        ]

    def buscar_reserva(self, reserva_id: int):
        reserva = db.reservas.get(reserva_id)
        return reserva


    def cancelar_reserva(self, reserva_id: int):
        reserva = db.reservas.get(reserva_id)
        reserva.cancelar()
        return reserva

    def finalizar_reserva(self, reserva_id: int, hora_atual: str):
        reserva = db.reservas.get(reserva_id)
        reserva.finalizar(hora_atual)
        return reserva
    
service = ReservaService()