## coding: UTF-8

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

# 教師データの下処理
# 正解番号を3列のフラグ構造に変換する
t_matrix = np.zeros(3 * n).reshape(n, 3).astype(np.float32)
for i in range(n):
    t_matrix[i, t[i]] = 1.0

# 0-149のベクトルをを訓練用データ(奇数)とテスト用データ(偶数)に分ける
indexes = np.arange(n) # 0 n-1
indexes_train = indexes[indexes%2 != 0] # 訓練用
indexes_test = indexes[indexes%2 == 0] # 検証用

x_train = x[indexes_train, :] # 訓練用入力
t_train = t_matrix[åindexes_train, :] # 訓練用正解
x_test = x[indexes_test, :] # 検証用入力
t_test = t[indexes_test] # 検証用正解

# Variableに変換
x_train_v = Variable(x_train)
t_train_v = Variable(t_train)
x_test_v = Variable(x_test)

# ニューラルネットワーク
class IrisChain(Chain):

    # 4 - 6 - 3のリンク
    def __init__(self):
        super().__init__(
            l1 = L.Linear(4, 6),
            l2 = L.Linear(6, 6),
            l3 = L.Linear(6, 3)
        )

    def predict(self, x):
        h1 = F.sigmoid(self.l1(x))
        h2 = F.sigmoid(self.l2(h1))
        h3 = self.l3(h2)
        return h3

# モデルとoptimizerの設定
model = IrisChain()
optimizer = optimizers.Adam()
optimizer.setup(model)

# 学習
for i in range(10000):
    # 勾配のリセット
    model.cleargrads()
    y_train_v = model.predict(x_train_v)

    # 損失関数による誤差の計算、平均二乗誤差
    loss = F.mean_squared_error(y_train_v, t_train_v)
    loss.backward()

    # 重みの更新
    optimizer.update()
