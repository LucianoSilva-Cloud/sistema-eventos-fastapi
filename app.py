from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/eventos/", response_model=schemas.EventoResponse)
def criar_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    novo_evento = models.Evento(
        titulo=evento.titulo,
        descricao=evento.descricao,
        vagas_totais=evento.vagas_totais,
        vagas_disponiveis=evento.vagas_totais
    )
    db.add(novo_evento)
    db.commit()
    db.refresh(novo_evento)

    return novo_evento

#Rota
@app.get("/eventos/", response_model=list[schemas.EventoResponse])
def listar_eventos(db: Session = Depends(get_db)):
    eventos = db.query(models.Evento).all()
    return eventos

from fastapi import HTTPException
@app.get("/eventos/{evento_id}", response_model=schemas.EventoResponse)
def buscar_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = db.query(models.Evento).filter(models.Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento

#Rota para comprar ingresso especifico
@app.post("/eventos/{evento_id}/inscricoes/", response_model=schemas.InscricaoResponse)
def criar_inscricao(evento_id: int, inscricao: schemas.InscricaoCreate, db: Session = Depends(get_db)):
    evento = db.query(models.Evento).filter(models.Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    if evento.vagas_disponiveis <= 0:
        raise HTTPException(status_code=400, detail="Não há vagas disponíveis para este evento")

    evento.vagas_disponiveis -= 1
    
    nova_inscricao = models.Inscricao(
        evento_id=evento_id,
        nome_participante=inscricao.nome_participante,
        email_participante=inscricao.email_participante
    )
    db.add(nova_inscricao)
    db.commit()
    db.refresh(nova_inscricao)

    return nova_inscricao