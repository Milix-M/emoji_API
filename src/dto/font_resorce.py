import logging
from ..common.constants import Fonts
import falcon

# ログ設定
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class EmojiResource:
    def on_get(self, req, resp):
        """利用可能なフォントの一覧をJSONで返す"""
        logger.info("フォント一覧 リクエスト")

        # 'path'を除外し、'typeface'だけを含む新しい辞書を生成
        response_dict = {
            font_name: {"typeface": font_data["typeface"]}
            for font_name, font_data in Fonts.FONT_NAME_PATH_MAPPING.items()
        }

        resp.status = falcon.HTTP_200
        resp.media = {"available_fonts": response_dict}
