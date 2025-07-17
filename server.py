from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from appController import AppController

app = FastAPI()

controller = AppController()
controller.run()

class Record(BaseModel):
    data: dict

class Records(BaseModel):
    records: List[Record]

@app.post("/predict")
def predict(records: Records):
    results = []
    for record in records.records:
        prediction = controller.classifier.predict(record.data)
        results.append({
            "description": ", ".join(f"{k}={v}" for k, v in record.data.items()),
            "prediction": "Will buy a computer" if prediction == "yes" else "Will NOT buy a computer"
        })
    return {"results": results}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)