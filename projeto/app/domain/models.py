from pydantic import BaseModel
from typing import Optional
from enum import Enum  


class Localizacao(BaseModel):
    latitude: float
    longitude: float
    
class EstacaoClimatica(BaseModel):
    id: Optional[int]
    nome: str
    localzacao: Localizacao
    
class DadoClimatico(BaseModel):
    id: Optional[int]
    data_hora: str
    estacao: EstacaoClimatica
    temperatura: float
    umidade: int
    velocidade_vento: float
    direcao_vento: str

class CondicaoClimatica(str, Enum):
    ENSOLARADO = "Ensolarado"
    PARCIALMENTE_NUBLADO = "Parcialmente Nublado"
    NUBLADO = "Nublado"
    CHUVOSO = "Chuvoso"
    TEMPESTUOSO = "Tempestuoso"
    