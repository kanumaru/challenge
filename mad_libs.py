import re
text = """キリンは大昔から　__複数名詞__　の興味の対象でした。キ
リンは　__複数名詞__　の中で一番背が高いですが、科学者たちはそのよ
うな長い　__体の一部__　をどうやって獲得したのか説明できません。キ
リンの身長は　__数値__ __単位__ 近くあり、その高さのほとんどは脚
と　__体の一部__ によるものです。
"""

def mad_libs(mls):
    hints = re.findall("__.*?__",mls)
    if hints is not None:
        hint = iter(hints)
        for word in hint:
            if word == "__複数名詞__" or word == "__単位__":
                next(hint)
            new = input("{}を入力".format(word))
            mls = mls.replace(word,new)
        print("\n")
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)
            
