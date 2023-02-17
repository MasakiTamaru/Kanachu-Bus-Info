# Unkoujouhou.py

神奈中バスのソフトウェアの"神奈中バスロケ"のスクレイピングをしました。
(http://real.kanachu.jp/pc/top)  
こちらに自分が調べたい乗車バス停と降車バス停を入力し検索ボタンを押します。
検索後のページのURLを、unkoujouhou.pyの変数(url)に代入することで、
必要な情報のみをスクレイピングしてくれます。

# Unkoujouhou2.py

unkoujouhou.pyとほとんど変わりませんが、こちらでは、時間を指定することで、
一定間隔で、スクレイピングをし続けてくれます。

# Unkoujouhou3.py

unkoujouhou.pyに自動で検索するモジュールを追加しました。
実行して、バス停名を入力すると検索結果が開きます。

# What I want to do

micro_Python で同じように実現したく考えています。(M5STACKにプログラムを内蔵したい)
また、unkoujouhou2.pyでは、無限ループになってしまっているので、
毎朝この時間からこの時間までのように、特定の時間のみ実行するプログラムを作成したいです。

URLをはらずにpythonに入力させる →  https://ai-inter1.com/python-selenium/

# Additional Information

このプログラムであると、神奈中バスのページから乗車バス停と降車バス亭を検索した結果を
URLにする必要がある。以下のライブラリを用いると、ブラウザの操作(検索)も行ってくれる。

https://ai-inter1.com/python-selenium/

# Finally

まだまだ初心者だと思うので、アドバイスよろしくお願いします！
