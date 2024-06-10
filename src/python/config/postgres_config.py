from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ['settings_db']


class SettingsDb(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    model_config = SettingsConfigDict(env_file="dev.env", env_file_encoding='utf-8')

    @property
    def DB_URL_ASYNCPG(self):
        # postgresql+asyncpg://user:pass@host:port/db
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings_db = SettingsDb()
