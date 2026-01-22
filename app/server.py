from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory=".")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://server.luckylinux.xyz", "https://server.luckylinux.xyz"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World!"})

@app.post("/", response_class=HTMLResponse)
async def update_message(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "This is CICD pipeline demo!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)