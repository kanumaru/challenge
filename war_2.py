from random import shuffle

class Card:
    suits = ["spades","hearts","diamonds","clubs"]
    values = [None,None,
              "2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,v,s):
        self.value = v
        self.suit = s

    def __lt__(self,c2):
        if self.value == c2.value:
            return self.suit < c2.suit
        return self.value < c2.value

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
        return False

    def __repr__(self):
        return "{} of {}".format(self.values[self.value],self.suits[self.suit])


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for s in range(4):
                self.cards.append(Card(i,s))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレイヤー１の名前を入力してください")
        name2 = input("プレイヤー２の名前を入力してください")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        print("このラウンドは{}が勝ちました。".format(winner))
              
    def play_game(self):
        cards = self.deck.cards
        print("戦争を始め余す")
        while len(cards) >= 2:
            if input("qで終了。それ以外のキーで続行") == "q":
                break
            self.p1.card = self.deck.rm_card()
            self.p2.card = self.deck.rm_card()
            if self.p1.card > self.p2.card:
                self.wins(self.p1.name)
                self.p1.wins += 1
            else:
                self.wins(self.p2.name)
                self.p2.wins += 1

        print("ゲーム終了！{}の勝利です！".format(self.winner(self.p1,self.p2)))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"

Game().play_game()
