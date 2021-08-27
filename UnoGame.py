


import random


class UnoCard:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        if self.color == 0:
            return "green" + str(self.number)
        if self.color == 1:
            return "yellow" + str(self.number)
        if self.color == 2:
            return "blue" + str(self.number)
        if self.color == 3:
            return "red" + str(self.number)

    def canPlay(self, other):
        if (self.number == other.number) or (self.color == other.color):
            return True
        else:
            return False


class CollectionOfUnoCards:

    def __init__(self):
        self.list = []

    def addCard(self, card):
        self.list.append(card)

    def makeDeck(self):
        for i in range(1, 10):
            for j in range(4):
                for k in range(2):
                    self.list.append(UnoCard(j, i))

    def shuffle(self):
        for i in range(len(self.list)):
            r = random.randint(i, len(self.list) - 1)

            self.list[i], self.list[r] = self.list[r], self.list[i]

    def __str__(self):
        text = "["
        for card in self.list:
            text += str(card) + ","

        text += "]"
        return text

    def getNumCards(self):
        return len(self.list)

    def getTopCard(self):
        return self.list[-1]

    def canPlay(self, c):
        for i in range(len(self.list)):
            if (self.list[i].canPlay(c) == 1):
                return True
        return False

    def getCard(self, index):
        return self.list[index]

    def getRandomCard(self):
        return self.list[random.randint(0, len(self.list) - 1)]

    def getRandomPlayableCard(self, current):
        playable = []
        for card in self.list:
            if (card.canPlay(current)):
                playable.append(card)

        if len(playable) == 0:
            return None

        play = playable[random.randint(0, len(playable) - 1)]
        self.list.remove(play)
        return play

    def isEmpty(self):
        return len(self.list) == 0


class Uno:
    deck = CollectionOfUnoCards()
    lastPlayedCard = 0
    hand1 = CollectionOfUnoCards()
    hand2 = CollectionOfUnoCards()

    def __init__(self):
        self.deck.makeDeck()
        self.deck.shuffle()
        for i in range(14):
            if i % 2 == 0:
                self.hand1.addCard(self.deck.list.pop())
            else:
                self.hand2.addCard(self.deck.list.pop())

    def playTurn(self, player):
        if player == 1:
            play = self.hand1.getRandomPlayableCard(self.lastPlayedCard)
            if not play:
                self.hand1.addCard(self.deck.list.pop())
                return

            self.lastPlayedCard = play
        else:
            play = self.hand2.getRandomPlayableCard(self.lastPlayedCard)
            if not play:
                self.hand2.addCard(self.deck.list.pop())
                return

            self.lastPlayedCard = play

    def playGame(self):
        player = 1
        self.lastPlayedCard = self.hand1.getRandomCard()
        self.hand1.list.remove(self.lastPlayedCard)

        while not (self.deck.isEmpty() or self.hand1.isEmpty() or self.hand2.isEmpty()):
            if player == 1:
                player = 2
            else:
                player = 1

            self.playTurn(player)

            print("hand1: " + str(self.hand1))
            print("hand2: " + str(self.hand2))
            print("last card: " + str(self.lastPlayedCard))
            print()

        if self.hand1.isEmpty():
            print("Winner: Player1")
        elif self.hand2.isEmpty():
            print("Winner: Player2")
        else:
            print("Tie!")


def main():
    my_game = Uno()
    my_game.playGame()


main()
