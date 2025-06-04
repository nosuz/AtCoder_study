#!/bin/bash

# 所有者を修正（初回起動時のみ）
# チェック対象のディレクトリとマーカーファイル
MARKER_FILE="$HOME/.wdm/docker_volume_initialized"

# マーカーファイルがなければ初期化スクリプトを実行
if [ ! -f "$MARKER_FILE" ]; then
    echo "Initialization required. Running initialize.sh..."
    sudo chown -R vscode:vscode /home/vscode/.wdm
    sudo chown -R vscode:vscode /home/vscode/.mozilla

    # 初期化完了を示すマーカーファイルを作成
    touch "$MARKER_FILE"
fi

# 通常の処理
exec /bin/bash
