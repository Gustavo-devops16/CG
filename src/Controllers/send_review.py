import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
app_key = os.getenv("X_VTEX_API_AppKey")
app_token = os.getenv("X_VTEX_API_AppToken")


def send_review(review):
    print(f"Enviando avaliação: {review.get('title', 'Título não fornecido')} para a VTEX")

    if isinstance(review, str):
        try:
            review = json.loads(review)  # Tenta converter a string JSON para um dicionário
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON")
            return
    elif not isinstance(review, dict):
        print("O parâmetro 'review' deve ser um dicionário ou uma string JSON válida.")
        return

    url = "https://compresuapeca.myvtex.com/reviews-and-ratings/api/reviews"
    headers = { 
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-VTEX-API-AppKey": app_key,
        "X-VTEX-API-AppToken": app_token
    }

    body = [
        {
            "id": review.get("id"),
            "productId": review.get("productId"),
            "rating": review.get("rating"),
            "text": review.get("text"),
            "reviewerName": review.get("reviewerName"),
            "approved": True,
            "title": review.get("title")
        }
    ]

    try:
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            print(f"Review enviado com sucesso: {response.json()}")
        else:
            print(f"Falha ao enviar review. Código de status: {response}")
    except Exception as e:
        print(f"Erro ao enviar review: {e}")
