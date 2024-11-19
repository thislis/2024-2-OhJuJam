from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import sign_in, sign_up, open_door

app = FastAPI()
app.include_router(sign_up.router)
app.include_router(sign_in.router)
app.include_router(open_door.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Main"}