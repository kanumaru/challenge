movie = ["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for m in movie:
    print(movie)

for i in range(25,51):
    print(i)

for i,m in enumerate(movie):
    print(str(i) + m)

while True:
    num = input("正解の数字を入力してください")
    if num in [1,2,3,5,13]:
        print("正解")
        break
    if num == "q":
        break
    print("不正解")
    print("正解の数字を入力するか、qで終了します。")

new_list = []
for num1 in [8,19,148,4]:
    for num2 in [9,1,33,83]:
        new_list.append(num1 * num2)
print(new_list)
