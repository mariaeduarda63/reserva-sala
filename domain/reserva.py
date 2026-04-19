from datetime import datetime
class Reserva:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        sala_id: int,
        data: str,
        hora_inicio: str,
        hora_fim: str,
        status: str = "active"
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.sala_id = sala_id
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.status = status

    def cancelar(self):
        self.status = "Cancelado"

    def finalizar(self, hora_atual: str):
        if hora_atual >= self.hora_fim:
            self.status = "Finalizado"

    def duracao_em_horas(self) -> float:
        fmt = "%H:%M"
        inicio = datetime.strptime(self.hora_inicio, fmt)
        fim = datetime.strptime(self.hora_fim, fmt)
        duracao = fim - inicio
        return duracao.total_seconds() / 3600

    def conflita_com(self, outra_reserva) -> bool:
        if self.data != outra_reserva.data:
            return False
        return not (
            self.hora_fim <= outra_reserva.hora_inicio or
            self.hora_inicio >= outra_reserva.hora.fim
        )