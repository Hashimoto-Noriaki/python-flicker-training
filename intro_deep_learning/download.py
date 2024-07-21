from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os
import time
import sys

# APIキーとシークレットを設定
key = "#####"
secret = "######"
wait_time = 1  # リクエストを発行するインターバル

# コマンドラインから取得したキーワードで保存ディレクトリを作成
animalname = sys.argv[1]  # コマンドラインで2番目の引数を取得
savedir = "./" + animalname

# フォルダーが存在しない場合は作成
if not os.path.exists(savedir):
    os.makedirs(savedir)

# FlickrAPIのクライアントオブジェクトを生成
flickr = FlickrAPI(key, secret, format='parsed-json')

# 検索を実行
result = flickr.photos.search(
    text=animalname,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, license'
)

# 検索結果から写真データを取り出し、ダウンロード
photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']  # photoオブジェクトからダウンロードURLを取得
    filepath = os.path.join(savedir, f"{photo['id']}.jpg")  # ファイル名をフルパスで生成
    if os.path.exists(filepath):
        continue  # ファイルが既に存在する場合はスキップ
    urlretrieve(url_q, filepath)  # ファイルダウンロードを実行
    time.sleep(wait_time)  # サーバー負荷を考慮して1秒あける
