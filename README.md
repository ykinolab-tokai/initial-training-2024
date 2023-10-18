# 木下研新入生研修

## 進め方

**現在検討中です．やりながら今後変わる可能性があります．**

- 1 時間で [演習問題](exercises.md) を解く
- 残りの時間で github にアップロード・レビューを行う

## 使い方

** はじめての人はまず[第1章のテキスト](https://github.com/ykinolab-tokai/initial-training/blob/main/text/01_Basic_Operations.ipynb) を開き，読み進めてください **
第1章のテキストを読み，手順に従って操作していけば**以下の手順は不要**です．

1. このレポジトリを fork する
2. fork したレポジトリをホームディレクトリなどに clone する
   ```
   $ git clone https://github.com/<user_name>/initial-training.git
   $ cd initial-training
   ```
   `<user_name>` の部分は各自のGitHubユーザー名に置き換えてください
3. 新しいブランチを作る
   ブランチ名は `<your_name>/chapter<章番号>` としてください．
   `<your_name>`の部分は，`First nameのイニシャル + Last name`をすべて小文字で書いてください．
   例：木下が 1 章のコードを追加するとき → `ykinoshita/chapter01`
   ```
   $ git branch <your_name>/chapter<XX>
   ```
4. ブランチを作成しただけでは，作業対象のブランチが切り替わりません．作業対象のブランチを作成した`<your_name>/chapter<章番号>`に切り替えるには以下のコマンドを入力します．
   ```
   $ git checkout <your_name>/chapter<章番号>
   ```
4. 自分用のディレクトリを作る
   ```
   $ mkdir <your_name>
   $ cd <your_name>
   ```
4. コードを書く
   ファイル名は `chapter<章番号>/q<問題番号>.py` とし，**章番号・問題番号は 1 始まりの 2 桁**に揃えてください．
   例：1 章の 1 個目 → `chapter01/q01.py`
5. 新しく書いたコードを git の管理対象に追加する
   ```
   $ git add ./<your_name>/chpaterXX/qYY.py
   ```
6. 変更を記録する
   コミットメッセージは「○ 章を追加」などわかりやすい文章にしてください．
   ```
   $ git commit -m 'your message'
   ```
7. Remote repository の変更を pull する
   ```
   $ git pull
   ```
8. Remote repository に push する
   このとき， `<your_name>/chapter<XX>` は 2. で作成したブランチ名にしてください
   ```
   $ git push origin <your_name>/chapter<XX>
   ```
9. GitHub 上で pull request を作成する

## 注意事項

- わからないところは **積極的** に RA か研究室の人に聞いてください．
- **他の人のディレクトリを変更しないでください．**
  - 他の人のコードを閲覧したい場合は、Web サイト上から閲覧してください．
- フォルダ名，ファイル名を間違えると進捗グラフに反映されません．

## 謝辞
以下を大変参考にさせていただきました．
- [都立大小野研究室のチュートリアル](https://github.com/onolab-tmu/asp-tutorial-2023)
- [Chainer Tutorial](https://tutorials.chainer.org/ja/tutorial.html)
- 田中，信号・データ処理のための行列とベクトル
