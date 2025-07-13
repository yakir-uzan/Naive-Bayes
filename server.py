import uvicorn
from fastapi import FastAPI
from naiveBayesClassifier import NaiveBayesClassifier

app = FastAPI()

@app.get("/")
async def root():

    return {"messege": "hello world"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)