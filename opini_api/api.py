from fastapi import FastAPI, Query
from scrapping import scrap
from fastapi.middleware.cors import CORSMiddleware

# from traitement import treat
# from model_deep import deepModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vous pouvez spécifier les domaines autorisés ici
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/opini_ia")
def process_data(url):
    # Scrapper les données
    data = scrap(url)
    
    """
    # Traiter les données
    treated_data = treat(data)
    
    # Effectuer le modèle de machine learning
    result = deepModel(treated_data)
    
    # Formater la sortie
    percentage = round(result * 100, 2)
    output = {
        "percentage": percentage,
        "phrases_negatives": ["Phrase négative 1", "Phrase négative 2", "Phrase négative 3"],
        "phrases_positives": ["Phrase positive 1", "Phrase positive 2", "Phrase positive 3"]
    }
    """
    # return output
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)

    
