import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "records": [
        {
            "data": {
                "Age": "Youth",
                "Income": "High",
                "Student": "No",
                "Credit_rating": "Fair"
            }
        },
        {
            "data": {
                "Age": "Senior",
                "Income": "Low",
                "Student": "Yes",
                "Credit_rating": "Excellent"
            }
        }
    ]
}

response = requests.post(url, json=data)
print(response.json())
