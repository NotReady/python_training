# coding: UTF-8

import chainer
import numpy as np
from chainer import Variable, Chain, optimizers
import chainer.links as L
import chainer.functions as F
# マットプロットリブ　グラフに描画
import matplotlib.pyplot as plt

# 階段関数のデータ
x,t = [],[]
for i in np.linspace(-1, 1, 100):
    x.append([i])
    if i < 0:
        t.append([0])
    else:
        t.append([1])

# データをグラフにプロットする
# プロットデータは1重配列に変換する
# print(x)
# print(np.array(x, dtype=np.float32).flatten())
#plt.plot(np.array(x, dtype=np.float32).flatten(),
#         np.array(t, dtype=np.float32).flatten())
#plt.show()

# モデルの実装
class MyChain(Chain):
    def __init__(self):
        super().__init__(
            l1 = L.Linear(1, 10),
            l2 = L.Linear(10, 1),
        )
    # callじゃないのか
    def predict(self, x):
        h1 = F.sigmoid(self.l1(x))
        return self.l2(h1)

# 入力と正解のVariableを準備
x = Variable(np.array(x, dtype=np.float32))
t = Variable(np.array(t, dtype=np.float32))
# モデルのインスタンス
model = MyChain()
# optimizerの実装
optimizer = chainer.optimizers.Adam()
optimizer.setup(model)

# 学習させる
y = None
for i in range(100000):
    # 勾配をリセット
    model.cleargrads()
    y = model.predict(x)

    # 学習の途中経過を表示
    if i % 10000 == 0:
        plt.plot(x.data.flatten(), y.data.flatten())
        plt.title("i = " + str(i))
        plt.show()

    # 損失関数による誤差の計算（平均二乗誤差）
    loss = F.mean_squared_error(y, t) # 出力と正解値の誤差
    loss.backward() # 勾配

    # Optimizerで重みを更新する
    optimizer.update()

plt.plot(x.data.flatten(), y.data.flatten())
plt.title("Finish!")
plt.show()
