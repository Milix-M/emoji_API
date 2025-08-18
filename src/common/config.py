from typing import List

class AppSettings:
    """Application settings."""
    PROJECT_NAME: str = "Emoji API"
    PROJECT_VERSION: str = "1.0.0"
    DESCRIPTION: str = "API for generating custom emoji images with text."

    # CORS settings
    CORS_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]

settings = AppSettings()
