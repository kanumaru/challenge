import random
class Deck:
    values = ["1","2","3","4","5","6","7","8","9","10","Juck","Queen","King"]
    def __init__(self):
        self.cards = []
        for i in range(4):
            for v in self.values:
                self.cards.append(v)
        self.cards.append("JOKER")
        random.shuffle(self.cards)


class Player:
    def __init__(self,name):
        self.rank = 0
        self.cards = None
        self.name = name
        self.zyanken = False
        self.difficult = False


class Game:
    rank = 3#イミュータブルだからクラス変数自体はメソッドでは変更不可。同様の名前のインスタンス変数を製造しそこに同値を代入し処理していく
    def __init__(self):
        self.p1 = Player(input("あなたの名前を入力してください"))
        self.p2 = Player(input("相手１の名前を入力してください"))
        self.p3 = Player(input("相手２の名前を入力してください"))
        self.p4 = Player(input("相手3の名前を入力してください"))

    def print_card(self,p1):
        print("今のあなたの手持ちのカードは、{}です".format("と".join(p1.cards)))

    def shft_card(self,card):
        for i in range(2):
            for v in Deck.values:
                if card.count(v) >= 2:
                    card.remove(v)
                    card.remove(v)
        return card

    def print_draw(self,player,target):
        if player == self.p1:
            print("{}が引く番です".format(player.name))
            print("相手の{}の手札は{}枚です".format(target.name,len(target.cards)))
            num = input("左から何番目のカードを引きますか？該当しない数値や文字を入力した場合はランダム")
            try:
                if 0 < int(num) <= len(target.cards):
                    value = target.cards.pop(int(num) - 1)
                else:
                    int("a")
            except ValueError:
                print("ランダムで引きます")
                value = target.cards.pop(random.randint(0,len(target.cards)-1))
            print("{}は{}を引きました".format(player.name,value))
            if len(target.cards) == 0:
                print("")
                print("{}が上がりました".format(target.name))
                target.rank += self.rank
                self.rank -= 1
                print("")
            if value in player.cards:
                player.cards.remove(value)
                print("同じ値のカードが手持ちにあるので一緒に捨てます")
            else:
                player.cards.append(value)
                print("同じ値のカードが手持ちにないので手札に加えます")
            print("")
        else:
            if target == self.p1:
                print("{}が{}からカードを引こうとしています！".format(player.name,target.name))
                print("{}の手札の内訳　：　{}".format(target.name,target.cards))
                if input("手札をシャッフルしますか？\"はい\"と入力するとシャッフルします") == "はい":
                    while True:
                        random.shuffle(target.cards)
                        print("")
                        print("{}の手札の内訳　：　{}".format(target.name,target.cards))
                        if input("もう一度シャッフルをしますか？\"はい\"と入力するとシャッフルします") != "はい":
                            break
            value = target.cards.pop(random.randint(0,len(target.cards)-1))
            if target == self.p1:
                print("{}は{}に{}を引かれました".format(target.name,player.name,value))
            else:
                print("{}は{}から一枚引きました".format(player.name,target.name))
            if len(target.cards) == 0:
                print("")
                print("{}が上がりました".format(target.name))
                target.rank += self.rank
                self.rank -= 1
                print("")
            if value in player.cards:
                player.cards.remove(value)
                print("{}は二枚のカードを捨てました".format(player.name))
            else:#これは１つ上のifのみと連携
                player.cards.append(value)
                print("{}は引いたカードを手札に加えました".format(player.name))
                if not player.difficult and value == "JOKER":
                    print("{}はなにやらそわそわしている".format(player.name))
            print("")
        if len(player.cards) == 0:
            print("{}が上がりました".format(player.name))
            player.rank += self.rank
            self.rank -= 1
            print("")

    def play_baba_game(self):
        print("")
        print("今からババ抜きを始めます")
        print("")
        print("難易度を選択してください。イージーモードではcomは引いたカードを左から順に加えていきます")
        if input("\"難しい\"と入力すればハードモード。それ以外だとイージーモード") == "難しい":
            self.p2.difficult = True
            self.p3.difficult = True
            self.p4.difficult = True
            print("ハードモード起動！")
        else:
            print("イージーモードで起動します")
        print("")
        cards = Deck().cards
        self.p1.cards = self.shft_card(cards[:13])
        self.p2.cards = self.shft_card(cards[13:26])
        self.p3.cards = self.shft_card(cards[26:39])
        self.p4.cards = self.shft_card(cards[39:52])
        luck = [self.p1,self.p2,self.p3,self.p4]
        luck[random.randint(0,3)].cards.append(cards[52])
        random.shuffle(luck)
        print("ランダムで引く順番が決まりました")
        print("{0}は{1}から、{1}は{2}から、{2}は{3}から、{3}は{0}からという順で引いていきます".format(luck[0].name,luck[1].name,luck[2].name,luck[3].name))
        print("")
        print("{}の手札の内訳　：　{}".format(self.p1.name,self.p1.cards))
        print("")
        for play in luck:
            print("{}の手札は{}枚です".format(play.name,len(play.cards)))
        print("")
        while True:
            self.screening(luck[0],luck[1],luck[2],luck[3])
            self.screening(luck[1],luck[2],luck[3],luck[0])
            self.screening(luck[2],luck[3],luck[0],luck[1])
            self.screening(luck[3],luck[0],luck[1],luck[2])
            if self.rank == 0:
                break
            print("")
            print("途中経過")
            print("")
            for num in range(4):
                print("{}の手札　：　{}枚".format(luck[num].name,len(luck[num].cards)))
            print("")
            print("")
        luck.sort(key = lambda x: x.rank)#僕一人じゃ思いつかなかったw
        print("決着がつきました")
        print("")
        print("最下位は{}".format(luck[0].name))
        print("")
        print("第三位は{}".format(luck[1].name))
        print("")
        print("第二位は{}".format(luck[2].name))
        print("")
        print("そして勝者は{}です！おめでとうございます！".format(luck[3].name))

    def screening(self,one,two,three,four):
        if len(one.cards) > 0:
            if len(two.cards) > 0:
                self.print_draw(one,two)
            elif len(three.cards) > 0:
                self.print_draw(one,three)
            elif len(four.cards) > 0:
                self.print_draw(one,four)
            if one.difficult:
                random.shuffle(one.cards)



Game().play_baba_game()
#今の所の問題点
#コンピューターの処理が速すぎて全然臨場感がない
