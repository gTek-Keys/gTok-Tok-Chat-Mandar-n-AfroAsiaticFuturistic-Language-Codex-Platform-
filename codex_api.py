from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from flow_manager import FlowManager

app = FastAPI()
flow = FlowManager()

# Allow all origins for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "gTok Codex API live", "phase": flow.state}

@app.post("/generate")
async def generate(request: Request):
    body = await request.json()
    user_input = body.get("text", "")
    result = flow.process(user_input)
    return {
        "response": result,
        "phase": flow.state,
        "blueprint": flow.get_blueprint().model_dump()
    }
