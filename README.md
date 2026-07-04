# Sistema de Gestão de Eventos

API RESTful para criação de eventos e gerenciamento de inscrições com controle de vagas em tempo real.

## 🚀 Tecnologias Utilizadas

* **FastAPI:** Framework moderno e rápido para construção de APIs com Python.
* **SQLAlchemy:** ORM para mapeamento e manipulação do banco de dados de forma segura.
* **SQLite:** Banco de dados relacional leve utilizado para o ambiente de desenvolvimento.
* **Docker:** Containerização da aplicação para garantir consistência entre ambientes.
* **Pydantic:** Validação de dados e tipagem estruturada para as requisições e respostas.

## 🛠️ Como Executar o Projeto

### Opção 1: Via Docker (Recomendado)

Certifique-se de ter o Docker Desktop aberto no seu computador. No terminal da pasta do projeto, execute:

1. Construir a imagem Docker:
```bash
docker build -t sistema-eventos .
## Iniciar o container:
docker run -d -p 8000:8000 sistema-eventos

# Execução Local (Python)

Crie e ative o ambiente virtual:
python -m venv venv
# No Windows:
.\venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Inicie o servidor:
python -m uvicorn app:app --reload


Com o servidor rodando (via Docker ou local), acesse a documentação interativa da API gerada automaticamente pelo FastAPI:

    Swagger UI (Testar as Rotas): http://127.0.0.1:8000/docs
