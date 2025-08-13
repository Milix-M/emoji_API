# Emoji_API

Python+FastAPI+Skiaを使用した絵文字生成API。

[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B56475%2Fgithub.com%2FMilix-M%2Femoji_API.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B56475%2Fgithub.com%2FMilix-M%2Femoji_API?ref=badge_shield&issueType=license)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B56475%2Fgithub.com%2FMilix-M%2Femoji_API.svg?type=shield&issueType=security)](https://app.fossa.com/projects/custom%2B56475%2Fgithub.com%2FMilix-M%2Femoji_API?ref=badge_shield&issueType=security)

## 概要 (Overview)

このプロジェクトは、PythonのFastAPIとSkiaライブラリを使用して、テキストからカスタム絵文字画像を生成するAPIを提供します。様々なフォント、色、サイズ、配置オプションをサポートし、動的な画像生成を可能にします。

## 特徴 (Features)

- **テキストから画像生成**: 指定されたテキストから絵文字画像を生成します。
- **カスタマイズ可能なオプション**: 幅、高さ、文字色、背景色、テキスト配置、フォントサイズ固定、画像引き伸ばし無効化などのパラメータをサポートします。
- **多様なフォントサポート**: 複数の日本語フォントを含む、利用可能なフォントを選択できます。
- **FastAPIによる高速API**: 高性能なFastAPIフレームワークを使用しています。
- **Docker対応**: Dockerizedされており、簡単に環境をセットアップ・デプロイできます。

## セットアップ (Setup)

### ローカル環境での実行 (Running Locally)

1. **リポジリのクローン**:

    ```bash
    git clone https://github.com/your-username/emoji_API.git
    cd emoji_API
    ```

2. **Python環境のセットアップ**:
    Python 3.9以上が必要です。`venv`などを使用して仮想環境を構築することを推奨します。

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. **依存関係のインストール**:

    ```bash
    pip install -r requirements.txt
    pip install -r requirements_dev.txt
    pip install ./common_lib/emojilib-1.0.1-cp39-cp39-linux_x86_64.whl
    ```

4. **アプリケーションの起動**:

    ```bash
    uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
    ```

    アプリケーションは `http://localhost:8000` で利用可能になります。

### Dockerを使用した実行 (Running with Docker)

DockerとDocker Composeがインストールされていることを確認してください。

1. **Dockerイメージのビルドと起動**:

    ```bash
    docker-compose up --build
    ```

    アプリケーションは `http://localhost:8000` で利用可能になります。

## テスト (Testing)

プロジェクトには`pytest`を使用した単体テストが含まれています。

1. **依存関係のインストール**:
    ローカル環境でのセットアップ手順に従い、`requirements_dev.txt`を含むすべての依存関係をインストールしてください。

2. **テストの実行**:

    ```bash
    pytest
    ```

## GitHub Actions

このプロジェクトはGitHub Actionsを使用してCI/CDパイプラインを自動化しています。

- `.github/workflows/ci.yml`: プルリクエストごとにテストを実行します。

## ライセンス (License)

このプロジェクトはMITライセンスの下で公開されています。詳細については[LICENCE](./LICENSE)ファイルを参照してください。
使用されているフォント・ライブラリには個別のライセンスがあります。詳細は`LICENCEs/`ディレクトリ内の各ライセンスファイルを参照してください。

## 貢献 (Contributing)

貢献を歓迎します！バグ報告、機能リクエスト、プルリクエストなど、お気軽にお寄せください。
