# 概要
顔画像のトリミングをPythonで実装した。
環境：Docker

# 使い方
1. git cloneする
2. $docker-compose up -d
3. $docker exec -it python3-opencv-matplotlib bash
4. $cd src/face
5. $python python face.py family.jpg
6. 顔の座標がコンソールに表示される
7. family_faceフォルダが作成される
  - トリミングして分割した顔画像ファイル
  - 元の画像に顔の部分だけ白枠をつけた画像ファイル

# 参考
http://famirror.hateblo.jp/entry/2015/12/19/180000
