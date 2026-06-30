from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "library_management_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = "mysql+pymysql://root:Sureshkumar%40123@localhost/library_db"

    class Config:
        env_file = ".env"


settings = Settings()