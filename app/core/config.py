from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Example: postgresql+psycopg://postgres:postgres@localhost:5432/app
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/app"
    RUN_MIGRATIONS: bool = True  # Disable in tests

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
