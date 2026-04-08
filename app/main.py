from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/api/ip")
def get_ip(request: Request):
    return {"ip": request.client.host}

@app.get("/ip", response_class=HTMLResponse)
def get_ip_html(request: Request):
    return f"<h1>Your public IP is {request.client.host}</h1>"