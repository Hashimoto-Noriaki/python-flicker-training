from flickrapi import FlickrAPI #FlikcrAPIクライアントのクラス定義
from urllib.request import urlretrieve #コマンドラインからhttp通信をする関数
import os, time, sys #Pythonからシステムにアクセスする関数, タイマー関数

# APIキーとsecretをセットします。wait_timeはAPIの負荷を下げるために画像の取得リクエストを送信するインターバルを1秒にセット
key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret = "xxxxxxxxxxxxxxxxxxxxx"
wait_time = 1 #リクエストを発行するインターバル

#クローリングしたファイル群を保存するフォルダーを指定
animalname = sys.argv[1] #コマンドラインで2番目の引数を取得
savedir = "./" + animalname#引数で与えた単語名でフォルダーを作成

# FlickrAPIのクライアントオブジェクトを生成
flickr = FlickrAPI(key, secret, format='parsed-json') 

# 検索を実行
result = flickr.photos.search(
    text = animalname,#検索ワード
    per_page = 400,#検索数上限
    media = 'photos', #データタイプ
    sort = 'relevance',#結果表示順, 最新から
    safe_search = 1,#子どもに不敵な画像を除外
    extras = 'url_q, licence'#オプション。データURL, ライセンスタイプ
)

# 検索結果から写真データを取り出し、ダウンロード
photos = result['photos']
