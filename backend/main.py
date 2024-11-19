from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.api import open_door

app = FastAPI()
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
    return RedirectResponse(url="/main", status_code=302)

@app.get("/main")
async def home():
    return {"message": "Main"}