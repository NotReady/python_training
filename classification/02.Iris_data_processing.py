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

# 行コメント cmd + /
# print(x)
# print(t)
# print(n)

# 教師データの下処理
# 正解番号を3列のフラグ構造に変換する
t_matrix = np.zeros(3 * n).reshape(n, 3).astype(np.float32)
for i in range(n):
    t_matrix[i, t[i]] = 1.0

# print(t_matrix)

# 0-149のベクトルをを訓練用データ(奇数)とテスト用データ(偶数)に分ける
indexes = np.arange(n) # 0 n-1
indexes_train = indexes[indexes%2 != 0] # 訓練用
indexes_test = indexes[indexes%2 == 0] # 検証用
# print(indexes)
# print(indexes_train)
# print(indexes_test)

x_train = x[indexes_train, :] # 訓練用入力
t_train = t_matrix[åindexes_train, :] # 訓練用正解
x_test = x[indexes_test, :] # 検証用入力
t_test = t[indexes_test] # 検証用正解

print(x_train)
print(t_train)
print(x_test)
print(t_test)

# Variableに変換
x_train_v = Variable(x_train)
t_train_v = Variable(t_train)
x_test_v = Variable(x_test)
