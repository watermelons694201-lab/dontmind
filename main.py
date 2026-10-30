from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/v1/models")
def list_models():
    return {"data": [{"id": "your-voice-model"}]}

@app.post("/v1/audio/speech")
def generate_speech():
    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)