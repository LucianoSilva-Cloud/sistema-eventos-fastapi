from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    vagas_totais = Column(Integer)
    vagas_disponiveis = Column(Integer)

    inscricoes = relationship("Inscricao", back_populates="evento")

class Inscricao(Base):
    __tablename__ = "inscricoes"

    id = Column(Integer, primary_key=True, index=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    nome_participante = Column(String)
    email_participante = Column(String)

    evento = relationship("Evento", back_populates="inscricoes")