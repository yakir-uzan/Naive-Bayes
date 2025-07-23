from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse, HTMLResponse
from pydantic import BaseModel
from typing import List
from controller.appController import AppController
from pathlib import Path

app = FastAPI()

# נתיב לתיקיית הבסיס וסטטיק
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
DATA_PATH = BASE_DIR / "data" / "DB.csv"

# חיבור תיקיית static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# יצירת הקונטרולר עם הנתיב לקובץ הדאטה
controller = AppController(data_path=DATA_PATH)
controller.run()

# מודלים לקלט POST
class Record(BaseModel):
    data: dict

class Records(BaseModel):
    records: List[Record]

# מסלול POST לחיזוי
@app.post("/predict", response_class=PlainTextResponse)
def predict(records: Records):
    record = records.records[0]
    prediction = controller.classifier.predict(record.data)
    return "Will buy" if prediction == "yes" else "Will NOT buy"

# מסלול GET לדף הבית
@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = STATIC_DIR / "index.html"
    return index_path.read_text(encoding="utf-8")

# הפעלת השרת
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
