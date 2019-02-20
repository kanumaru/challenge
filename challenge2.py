def argument(n):
    """
    この関数は引数を２で割った値を返します。
    引数には数値を１つ入力してください
    """
    return n / 2
def authentication(n):
    """
    この関数は引数に４をかけた値を返します。
    引数には数値を１つ入力してください
    """
    return n * 4
print(authentication(argument(10)))

def field(n):#field(a)やfield(1,2,3)とされることで、この時点でエラーする可能性あり
    """
    この間酢は引数を浮動小数点数にして返します。
    様々な例外に対応しているので、引数には何を入力してくださっても構いません。
    """
    try:
        print(float(n))
    except(ValueError):
        print("数値を入力してください")
field("こんにちは")
field("11")
field("1.1")
field(11)
field(1.1)

def align():
    """
    この関数は入力された数値を二乗して返します
    """
    return int(input("好きな数値を入力してください")) ** 2
print(align())

def author(s):
    """
    この間酢は引数を出力します
    """
    print(s)
author("こんにちは")

def aggregate(a,b,c,d=10,e=100):
    """
    この関数は引数を合計した数値を出力します。
    引数には最低でも３つの数値を入力してください。
    ５つより多く入力しないでください。
    """
    print(a + b + c + d + e)
aggregate(1,2,3)
