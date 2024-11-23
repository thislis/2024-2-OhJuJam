from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

app = FastAPI()
door_opened = False

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FormData(BaseModel):
    your_action: int

@app.get("/")
async def root():
    return RedirectResponse(url="/main", status_code=302)

@app.get("/main")
async def home():
    return {"message": "Main"}

@app.get("/door/load")
def load_door():
    if door_opened:
        door_state = "Opened"
    else:
        door_state = "Reverse Opened"
    return door_state

@app.post("/door/open")
def update_door(form_data: FormData):
    global door_opened
    if form_data.your_action == 1:
        door_opened = True
    elif form_data.your_action == 2:
        door_opened = False
    return {"message": "Success"}