from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_url: str = Field(..., env="postgres_url")
    server_port: int = Field(..., env="server_port")
