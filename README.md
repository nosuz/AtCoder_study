# AtCoder の解答記録

AtCoder Beginner Contest(ABC)の問題を解いた記録です。基本的に正解できたコードのみが登録されていますが、一部不正解だが記録のために commit されたコードも入っています。

## 回答成績

- ✅: コンテスト時間内に正解
- 🙆: コンテスト外で正解
- 📖: 解説などに頼って正解
- ❌: 正解ではないが、とりあえずコミット

|     コンテスト      | パフォーマンス |  A  |  B  |  C  |  D  |  E  |  F  |
| :-----------------: | :------------: | :-: | :-: | :-: | :-: | :-: | :-: |
| [ABC392](./ABC391/) |                | 🙆 | 🙆 | 🙆 | 🙆 |     |     |
| [ABC399](./ABC399/) |                | 🙆 | 🙆 | 🙆 |     |     |     |
| [ABC400](./ABC400/) |      241       | ✅  | ✅  | 🙆 | 🙆 |     |     |
| [ABC401](./ABC401/) |      239       | ✅  | ✅  | 🙆 |     |     |     |
| [ABC402](./ABC402/) |      188       | ✅  | ✅  | 🙆 | 🙆 |     |     |
| [ABC403](./ABC403/) |      582       | ✅  | ✅  | ✅  |     |     |     |
| [ABC404](./ABC404/) |      297       | ✅  | ✅  |     |     |     |     |
| [ABC405](./ABC405/) |      622       | ✅  | ✅  | ✅  | ✅  |     | ❌  |
| [ABC406](./ABC406/) |      487       | ✅  | ✅  |     | 🙆 |     |     |
| [ABC407](./ABC407/) |      478       | ✅  | ✅  | ✅  |     |     |     |
| [ABC408](./ABC408/) |      260       | ✅  | ✅  | 🙆 |     |     |     |
| [ABC409](./ABC409/) |      207       | ✅  | ✅  | 🙆 |     |     |     |
| [ABC410](./ABC410/) |      568       | ✅  | ✅  | ✅  |     |     |     |
| [ABC411](./ABC411/) |      550       | ✅  | ✅  | ✅  |     |     |     |
| [ABC412](./ABC412/) |      328       | ✅  | ✅  | 🙆 |     |     |     |
| [ABC413](./ABC413/) |      337       | ✅  | ✅  | ✅  | 🙆 |     |     |
| [ABC415](./ABC415/) |      399       | ✅  | ✅  | 🙆 | 🙆 |     |     |
| [ABC416](./ABC416/) |      322       | ✅  | ✅  | 🙆 |     |     |     |
| [ABC417](./ABC417/) |      267       | ✅  | ✅  | 🙆 |     |     |     |
| [ABC418](./ABC418/) |      459       | ✅  | ✅  |     |     |     |     |
| [ABC419](./ABC419/) |      806       | ✅  | ✅  | ✅  | ✅  |     |     |
| [ABC420](./ABC420/) |      391       | ✅  | ✅  | ✅  |     |     |     |
| [ABC422](./ABC422/) |                | 🙆 | 🙆 |     |     |     |     |
| [ABC430](./ABC430/) |                | 🙆 | 🙆 | 📖 |     |     |     |
| [ABC431](./ABC431/) |                | 🙆 | 🙆 | 🙆 |     |     |     |
| [ABC432](./ABC432/) |                | 🙆 | 🙆 | 🙆 |     |     |     |
| [ABC433](./ABC433/) |                | 🙆 | 🙆 | 🙆 |     |     |     |
| [ABC434](./ABC434/) |                | 🙆 | 🙆 | 🙆 | 📖 |     |     |
| [ABC435](./ABC435/) |                | 🙆 | 🙆 | 🙆 | 📖 |     |     |
| [ABC436](./ABC436/) |                | 🙆 | 🙆 | 📖 | 🙆 |     |     |
| [ABC437](./ABC437/) |                | 🙆 | 🙆 | 📖 | 🙆 |     |     |
| [ABC438](./ABC438/) |                | 🙆 | 🙆 | 🙆 | 🙆 |     |     |
| [ABC439](./ABC439/) |      262       | ✅  | ✅  | 🙆 | 🙆 |     |     |
| [ABC440](./ABC440/) |      309       | ✅  | ✅  | 🙆 | 🙆 | 🙆 |     |
| [ABC441](./ABC441/) |      839       | ✅  | ✅  | 📖 | ✅  |     |     |
| [ABC442](./ABC442/) |      551       | ✅  | ✅  | ✅  | ✅  |     |     |
| [ABC443](./ABC443/) |                | 🙆 | 🙆 | 🙆 |     |     |     |

## Dev Container

[AtCoder用のDev Container](https://github.com/nosuz/atcoder_devcon)を使用しています。そのため、プログラミング環境の他、Javaのコードを簡単にコンテストページに貼り付けるChrome拡張などもレポジトリに含んでいます。

### Container の作成

コンテナを作成する手順は、次のとおりです。

1. このレポジトリをクローンする。
2. UID と GID を確認する。

もしローカルの UID と GID が次の表と異なる場合は、次のいずれかのコマンドを実行してローカルの ID がコンテナに反映されるように設定してください。この操作がないと、docker image の作成に時間がかかり、作成された image のサイズも大きくなります。

|     | ID   |
| --- | ---- |
| UID | 1000 |
| GID | 1000 |

1. VSCode で開き、コマンドパレットから`Dev Containers: Rebuild Container`を実行する。

```
bash .devcontainer/generate_env.sh
# or
python .devcontainer/generate_env.py
```

以上で、Python 環境の他、問題の入出力例を取得するプログラムが使えるようになります。

#### ログインテスト

ログイン状態かは、次のコマンドで確認できます。

```bash
./setup.py --login
```

`Screen Name`が表示されない場合は、ログイン状態が解除されています。Web Browserからcookie情報をコピーしてください。

### 入力・出力例の取得とコード作成

スケルトンコードとテストコードの作成には、`setup.py`を使用します。例えばABC439のコードを作成するには、次のコマンドを実行します。

```bash
./setup.py abc439
```

このコマンドを実行すると、`default_lang.txt`で指定した言語用のスケルトンコードとテストコードが作成されます。オプションにより、作成する言語を指定することができます。

### Options

- --python, --java: それぞれPythonとJava用のスケルトンコードとテストコードを作成します。

### default_lang.txt

`default_lang.txt`は、`setup.py`がオプションの指定なしに実行された時に作成する言語を指定します。

- #から始まる行は、コメントとなる。
- 言語は、各1行で指定する。

## Testing Codes

### Python

Pythonのテスト環境は、[pytest](https://docs.pytest.org/en/stable/)を使う方法と、`validate.py`を使う方法があります。

#### pytest

`pytest`を使った入力・出力例でのテスト

```bash
# A問題のテスト
pytest tests/test_a.py

# 個別の入力例でテスト
pytest tests/test_a.py -k sample1
pytest tests/test_a.py -k sample2

```

#### validate.py

`validate.py`を使った入力・出力例でのテスト

`validate.py`用の入力・出力例は、コードにコメントとして記載します。そのため自作の入力例を簡単にテストすることができます。

```bash
# A問題のテスト
python ../validate.py A.py

# 個別の入力例でテスト
python ../validate.py A.py --limit 1
python ../validate.py A.py --limit 1,2

```

### Java

`JUnit`を使った入力・出力例でのテスト

```bash
# A問題のテスト
gradle test --tests ATest

# 個別の入力例でテスト
gradle test --tests ATest.sample1
gradle test --tests ATest.sample2

```
