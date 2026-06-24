from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "URL Shortener"
    debug: bool = False
    base_url: str = "http://localhost:8000"
    database_url: str = "postgresql://localhost/urlshortener"

    class Config:
        env_file = ".env"

settings = Settings()