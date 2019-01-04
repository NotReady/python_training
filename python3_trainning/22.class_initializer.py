# coding: UTF-8

# ---------------------------------------
# @note クラスのイニシャライザ
# def __init__(self, initializeArg)
# ---------------------------------------

class Dog():
    #プロパティは実装があれば自動的に定義されるので不要！
    #name = ""
    def __init__(self, nm):
        self.name = nm

    def bark(self):
        m = self.name + ": Bow wow!"
        print(m)

pochi = Dog("Pochi")
pochi.bark()

# サブクラス
class Shibainu(Dog):
    def __init__(self, nm, age):
        super().__init__(nm)
        self.age = age

    def sayAboutMe(self):
        m = self.name + ": I'm " + str(self.age) + " years old"
        print(m)

hachi = Shibainu("Hachi", 10)
hachi.sayAboutMe()

class Mameshiba(Shibainu):
    def __init__(self, nm, age, w):
        super().__init__(nm, age)
        self.weight = w

    def myProfile(self):
        m = self.name + ": I'm "  + str(self.age) + " years old and " + str(self.weight) + "kg"
        print(m)

mame = Mameshiba("mameshiba", 3, 5)
mame.myProfile()