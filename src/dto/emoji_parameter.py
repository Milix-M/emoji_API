import logging
from dataclasses import dataclass
from typing import Literal

import emojilib
import falcon

from ..common.constants import Fonts

# ログ設定
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# 'align'パラメータの選択肢をリテラル型で定義
# これにより、'left', 'center', 'right' 以外は型チェッカーでエラーにできる
AlignOptions = Literal["left", "center", "right"]


@dataclass
class EmojiParamDTO:
    """
    テキスト画像生成のためのパラメータを保持するDTOクラス
    """

    text: str = "絵文\n字。"
    width: int = 128
    height: int = 128
    color: str = "#000000FF"
    background_color: str = "#00000000"
    align: AlignOptions = "center"
    size_fixed: bool = False
    disable_stretch: bool = False
    typeface_file: str = Fonts.FONT_NAME_PATH_MAPPING["M+ 1p black"]["path"]
    typeface_name: str = "M+ 1p black"
    format: str = "png"
    quality: int = 100

    def emoji_generate(self, req_dto):
        """DTOを基に絵文字画像を生成し、'emoji.png'として保存する。

        `typeface_name`からフォントパスを解決し、emojilibで画像を生成する。

        Args:
            req_dto (EmojiParamDTO): 画像生成用のパラメータを持つDTO。
                関数内で`typeface_file`が設定され、`typeface_name`はNoneに更新される。

        Raises:
            KeyError: 不正なフォント名が指定された場合に発生する。
        """

        # フォント名からフォントパスを出す
        req_dto.typeface_file = Fonts.FONT_NAME_PATH_MAPPING[req_dto.typeface_name][
            "path"
        ]

        # Noneにしないと何故かエラーになる
        req_dto.typeface_name = None

        try:
            logger.info("絵文字生成中...")
            # 絵文字生成
            emoji_raw = emojilib.generate(
                text=req_dto.text,
                width=req_dto.width,
                height=req_dto.height,
                color=req_dto.color,
                background_color=req_dto.background_color,
                align=req_dto.align,
                size_fixed=req_dto.size_fixed,
                disable_stretch=req_dto.disable_stretch,
                typeface_file=req_dto.typeface_file,
                typeface_name=req_dto.typeface_name,
                format=req_dto.format,
                quality=req_dto.quality,
            )
            logger.info("絵文字生成完了")
            return emoji_raw
        except Exception as e:
            logger.error(f"絵文字生成でエラーが発生しました: {e}")
            raise falcon.HTTPInternalServerError(
                title="Image generation error",
                description=f"An error occurred while generating the image: {e}",
            )

    def on_post(self, req, resp):
        """
        画像生成のリクエストを受け付け、DTOにマッピングして処理します。
        """
        try:
            req_param = req.get_media()
            dto = EmojiParamDTO(**req_param)

        except (TypeError, ValueError) as e:
            # TypeError: 必須引数がない場合 (例: textがない)
            # ValueError: 型が不正な場合 (例: alignに'top'を指定)
            raise falcon.HTTPBadRequest(
                title="Invalid parameters",
                description=f"Request body is invalid or missing required fields. Error: {e}",
            )

        logger.info(f"画像生成リクエストを受け付けました: {req_param}")

        try:
            image_data = self.emoji_generate(dto)

            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_PNG
            resp.data = image_data

        except Exception as e:
            # 画像生成中のエラーをハンドリング
            logger.error(f"リクエスト処理中にエラー: {e}")
            raise falcon.HTTPInternalServerError(
                title="Image Generation Failed",
                description="An unexpected error occurred during image generation.",
            )
