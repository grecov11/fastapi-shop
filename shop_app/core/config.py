from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    def DATABASE_URL_asyncpg(self) -> str:
        """Формирует строку подключения для asyncpg."""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="../../.env")

settings = Settings()
database_url = settings.DATABASE_URL_asyncpg()
# print(database_url)
