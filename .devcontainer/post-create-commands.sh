#!/bin/bash

# 所有者を修正（初回起動時のみ）
# チェック対象のディレクトリとマーカーファイル
MARKER_FILE="$HOME/.wdm/docker_volume_initialized"

# マーカーファイルがなければ初期化スクリプトを実行
if [ ! -f "$MARKER_FILE" ]; then
    echo "Initialization required. Running initialize.sh..."
    sudo chown -R vscode:vscode $HOME/.wdm
    sudo chown -R vscode:vscode $HOME/.mozilla

    # 初期化完了を示すマーカーファイルを作成
    touch "$MARKER_FILE"
fi

# install gradle
export SDKMAN_DIR="$HOME/.sdkman"
curl -s "https://get.sdkman.io" | bash
source "$SDKMAN_DIR/bin/sdkman-init.sh"
sdk install gradle 8.7
