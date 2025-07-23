from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse, HTMLResponse
from pydantic import BaseModel
from typing import List
from controller.appController import AppController
import pathlib

app = FastAPI()

# הגשת קבצים סטטיים
app.mount("/static", StaticFiles(directory="static"), name="static")

# הפעלת הקונטרולר
controller = AppController()
controller.run()

# מבני נתונים ל־POST
class Record(BaseModel):
    data: dict

class Records(BaseModel):
    records: List[Record]


@app.post("/predict", response_class=PlainTextResponse)
def predict(records: Records):
    record = records.records[0]
    prediction = controller.classifier.predict(record.data)
    return "Will buy" if prediction == "yes" else "Will NOT buy"


@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = pathlib.Path("../static/index.html")
    return index_path.read_text(encoding="utf-8")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
