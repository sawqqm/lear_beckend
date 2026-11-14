from pydantic_settings import SettingsConfigDict

from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str 
    cors_allowed_origins: list[str]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
settings = Settings()

