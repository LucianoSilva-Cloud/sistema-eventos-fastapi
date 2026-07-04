from pydantic import BaseModel

class EventoCreate(BaseModel):
    titulo: str
    descricao: str
    vagas_totais: int

class EventoResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    vagas_totais: int
    vagas_disponiveis: int
    class Config:
        from_attributes = True

#Esquema preenchimento
class InscricaoCreate(BaseModel):
    nome_participante: str
    email_participante: str

class InscricaoResponse(BaseModel):
    id: int
    evento_id: int
    nome_participante: str
    email_participante: str
    class Config:
        from_attributes = True