# X Bot

Qiitaの[Seleniumを用いたTwitterへのログイン及び投稿](https://qiita.com/rinodrops/items/f1cd9c3ddf6cd8a20d05)を参考にした。

## 機能一覧

- [x] twitter のログイン
- [x] tweetの投稿
- [x] 画像付きtweetの投稿
- [ ] フォロワーにDMの送信
- [x] 定期実行（Github Actionsを利用）

## 定期実行の設定

1. `.github/workflows/schedule.yml` を開き `cron` をutcで指定する

```yaml
on:
  schedule:
    - cron: "0 0 * * *"  # 毎日0時0分 (UTC) に実行
```

2. GitHub Secretsの設定

    1. GitHubリポジトリのページに移動
    1. 「Settings」タブを選択
    1. 左側のメニューから「Secrets and variables」→「Actions」を選択
    1. 「New repository secret」をクリック
    1. 下記の環境変数を追加する（但し、値は自分の環境に合わせたものを使用すること）

```
EMAIL=メールアドレスを指定する
PASSWORD=パスワードを平文で指定する
USERNAME=ユーザ名を指定する
USER_AGENT=ユーザーエージェントを指定する
```
