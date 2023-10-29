from pydantic import BaseSettings

__all__ = ["settings"]


class Settings(BaseSettings):
    NOME_SERVICO: str
    VERSION: str
    PORT: int
    STRING_DB: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
