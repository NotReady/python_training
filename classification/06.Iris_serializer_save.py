## coding: UTF-8

# chainerのインポート
import chainer
from chainer import Variable, Chain, optimizers, serializers
import chainer.links as L
import chainer.functions as F

from chainer.datasets import tuple_dataset
from chainer import training, iterators
from chainer.training import extensions

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
t_train = t_matrix[indexes_train, :] # 訓練用正解
x_test = x[indexes_test, :] # 検証用入力
t_test = t[indexes_test] # 検証用正解

# Variableに変換
train = tuple_dataset.TupleDataset(x_train, t_train)
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

    # tranerを用いる場合は__callメソッドの実装が必要
    def __call__(self, x, t):
        return F.mean_squared_error(self.predict(x), t)

    def predict(self, x):
        h1 = F.sigmoid(self.l1(x))
        h2 = F.sigmoid(self.l2(h1))
        h3 = self.l3(h2)
        return h3

# モデルとoptimizerの設定
model = IrisChain()
optimizer = optimizers.Adam()
optimizer.setup(model)

# trainerによる学習
train_iter = iterators.SerialIterator(train, 30)
updater = training.StandardUpdater(train_iter, optimizer)
trainer = training.Trainer(updater, (5000, 'epoch'))
trainer.extend(extensions.ProgressBar())
trainer.run()

serializers.save_npz("my_iris.npz", model)