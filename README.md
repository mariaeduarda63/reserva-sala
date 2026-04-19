# API de Reserva de Salas de Estudo

Este projeto tem como objetivo o desenvolvimento de uma API REST para gerenciamento de reservas de salas de estudo.
O sistema deve seguir arquitetura em camadas e respeitar regras de negócio relacionadas a cadastro, reservas, conflitos de horário e cancelamento.


## Objetivo

Construir uma API capaz de:

- Criar usuários
- Listar usuários
- Criar salas
- Listar salas
- Criar reservas
- Listar reservas
- Cancelar reservas
- Finalizar reservas


## Estrutura do Projeto

A aplicação deve seguir a seguinte organização:

salas_api/
├── api/routes/
├── domain/
├── repositories/
├── schemas/
├── services/
└── main.py


## Como rodar o projeto

1. Crie e ative um ambiente virtual:
    - python -m venv venv 
    - source venv/bin/activate # Linux/macOS 
    - venv\Scripts\activate # Windows

2. Instale as dependências:
    - pip install fastapi uvicorn "pydantic[email]"

3. Rode a aplicação:
    - uvicorn main:app --reload

## Endpoints principais
- Usuários
    POST /usuarios → criar usuário
    GET /usuarios → listar usuários

- Salas
    POST /salas → criar sala
    GET /salas → listar salas

- Reservas
    POST /reservas → criar reserva
    GET /reservas → listar reservas
    GET /reservas/usuario/{usuario_id} → listar reserva usuário
    GET /reservas/{reserva_id} → buscar reserva
    PUT /reservas/{reserva_id}/cancelar → cancelar
    PUT /reservas/{reserva_id}/finalizar → finalizar

## Exemplos de payload
- Criar usuário
    {
        "nome": "Ana Souza",
        "email": "ana@email.com"
    }

- Criar sala
    {
        "nome": "Sala 101",
        "capacidade": 6,
        "bloco": "A"
    }

- Criar reserva
    {
        "usuario_id": 1,
        "sala_id": 1,
        "data": "2026-04-20",
        "hora_inicio": "14:00",
        "hora_fim": "15:30"
    }
    
## Tecnologias
- Python
- Fastapi
- Uvicorn
- Pydantic
