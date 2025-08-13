import logging
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import emojilib

from .common.constants import Fonts
from .dto.emoji_parameter import EmojiParam

# ログ設定
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では適切なオリジンに制限してください
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fonts")
def get_available_fonts():
    """利用可能なフォントの一覧を返す"""
    logger.info("フォント一覧リクエスト受信")
    response_dict = {
        font_name: {"typeface": font_data["typeface"]}
        for font_name, font_data in Fonts.FONT_NAME_PATH_MAPPING.items()
    }
    return {"available_fonts": response_dict}


@app.post("/emoji")
def generate_emoji(param: EmojiParam):
    """パラメータに基づいて絵文字画像を生成する"""
    logger.info(f"画像生成リクエスト受信: {param.model_dump()}")

    try:
        # フォント名からフォントパスを取得
        font_path = Fonts.FONT_NAME_PATH_MAPPING[param.typeface_name]["path"]
    except KeyError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid typeface_name: '{param.typeface_name}'. Please use one of the available fonts from the /fonts endpoint.",
        )

    try:
        logger.info("絵文字生成中...")
        # Pydanticモデルから辞書に変換してemojilibに渡す
        param_dict = param.model_dump()
        # emojilibが必要とするパラメータを準備
        param_dict["typeface_file"] = font_path
        # typeface_nameはemojilibでは不要なのでNoneにする
        param_dict["typeface_name"] = None

        emoji_raw = emojilib.generate(**param_dict)
        logger.info("絵文字生成完了")

        # FastAPIのResponseを使ってバイナリデータを返す
        return Response(content=emoji_raw, media_type="image/png")

    except Exception as e:
        logger.error(f"絵文字生成でエラーが発生しました: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred during image generation: {e}",
        )