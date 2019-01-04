# coding: UTF-8

# ---------------------------------------
# @note クラス
# ---------------------------------------

class Dog:
    # パブリックフィールド

    # プロパティ
    name = ""
    # メソッドにはself引数を付与する
    def bark(self):
        m = self.name + ": Bow-wow!"
        print(m)

# インスタンス
pochi = Dog()
pochi.name = "Pochi"
pochi.bark()

hachi = Dog()
hachi.name = "Hachi"
hachi.bark()
