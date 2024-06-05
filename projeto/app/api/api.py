from app.services.weather_service import obter_dados_climaticos
from fastapi import APIRouter, HTTPException, Query
from app.domain.models import DadoClimatico

router = APIRouter()

@router.post("/dados-climaticos/", response_model=DadoClimatico)
async def coletar_dados_climaticos(localizacao: str = Query(..., description="Localização no formato Cidade,País")):
    dados_climaticos = obter_dados_climaticos(localizacao)
    if not dados_climaticos:
        raise HTTPException(status_code=404, detail="Localização não encontrada.")
    
    return dados_climaticos

@router.get("/dados-climaticos/")
async def listar_dados_climaticos(page: int = Query(1, gt=0), limit: int = Query(10, gt=0, le=100)):
    # Implementar a logica aqui
    
    return {"message": f"Listando dados climáticos da página {page} com limite {limit}"}
    