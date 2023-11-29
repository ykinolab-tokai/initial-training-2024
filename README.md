# 木下研新入生研修

## 進め方

**現在検討中です．やりながら今後変わる可能性があります．**

- [演習問題](exercises.md) の解説を，ランダムに選ばれた人にしてもらう
- 残りの時間は，グループに分かれ次章の [演習問題](exercises.md) を解く
- 次週までに GitHub にアップロード・レビューを行う

## 使い方

はじめての人はまず[第1章のテキスト](https://github.com/ykinolab-tokai/initial-training/blob/main/text/01_Basic_Operations.ipynb) を開き，読み進めてください．

第2章以降に取り組む際は以下の手順に従って操作してください．

1. GitHub 上で研究室の Remote repository `ykinolab-tokai/initial-training`を自分用の Remote repository `<user_name>/initial-training` の `main` ブランチに merge する．
2. Remote repository の変更を Local repository に取り込む (pull する)．
   ```
   $ cd ~/initial-training
   $ git checkout main
   $ git pull origin main
   ```
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
