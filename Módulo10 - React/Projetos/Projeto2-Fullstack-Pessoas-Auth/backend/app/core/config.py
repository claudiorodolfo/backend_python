import os


class Settings:
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-altere-em-producao")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


settings = Settings()
