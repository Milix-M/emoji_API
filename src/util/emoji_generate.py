import emojilib
from ..dto.emoji_parameter import EmojiParamDTO


def emoji_generate(dto: EmojiParamDTO):
    if dto.typeface_name == "rounded-mplus-1p-black":
        dto.typeface_file = "../static/rounded-mplus-1p-black.ttf"

    emoji_raw = emojilib.generate(**dto)
    with open("emoji.png", "wb") as f:
        f.write(emoji_raw)

    return
