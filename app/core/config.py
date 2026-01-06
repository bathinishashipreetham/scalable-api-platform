from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Scalable API Platform"
    api_version: str = "v1"
    debug: bool = True

    model_config = {
        "env_file": ".env"
    }


settings = Settings()

