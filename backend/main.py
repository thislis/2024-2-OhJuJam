from fastapi import Fastapi

app = Fastapi()

@app.get("/")
async def root():
    return {"message": "Main"}

