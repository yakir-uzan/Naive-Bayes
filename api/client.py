import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "records": [
        {
            "data": {
                "age": "youth",
                "income": "high",
                "student": "no",
                "credit_rating": "fair"
            }
        },
        {
            "data": {
                "age": "senior",
                "income": "low",
                "student": "yes",
                "credit_rating": "excellent"
            }
        }
    ]
}

response = requests.post(url, json=data)
print(response.text)
