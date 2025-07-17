import requests

url = "http://127.0.0.1:8000/predict"

data = {"records": [{"data": {"feature1": "value1", "feature2": "value2"}}, {"data": {"feature1": "value3", "feature2": "value4"}}]}

response = requests.post(url, json=data)
print(response.json())
