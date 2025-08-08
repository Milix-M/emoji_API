from dataclasses import dataclass, asdict
from typing import Optional, Literal
from ..util.emoji_generate import emoji_generate
import falcon

# 'align'パラメータの選択肢をリテラル型で定義
# これにより、'left', 'center', 'right' 以外は型チェッカーでエラーにできます
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
    typeface_file: Optional[str] = None  # Noneを許容するためOptionalを使用
    typeface_name: Optional[str] = None
    format: str = "png"
    quality: int = 100

    def on_post(self, req, resp):
        """
        画像生成のリクエストを受け付け、DTOにマッピングして処理します。
        """
        try:
            # 1. リクエストボディのJSONを取得
            req_param = req.get_media()

            # 2. 辞書をアンパックしてDTOをインスタンス化
            #    JSONのキーがDTOの属性名と一致している必要がある
            dto = EmojiParamDTO(**req_param)

        except (TypeError, ValueError) as e:
            # TypeError: 必須引数がない場合 (例: textがない)
            # ValueError: 型が不正な場合 (例: alignに'top'を指定)
            raise falcon.HTTPBadRequest(
                title="Invalid parameters",
                description=f"Request body is invalid or missing required fields. Error: {e}",
            )

        # 3. DTOを使って何らかの処理を行う (この例では画像生成をシミュレート)
        #    dto.text, dto.width などで安全にパラメータにアクセスできる
        print(
            f"画像生成リクエストを受け付けました: text='{dto.text}', width={dto.width}"
        )

        emoji_generate(dto)

        # 4. 成功レスポンスを返す
        #    受け取ったパラメータをDTO経由で確認のために返す
        resp.status = falcon.HTTP_200
        resp.media = {
            "status": "success",
            "message": "Image generation request received.",
            "received_parameters": asdict(dto),  # DTOを辞書に変換して返す
        }
