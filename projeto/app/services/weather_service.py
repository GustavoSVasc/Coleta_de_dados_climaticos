import requests
from app.domain.models import DadoClimatico, EstacaoClimatica

def obter_dados_climaticos(localizacao: str):
    app_key = "6ddfa73781ed9e02957b12b224d7b20f"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": localizacao,
        "appid": app_key,
        "units": "metric"
    }
    
    resposta = requests.get(base_url, params=parametros)
    if resposta.status_code == 200:
        dados_climaticos = resposta.json()
        estacao = EstacaoClimatica(
        id=dados_climaticos["id"],
        nome=dados_climaticos["name"],
        localizacao=localizacao
    )
        
        dado_climatico = DadoClimatico(
        id=dados_climaticos["id"],
        data_hora=dados_climaticos["dt"],
        estacao=estacao,
        temperatura=dados_climaticos["main"]["temp"],
        umidade=dados_climaticos["main"]["humidity"],
        velocidade_vento=dados_climaticos["wind"]["speed"],
        direcao_vento=dados_climaticos["wind"]["deg"]
    )
        
        return dado_climatico
    else:
        return None