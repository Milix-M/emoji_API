"""Main application file for the Emoji API.

This file initializes the FastAPI application, configures logging, sets up CORS middleware,
and includes the API routers.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import emoji

# ログ設定
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Emoji API",
    description="API for generating custom emoji images with text.",
    version="1.0.0",
)
"""FastAPI application instance."""

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの登録
app.include_router(emoji.router)
