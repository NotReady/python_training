#coding: UTF-8

# ---------------------------------------
# @note 辞書(ハッシュリスト)
# - キーの型はなんでもよくて同居可能
# - 定義      variable = {key:value[, key:value]}
# - 参照       variable[key]
# - 追加/更新   variable[key] = value
# ---------------------------------------

# 定義{key:value[, key:value]}
a = {"Taro":1984, "Hanako":1985}
print(a)

# 参照　variable[key]
b = a["Taro"]
print(b)

# 追加　variable[key] = value
a["Jiro"] = 1988
print(a)

# 上書き　variable[key] = newValue
a["Hanako"] = 1990
print(a)

# keyの型はなんでも良いかつ、同居可能
c = {1:1991, 2:1992, "str":1, 0.1:1}
print(c)

d = c[1]
print(d)