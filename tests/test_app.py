import pytest
from unittest.mock import patch
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

def test_generate_emoji_missing_parameters():
    """
    POST /emoji エンドポイントの必須パラメータ欠落ケースのテスト
    """
    response = client.post("/emoji", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert "field required" in response.json()["detail"][0]["msg"]

def test_generate_emoji_invalid_data_type():
    """
    POST /emoji エンドポイントの無効なデータ型ケースのテスト
    """
    response = client.post(
        "/emoji",
        json={
            "text": "テスト",
            "width": "invalid",  # 無効なデータ型
        },
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert "value is not a valid integer" in response.json()["detail"][0]["msg"]

def test_generate_emoji_out_of_range_quality():
    """
    POST /emoji エンドポイントの品質パラメータ範囲外ケースのテスト
    """
    response = client.post(
        "/emoji",
        json={
            "text": "テスト",
            "quality": 101,  # 範囲外の値
        },
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert "ensure this value is less than or equal to 100" in response.json()["detail"][0]["msg"]

def test_generate_emoji_invalid_align():
    """
    POST /emoji エンドポイントの無効なalign値ケースのテスト
    """
    response = client.post(
        "/emoji",
        json={
            "text": "テスト",
            "align": "invalid_align",  # 無効なalign値
        },
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert "value is not a valid enumeration member" in response.json()["detail"][0]["msg"]

def test_generate_emoji_empty_text():
    """
    POST /emoji エンドポイントの空のテキストケースのテスト
    """
    response = client.post(
        "/emoji",
        json={
            "text": "",  # 空のテキスト
        },
    )
    assert response.status_code == 200  # 空のテキストでも成功するはず
    assert response.headers["content-type"] == "image/png"
    assert len(response.content) > 0

@patch('src.services.emoji_service.generate_emoji_logic')
def test_generate_emoji_internal_server_error(mock_generate_emoji_logic):
    """
    POST /emoji エンドポイントの内部サーバーエラーケースのテスト
    """
    mock_generate_emoji_logic.side_effect = Exception("Test internal error")
    response = client.post(
        "/emoji",
        json={
            "text": "テスト",
            "typeface_name": "M+ 1p black",
        },
    )
    assert response.status_code == 500
    assert "detail" in response.json()
    assert "An unexpected error occurred during image generation: Test internal error" in response.json()["detail"]
