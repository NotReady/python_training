# coding: UTF-8

#------------------------
#
#------------------------

import chainer
from chainer import Chain, Variable, optimizers, serializers, datasets
import chainer.links as L
import chainer.functions as F

from chainer.datasets import tuple_dataset
from chainer import training, iterators
from chainer.training import  extensions

import numpy as np

mnist_data = datasets.get_mnist(ndim=3)
train_data = mnist_data[0]
test_data = mnist_data[1]

print("Train", len(train_data))
print("Test:", len(test_data))

# 画像を表示
# import matplotlib.pyplot as plt
#
# index = 2
# plt.imshow(train_data[index][0].reshape(28, 28), cmap='gray')
# plt.title(train_data[index][1])
# plt.show()

class MyMNIST(Chain):
    def __init__(self):
        # L.Convolution2D(チャンネル数(RGB=3)、フィルター数、フィルタのサイズ)
        super(MyMNIST, self).__init__(
            # 画像サイズは
            # 入力(1レイヤー, 28px, 28px)
            # => フィルタ(15レイヤー, 24px, 24px)
            #  元画像28px - オフセット(フィルタ5px - 1px)px =>  24px
            cnn1 = L.Convolution2D(1, 15, 5),
            # 画像サイズは
            # プーリング結果(15レイヤー, 12px, 12px)
            # => フィルタ(40レイヤー, 8px, 8px)
            #  元画像12px - オフセット(フィルタ5px - 1px)px =>  8px
            cnn2 = L.Convolution2D(15, 40, 5),

            l1 = L.Linear(640, 400),
            l2 = L.Linear(400, 10),
        )

    # trainerを使うのでcallを実装
    def __call__(self, x, t):
        return F.softmax_cross_entropy(self.predict(x), t)

    # プーリング
    def predict(self, x):
        # F.max_pooling_2d(入力画像、領域のサイズ)
        # プーリングによって領域サイズを畳み込み
        # フィルタ(15レイヤー, 24px, 24px)
        #  => プーリング(15レイヤー, 12px, 12px)
        #   => フィルタ24px / 2pxプーリング領域 = 12px
        h1 = F.max_pooling_2d(F.relu(self.cnn1(x)), 2)
        # フィルタ(40レイヤー, 8px, 8px)
        #  => プーリング(40レイヤー, 4px, 4px)
        #   => フィルタ8px / 2pxプーリング領域 = 4px
        h2 = F.max_pooling_2d(F.relu(self.cnn2(h1)), 2)
        # linkにプーリング(40レイヤー, 4px, 4px)=640pxを入力する
        h3 = F.dropout(F.relu(self.l1(h2)))

        return self.l2(h3)

# モデルとoptimizerの設定
model = MyMNIST()
optimizer = optimizers.Adam()
optimizer.setup(model)

# 学習
iterator = iterators.SerialIterator(train_data, 500)
updater = training.StandardUpdater(iterator, optimizer)
trainer = training.Trainer(updater, (20, 'epoch'))
trainer.extend(extensions.ProgressBar())
trainer.run()

# モデルの保存
serializers.save_npz("my_mnist.npz", model)

# テスト
correct = 0
for i in range(len(test_data)):
    x = Variable(np.array([test_data[i][0]], dtype=np.float32))
    t = test_data[i][1]
    y = model.predict(x)
    maxIndex = np.argmax(y.data)
    if maxIndex == t:
        correct += 1

print("Correct:", correct, "Total:", len(test_data), "Acuuracy:", correct / len(test_data) * 100, "%")
