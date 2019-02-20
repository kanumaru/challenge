musician = ["BUMP OF CHIKEN","B'z","Mr.Children"]

place = [(36,139),(36,140),(36,135)]

i_am = {"height":189,"color":"green","author":"東野圭吾"}

key = input("キーワードを入力してください")
if key in i_am:
    print(i_am[key])
else:
    print("キーワードが間違っています")
    
i_am["BUMP OF CHIKEN"] = ["月虹","orbital period"]

print({"ゴン","キルア","クラピカ","レオリオ"} & {"ゴン","ナックル","シュート","モラウ","キルア"})

print(musician)
print(place)
print(i_am)
