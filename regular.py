import re
print(re.findall("beautiful","Beautiful is better than ugly",re.IGNORECASE))
zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

print(re.findall("^If",zen,re.MULTILINE))

print(re.findall("t[wo]o","Two too",re.IGNORECASE))#ふた文字目はwでもoでもいいよ！

print(re.findall("\d","123 hi 34 Hello."))

print(re.findall("\\$","I love $",re.IGNORECASE))

print(re.findall(".*?oo","The ghost that says boo haunts the loo",re.IGNORECASE))

print(re.findall(".oo","The ghost that says boo haunts the loo"))
