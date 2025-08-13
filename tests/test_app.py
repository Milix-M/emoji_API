import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_fonts():
    """
    GET /fonts エンドポイントのテスト
    """
    response = client.get("/fonts")
    assert response.status_code == 200
    assert "available_fonts" in response.json()
    assert isinstance(response.json()["available_fonts"], dict)
    # 特定のフォントが存在するか確認 (例: "M+ 1p black")
    assert "M+ 1p black" in response.json()["available_fonts"]

def test_generate_emoji_success():
    """
    POST /emoji エンドポイントの成功ケースのテスト
    """
    response = client.post(
        "/emoji",
        json={
            "text": "テスト",
            "width": 128,
            "height": 128,
            "color": "#000000FF",
            "background_color": "#00000000",
            "align": "center",
            "size_fixed": False,
            "disable_stretch": False,
            "typeface_name": "M+ 1p black",
            "format": "png",
            "quality": 100,
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert len(response.content) > 0 # 画像データが空でないことを確認

def test_generate_emoji_invalid_typeface():
    """
    POST /emoji エンドポイントの無効なフォント名ケースのテスト
    """
    response = client.post(
        "/emoji",
        json={
            "text": "テスト",
            "typeface_name": "InvalidFontName", # 存在しないフォント名
        },
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Invalid typeface_name" in response.json()["detail"]