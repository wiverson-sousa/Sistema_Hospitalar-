from fastapi import FastAPI
from app.routers.medico import router as router_medico
from app.routers.consulta import router as router_consulta

app = FastAPI()

app.include_router(router_medico, prefix='/api/medico', tags=['medico'])
app.include_router(router_consulta, prefix='/api/consulta', tags=['consulta'])
