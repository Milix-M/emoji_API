# ベースイメージをPython 3.9に変更
# python:3.9-slim-bullseye を使用してイメージサイズを抑えます
FROM python:3.9-slim-bullseye

# ビルド時にホストのユーザーIDとグループIDを受け取るための引数
ARG USER_ID
ARG GROUP_ID

# rootユーザーでパッケージのインストールとユーザー作成を行う
RUN apt-get update && \
    apt-get install -y sudo fontconfig libgl1-mesa-dev libglu1-mesa libopencv-dev && \
    # 受け取ったIDでグループとユーザーを作成
    addgroup --gid $GROUP_ID dockeruser && \
    adduser --uid $USER_ID --gid $GROUP_ID --disabled-password --gecos "" dockeruser && \
    # 作成したユーザーをsudoグループに追加
    adduser dockeruser sudo && \
    # パスワードなしでsudoを実行できるように設定
    echo "dockeruser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    # キャッシュを削除してイメージサイズを削減
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# これ以降の命令を実行するユーザーをdockeruserに切り替え
USER dockeruser

# 作業ディレクトリを設定
WORKDIR /app

# パッケージファイルをコピーする際に所有者をdockeruserに設定
COPY --chown=dockeruser:dockeruser ./common_lib/emojilib-1.0.1-cp39-cp39-linux_x86_64.whl /app/

# pipでパッケージをインストール
# --no-cache-dir オプションでキャッシュを残さず、イメージサイズを削減します
RUN pip install --no-cache-dir ./emojilib-1.0.1-cp39-cp39-linux_x86_64.whl

COPY --chown=dockeruser:dockeruser ./requirements.txt /app/
RUN pip install --no-cache-dir -r ./requirements.txt

# コンテナ起動時のデフォルトコマンド (インタラクティブなPythonシェルを起動)
CMD [ "python" ]
