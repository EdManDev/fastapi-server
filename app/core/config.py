from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Server"
    DATABASE_URL: PostgresDsn
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()