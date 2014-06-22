hnzy-sezemi-2014-readable-code-1
=================================

リーダブルコード勉強会用   
Python

# 実行手順

Python2系で動作します。以下に実行例を示します。

```
python --version
>>> Python 2.7.6
python recipe.py recipe-records.txt 2
>>> 2 : 杏仁豆腐
```

レシピデータは外部ファイルに保存します。ファイルのフォーマットは

2 : 杏仁豆腐   

のようにレシピとレシピIDが1行ずつ並んだ状態で保存します。
recipe.pyの実行時にレシピデータのファイル名とレシピIDを与えることで、
IDを指定したレシピのデータを作成することができます。