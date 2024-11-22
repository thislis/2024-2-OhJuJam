from operator import itemgetter
import json

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

app = FastAPI()
door_opened = False
ranking = []

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FormData(BaseModel):
    your_action: int
    name: str
    win: int

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

@app.post("/ranking/update")
def update_ranking(form: FormData):
    global ranking
    ranking.append({"name": form.name, "win": form.win})
    ranking = sorted(ranking, key=itemgetter('win'), reverse=True)
    return {"message": "Success"}

@app.get("/ranking/load")
def loading_ranking():
    ranker = {}
    for i in range(1, 11):
        global ranking
        if i <= len(ranking):
            ranker[f"rank {i}"] = ranking[i-1]
        else:
            ranker[f"rank {i}"] = {"name": "N/A", "win": 0}  # 기본값 추가
    return json.dumps(ranker)
