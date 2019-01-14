# coding: UTF-8

# chainerのインポート
import chainer
from chainer import Variable, Chain, optimizers
import chainer.links as L
import chainer.functions as F

import numpy as np
# irisソース
from sklearn import datasets

# Irisデータの読み込み
iris_data = datasets.load_iris()
# print(iris_data)

# iris_dataはBunchオブジェクト・・・
# ディクショナリのキーを属性として参照できる型
# ndarray.astype(型) => 型キャスト
x = iris_data.data.astype(np.float32)
t = iris_data.target
n = t.size

print(x)
print(t)
print(n)