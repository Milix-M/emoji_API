from pydantic import BaseModel, Field
from typing import Literal

# 'align'パラメータの選択肢をリテラル型で定義
AlignOptions = Literal["left", "center", "right"]
"""Literal type for text alignment options."""


class EmojiParam(BaseModel):
    """Pydantic model for holding parameters for text image generation."""

    text: str = Field(default="絵文\n字。", description="画像に表示するテキスト")
    width: int = Field(default=128, description="画像の幅")
    height: int = Field(default=128, description="画像の高さ")
    color: str = Field(default="#000000FF", description="文字色 (RGBA)")
    background_color: str = Field(default="#00000000", description="背景色 (RGBA)")
    align: AlignOptions = Field(default="center", description="テキストの水平方向の配置")
    size_fixed: bool = Field(default=False, description="フォントサイズを固定するかどうか")
    disable_stretch: bool = Field(default=False, description="画像の引き伸ばしを無効にするかどうか")
    typeface_name: str = Field(default="M+ 1p black", description="使用するフォント名")
    format: str = Field(default="png", description="出力画像形式")
    quality: int = Field(default=100, description="画質 (JPEGの場合に有効)")