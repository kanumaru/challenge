class Shape:
    def what_am_i(self):
        return "I am shape"
class Rectangle(Shape):
    def __init__(self,w,l):
        self.wedth = w
        self.length = l

    def calculate_perimeter(self):
        return self.wedth*2 + self.length*2

class Square(Shape):
    def __init__(self,l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self,num):
        self.length += num
class Horse:
    def __init__(self,name,f,m,j):#クラスそのものをコンポジションする場合は、そのクラスの引数を忘れないこと
        self.name = name
        self.father = f
        self.mother = m
        self.jockey = j

class Rider:
    def __init__(self,name,age,win):
        self.name = name
        self.age = age
        self.win = win
