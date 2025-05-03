from pathlib import Path
import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from matrx_utils.conf import configure_settings

load_dotenv()


class Settings(BaseSettings):
    # App info
    APP_NAME: str = "microservice"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # API settings
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    TEMP_DIR: Path = Path(BASE_DIR) / "temp"

    # Logging
    LOG_LEVEL: str = "WARNING"
    LOCAL_LOG_DIRECTORY: Path = Path(TEMP_DIR) / "logs"
    REMOTE_LOG_DIRECTORY: Path = "var/log"
    LOG_FILENAME: str = f"matrx_app.log"
    LOG_VCPRINT: bool = True

    STATIC_ROOT: Path = Path(BASE_DIR) / "staticfiles"
    PORT: int = 8000

    SAVE_DIRECT_SCHEMA: bool = True
    LONG_RUNNING_SERVICES: list[str] = ["transcription_service",
                                        "scrape_service"]

    # Migration related settings.

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


# Create settings instance
settings = Settings()
configure_settings(settings_object=settings)

BASE_DIR = settings.BASE_DIR
TEMP_DIR = settings.TEMP_DIR
# Ensure directories exist
os.makedirs(settings.TEMP_DIR, exist_ok=True)
os.makedirs(settings.LOCAL_LOG_DIRECTORY, exist_ok=True)
