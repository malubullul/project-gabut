from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart irrigation API running", "ts": int(time.time())}

@app.get("/health")
def health():
    return {"status": "ok"}
