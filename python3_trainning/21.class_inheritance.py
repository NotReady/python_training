# coding: UTF-8

# ---------------------------------------
# @note クラスの継承
# class subClass(superClass):
# ---------------------------------------

# スーパークラス
class Dog:
    name = ""
    def bark(self):
        m = self.name + ": Bow wow!"
        print(m)

# サブクラス
class Shibainu(Dog):
    age = 0
    def sayAge(self):
        m = "I'm " + str(self.age) + " years old"
        print(m)

hachi = Shibainu()
hachi.name = "Hachi"
hachi.bark()
hachi.age = 10
hachi.sayAge()
