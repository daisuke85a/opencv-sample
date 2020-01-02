# 概要
OpenCVをDocker-compose.yamlで使えるようにした

# 使い方
1. git cloneする
2. $docker-compose up -d
3. $docker exec -it python3-opencv-matplotlib bash
4. $cd src/face
5. python python face.py family.jpg
6. 顔の座標がコンソールに表示される
