import logging
import emojilib

from src.common.constants import Fonts
from src.dto.emoji_parameter import EmojiParam

logger = logging.getLogger(__name__)


def get_fonts_logic():
    """Retrieves the logic for available fonts.

    Returns:
        dict: A dictionary mapping font names to their typeface information.
    """
    logger.info("フォント一覧ロジック実行")
    return {
        font_name: {"typeface": font_data["typeface"]}
        for font_name, font_data in Fonts.FONT_NAME_PATH_MAPPING.items()
    }


def generate_emoji_logic(param: EmojiParam) -> bytes:
    """Generates an emoji image based on the provided parameters.

    Args:
        param (EmojiParam): Parameters for generating the emoji image.

    Returns:
        bytes: Raw image data in bytes.

    Raises:
        KeyError: If an invalid typeface name is provided.
    """
    logger.info(f"画像生成ロジック実行: {param.model_dump()}")

    # KeyErrorは呼び出し元で処理するため、ここではチェックのみ
    if param.typeface_name not in Fonts.FONT_NAME_PATH_MAPPING:
        raise KeyError(f"Invalid typeface_name: '{param.typeface_name}'")

    font_path = Fonts.FONT_NAME_PATH_MAPPING[param.typeface_name]["path"]

    logger.info("絵文字生成中...")
    param_dict = param.model_dump()
    param_dict["typeface_file"] = font_path
    # typeface_nameはemojilibでは不要なのでNoneにする
    param_dict["typeface_name"] = None

    emoji_raw = emojilib.generate(**param_dict)
    logger.info("絵文字生成完了")
    return emoji_raw
