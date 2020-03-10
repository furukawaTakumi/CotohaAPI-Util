# CotohaAPI-Util
自然言語処理機能を提供するCOTOHA APIを簡単に利用できるクラスを作りました。

## スタートガイド
手順は全部で3つです。
#### COTOHA API開発者として登録する
COTOHA APIを利用する開発者として、以下のページでユーザ登録を行います。  

https://api.ce-cotoha.com/contents/index.html

#### ユーザデータを自身のものに変更する。
jsonファイル`api/data/account_data.json`の該当項目を自身のアカウント情報のものに書き換えてください。

#### サンプルファイルを動かしてみる
コマンドを用いてファイルを実行します。  
```
python sample.py
```

これで動作するはずです。

# サンプルプログラム解説
サンプルプログラムは前項目の通り、`sample.py`です。
少しずつ分解して解説していきます。

#### インポート
```python
from api.CotohaAccount import CotohaAccount
from api.CotohaAPI import CotohaAPI
```
利用するクラスをインポートしています。

#### インスタンスの生成
```python
account = CotohaAccount('api/data/account_data.json')
cotoha_api = CotohaAPI(account)
```

`CotohaAccount`クラスは定義されたアカウント情報を読み込み、提供する役割を担います。  

`CotohaAPI`クラスは実際にCOTOHA APIにリクエストを送信するためのものです。CotohaAccountオブジェクトを引数に渡して生成してください。

#### APIに解析してほしいデータを送信
`request_submit`メソッドを用いてAPIにリクエストを送信します。  

```python
parse_res = cotoha_api.request_submit('parse', {
    'sentence': '犬も歩けば棒に当たる'
    })
similarity_res = cotoha_api.request_submit('similarity', {
    's1': 'わけわかめ',
    's2': '意味がわからないよ',
    'type': 'kuzure'
    })

print(parse_res)
print(similarity_res)
```

第一引数は、自然言語処理の内容を示す文字列です。  
これは、APIを利用する際のHTTPエンドポイントの末尾と対応しています。  
構文解析を利用するためのエンドポイントは、リファレンスを参照しますと、`[API Base URL]/nlp/v1/parse`ですので、構文解析を利用するときに渡す引数文字列は`parse`となります。

第二引数は、解析に必要なデータです。  
各APIを利用する際に要求されるリクエストボディの内容を辞書として渡してください。  

なお、アクセストークンの取得処理は`request_submit`メソッドの内部に隠蔽されています。
