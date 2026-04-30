from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware # <--- 1. Import this

app = FastAPI()

# 2. Add this block right here:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Allows React to talk to Python
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Percepts(BaseModel):
    stench: bool
    breeze: bool
    glitter: bool

@app.get("/api/python")
def hello_world():
    return {"message": "Hello from Python logic!"}

@app.post("/api/infer")
def infer_move(percepts: Percepts):
    # This is a placeholder for your logic
    if percepts.glitter:
        return {"action": "GRAB", "reason": "Found the gold!"}
    if percepts.breeze:
        return {"action": "CAUTION", "reason": "Pit detected nearby."}
    return {"action": "FORWARD", "reason": "Path seems safe."}




# A simple mock-up of a 4x4 grid state
# P = Pit, W = Wumpus, G = Gold
world_map = {
    "0,1": "Breeze",
    "1,0": "Stench",
    "1,1": "Safe",
    "2,2": "Glitter"
}

@app.get("/api/logic")
def check_square(x: int, y: int):
    coord = f"{x},{y}"
    percept = world_map.get(coord, "Clear")
    
    # Simple Inference Logic
    if percept == "Glitter":
        return {"status": "Win", "msg": "You found the gold!", "action": "Grab"}
    elif percept == "Breeze":
        return {"status": "Danger", "msg": "It's breezy... a pit is near.", "action": "Wait"}
    else:
        return {"status": "Safe", "msg": "Everything looks okay.", "action": "Move"}