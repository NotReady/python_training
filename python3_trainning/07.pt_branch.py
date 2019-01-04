#coding: UTF-8

# ---------------------------------------
# @note 分岐
# - 条件演算子の行末にコロン
# - if ... : / elif ... : / else
# ---------------------------------------

a = 5

if a == 5:
    print("Hello")
else:
    print("Hi")

b = 4

if b < 3:
    print("Hello")
elif b < 5:
    print("Hi")
else:
    print("Yeah")

time = 15

if time > 5 and time < 12:
    print("Good morning!")
elif time >= 12 and time < 18:
    print("Good afternoon!")
else:
    print("Good night!")