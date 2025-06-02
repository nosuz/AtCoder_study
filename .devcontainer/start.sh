#!/bin/bash

# 所有者を修正（初回起動時のみ）
sudo chown -R vscode:vscode /home/vscode/.wdm
sudo chown -R vscode:vscode /home/vscode/.mozilla

# 通常の処理（例）
exec /bin/bash
