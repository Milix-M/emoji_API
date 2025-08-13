import logging
from fastapi import APIRouter, HTTPException, Response
from src.dto.emoji_parameter import EmojiParam
from src.services import emoji_service

logger = logging.getLogger(__name__)
router = APIRouter()
"""API router for emoji-related endpoints."""


@router.get("/fonts")
def get_available_fonts():
    """Retrieves a list of available fonts.

    Returns:
        dict: A dictionary containing a list of available fonts and their typefaces.
    """
    logger.info("フォント一覧リクエスト受信")
    response_dict = emoji_service.get_fonts_logic()
    return {"available_fonts": response_dict}


@router.post("/emoji")
def generate_emoji(param: EmojiParam):
    """Generates an emoji image based on the provided parameters.

    Args:
        param (EmojiParam): Parameters for generating the emoji image.

    Returns:
        Response: A FastAPI Response containing the generated image.

    Raises:
        HTTPException: If an invalid typeface name is provided or an unexpected error occurs.
    """
    logger.info(f"画像生成リクエスト受信: {param.model_dump()}")
    try:
        emoji_raw = emoji_service.generate_emoji_logic(param)
        return Response(content=emoji_raw, media_type="image/png")
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"{e}. Please use one of the available fonts from the /fonts endpoint.",
        )
    except Exception as e:
        logger.error(f"絵文字生成でエラーが発生しました: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred during image generation: {e}",
        )
