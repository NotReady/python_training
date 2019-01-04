# coding: UTF-8

# ---------------------------------------
# @note callメソッド
# 名無しメソッド
# def __call__(self[, args])
# ---------------------------------------

class Dog():
    def __init__(self, na):
        self.name = na

    def bark(self):
        m = self.name + ": Bow-wow!"
        print(m)

    # callメソッドの定義
    def __call__(self, ag, w):
        m = "Name: " + self.name + " Age: " + str(ag) + \
            " Weight:" + str(w) + "kg"
        print(m)

pochi = Dog("Pochi")
pochi.bark()
# callメソッド呼び出し => インスタンス直で呼び出す
pochi(4, 20)
