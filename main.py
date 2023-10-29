from fastapi import FastAPI
from starlette.responses import JSONResponse
from src.routes.personagem import Personagem
from src.env import settings


app = FastAPI(
    title=settings.NOME_SERVICO,
    description="Sistema para importacão de dados de producão para homologacão",
    version=settings.VERSION
)

app.include_router(Personagem)


@app.get("/", tags=["Root"])
def read_root():
    return JSONResponse(
        status_code=200,
        content={
            "status": True,
            "message": settings.NOME_SERVICO,
            "version": settings.VERSION
        }
    )
