from fastapi import FastAPI
from backend.src.api import sign_in
from backend.src.api import sign_up
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(sign_up.router)
app.include_router(sign_in.router)

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