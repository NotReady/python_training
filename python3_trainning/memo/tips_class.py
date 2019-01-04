# スーパークラスの定義
class superClass():

    # self.propertyでプロパティは自動的に生成されるので定義は不要
    # name = ""

    # イニシャライザ(コンストラクタ)
    def __init__(self, nm):
        self.name = nm

    def myNameIs(self):
        print("my name is " + self.name)

    # callメソッドの定義
    def __call__(self):
        print("do call")

# サブクラスの定義
class subClass(superClass):

    def __init__(self, nm, ag):
        # スーパークラスを参照してイニシャライザ実行
        super().__init__(nm)
        self.age = ag

    # 拡張
    def myAgeIs(self):
        print("my age is " + str(self.age) + " years old")

    # 上書き
    def __call__(self):
        print("do sub call")

superObj = superClass("obj1")

subObj = subClass("sub", 10)
subObj.myNameIs()
subObj.myAgeIs()
# callメソッド呼び出し => インスタンス直で呼び出す
subObj()
