# Unkoujouhou_Py

神奈中バスのソフトウェアの"神奈中バスロケ"のスクレイピングをしました。
(http://real.kanachu.jp/pc/top)  
こちらに自分が調べたい乗車バス停と降車バス停を入力し検索ボタンを押します。
検索後のページのURLを、unkoujouhou.pyの変数(url)に代入することで、
必要な情報のみをスクレイピングしてくれます。

# Unkoujouhou2_py

unkoujouhou.pyとほとんど変わりませんが、こちらでは、時間をしてすることで、
一定間隔で、スクレイピングをし続けてくれます。

# What I want to do

micro_Python で同じように実現したく考えています。(M5STACKにプログラムを内蔵したい)
また、unkoujouhou2.pyでは、無限ループになってしまっているので、
毎朝この時間からこの時間までのように指定したいです。