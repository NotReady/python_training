# coding: UTF-8

# ---------------------------------------
# @note クラスとリストを使ったサンプル
# ---------------------------------------

class Calculation():
    value = 0
    def square(self):
        s = self.value ** 2
        return s

d = [Calculation(), Calculation(), Calculation()]

root = 3
for i in d:
    i.value = root
    print(i.square())
    root += 2
