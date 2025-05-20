from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    ENV: str = Field(
        default="local",
        env="ENV",
        description="Execution environment"
    )
    # Database configuration
    DATABASE_URL: Optional[str] = Field(
        default=None,
        env="DATABASE_URL",
        description="Database connection URL"
    )
    # JWT configuration
    SECRET_KEY: str = Field(
        default="your-secret-key",
        env="SECRET_KEY",
        description="Secret key to sign JWT tokens"
    )
    ALGORITHM: str = Field(
        default="HS256",
        env="ALGORITHM",
        description="Encryption algorithm for JWT tokens"
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30,
        env="ACCESS_TOKEN_EXPIRE_MINUTES",
        description="JWT token expiration time in minutes"
    )

    class Config:
        env_file = ".env"

settings = Settings()
