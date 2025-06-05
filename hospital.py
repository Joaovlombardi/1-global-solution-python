# João Vitor: RM 563329 - Nicolas Baradel: RM 563245 - Patrick Correa: RM 564088

import requests  # Importa a biblioteca para fazer requisições HTTP

def hospital_mais_proximo(endereco):
    # Faz uma requisição para o serviço Nominatim para obter coordenadas do endereço
    geo = requests.get("https://nominatim.openstreetmap.org/search",
                       params={"q": endereco, "format": "json"},
                       headers={"User-Agent": "project"}).json()

    # Verifica se encontrou coordenadas para o endereço
    if not geo:
        return "Endereço não encontrado."

    # Pega latitude e longitude do endereço
    lat, lon = geo[0]["lat"], geo[0]["lon"]

    # Monta a consulta Overpass para buscar hospitais num raio de 5km
    overpass_query = f"""
    [out:json];
    node["amenity"="hospital"](around:5000,{lat},{lon});
    out center 1;
    """

    # Envia a consulta para a API Overpass
    res = requests.post("https://overpass-api.de/api/interpreter",
                        data=overpass_query,
                        headers={"User-Agent": "project"}).json()

    # Verifica se algum hospital foi encontrado
    if not res["elements"]:
        return "Nenhum hospital encontrado próximo ao endereço."

    # Pega os dados do primeiro hospital encontrado
    hospital = res["elements"][0]
    nome = hospital["tags"].get("name", "Nome não disponível")

    # Pega as coordenadas do hospital (ponto direto ou centro do elemento)
    lat_h = hospital.get("lat") or hospital.get("center", {}).get("lat")
    lon_h = hospital.get("lon") or hospital.get("center", {}).get("lon")

    # Retorna informações formatadas sobre o hospital
    return f"Hospital mais próximo: {nome}\nLocalização: {lat_h}, {lon_h}"
