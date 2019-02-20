class Square:
    square_list = []
    def __init__(self,l):
        self.length = l
        self.square_list.append(self)

    def calculate_area(self):
        return self.length * 4

    def __repr__(self):
        return "{0} by {0} by {0} by {0}".format(self.length)#ゼロから始まることに注意。数を入れなければデフォルトで０、１、２、３となる。
s = Square(10)
print(s.square_list)
s2 = Square(20)
print(s.square_list)

def judge(j1,j2):
    return j1 is j2
print(judge(1,1))
print(judge("バカ","アホ"))
print(judge("abc","abc"))
