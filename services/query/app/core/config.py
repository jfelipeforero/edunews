from pydantic_settings import BaseSettings, SettingsConfigDict


"""
Pydantic: Settings management
"""

class Settings(BaseSettings):
    FIRST_SUPERUSER: str = "jfelipef"
    FIRST_SUPERUSER_TITLE: str = "password"
    DB_URL: str

    model_config = SettingsConfigDict(env_file="./env")

settings = Settings(_env_file='.env')
