from fastapi import FastAPI
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

@app.get("/")
async def root():
    return RedirectResponse(url="/main", status_code=302)

@app.get("/main")
async def home():
    return {"message": "Main"}

@app.get("/load")
def load_door():
    return {"door_state": door_opened}

@app.post("/open")
def update_door(form_data):
    if form_data.action == 1:
        door_opened = True
    elif form_data.action == -1:
        door_opened = False
    return {"message": "Success"}