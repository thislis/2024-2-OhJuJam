from fastapi import FastAPI
from backend.src.api import sign_in
from backend.src.api import sign_up

app = FastAPI()
app.include_router(sign_up.router)
app.include_router(sign_in.router)

@app.get("/")
async def root():
    return {"message": "Main"}