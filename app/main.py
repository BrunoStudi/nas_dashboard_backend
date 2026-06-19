from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import disks, cpu, zpools, ipmi, system, gpu

app = FastAPI(title="Dashboard NAS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(disks.router)
app.include_router(cpu.router)
app.include_router(gpu.router)
app.include_router(zpools.router)
app.include_router(ipmi.router)
app.include_router(system.router)



@app.get("/")
def root():
    return {"message": "Dashboard NAS API opérationnelle"}