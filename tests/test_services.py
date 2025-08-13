import pytest
from unittest.mock import patch
from src.services.emoji_service import get_fonts_logic, generate_emoji_logic
from src.dto.emoji_parameter import EmojiParam
from src.common.constants import Fonts

def test_get_fonts_logic():
    """
    get_fonts_logic関数のテスト
    """
    fonts = get_fonts_logic()
    assert isinstance(fonts, dict)
    for font_name, font_data in Fonts.FONT_NAME_PATH_MAPPING.items():
        assert font_name in fonts
        assert "typeface" in fonts[font_name]
        assert fonts[font_name]["typeface"] == font_data["typeface"]

@patch('emojilib.generate')
def test_generate_emoji_logic_success(mock_emojilib_generate):
    """
    generate_emoji_logic関数の成功ケースのテスト
    """
    mock_emojilib_generate.return_value = b'mock_image_data'
    param = EmojiParam(text="テスト", typeface_name="M+ 1p black")
    result = generate_emoji_logic(param)
    assert result == b'mock_image_data'
    mock_emojilib_generate.assert_called_once()

@patch('emojilib.generate')
def test_generate_emoji_logic_invalid_typeface(mock_emojilib_generate):
    """
    generate_emoji_logic関数の無効なフォント名ケースのテスト
    """
    param = EmojiParam(text="テスト", typeface_name="InvalidFontName")
    with pytest.raises(KeyError, match="Invalid typeface_name: 'InvalidFontName'"):
        generate_emoji_logic(param)
    mock_emojilib_generate.assert_not_called()
