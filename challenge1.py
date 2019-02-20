print("こんにちは")
print("Hello")
print("ニーハオ")

import random
x = random.randint(0,20)
if x < 10:
    print("xは１０未満です")
if x >= 10:
    print("xは１０以上です")

y = random.randint(0,100)
if y <= 10:
    print("yは１０以下です")
elif 10 < y <= 25:
    print("yは１０より大きく、２５以下です")
else:
    print("yは２５より大きいです")

print(100 % 13)

print(100 // 13)

age = random.randint(0,100)
if age < 20:
    print("Child")
elif age <= 65:
    print("Adult")
else:
    print("Aged Adult")

