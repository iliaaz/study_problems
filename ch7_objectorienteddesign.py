from dataclasses import dataclass, field
import heapq
import random


@dataclass
class deck():
    """docstring for deck"""
    id: int
    numberofdecks: int = 1
    cards: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.reset(self.numberofdecks)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self, numberofdecks=1):
        self.cards = list(range(1, 53)) * numberofdecks


@dataclass
class blackjack():
    id: int
    deck: deck
    numberofplayers: int
    hands: list[list] = field(default_factory=list)

    def dealhands(self):
        self.hands = []
        for i in range(self.numberofplayers):
            self.hands.append([])
            self.hands[i].append(self.deck.cards.pop())
            self.hands[i].append(self.deck.cards.pop())
        return self.hands

    def valuehand(self, hand):
        ace = any(True for card in hand if card % 13 == 1)
        sum = 0
        for card in hand:
            if card % 13 == 0 or card % 13 > 9:
                sum += 10
            else:
                sum += card % 13
        if sum <= 11 and ace:
            return sum + 10
        else:
            return sum

    def dealcard(self, handnumber):
        carddealt = self.deck.cards.pop()
        self.hands[handnumber].append(carddealt)
        return carddealt


@dataclass
class callcenter():
    id: int
    employees: dict = field(default_factory=dict)
    available: list = field(default_factory=list)

    def hire_employee(self, employee):
        # Add new employee object to employees
        pass

    def fire_employee(self, employeeid):
        # Remove employee object from employees
        pass

    def employee_available(self, employeeid):
        # Add employee to available priority queue; role designates value
        pass

    def employee_unavailable(self, employeeid):
        # Remove employee from available
        pass

    def dispatch_call(self):
        # Pop top employee from available queue
        pass


@dataclass
class employee():
    id: int
    name: str
    role: str


@dataclass 
class song():
    title: str
    artist: str
    year_recorded: int


@dataclass
class album():
    title: str
    artist: str
    year_released: int
    tracks: list[song]


@dataclass
class display():
    status: str
    nowplaying: str
    queuestatus: str


@dataclass
class jukebox():
    library: list[album] = field(default_factory = list)
    playlist: list = field(default_factory = list)
    statusdisplay: display = None

    def addalbum(self):
        pass

    def removealbum(self):
        pass

    def queuealbum(self, albumid):
        pass

    def queuesong(self, albumid, songid):
        pass

    def clearqueue(self):
        self.playlist = []


@dataclass
class parkingspot():
    length: int
    width: int
    occupied: bool = False


@dataclass
class parkingzone():
    parkingspots: list[parkingspot]

    def capacity(self):
        return sum(not spot.occupied for spot in self.parkingspots)


@dataclass
class parkinglot():
    zones: list[parkingzone]

    def capacity(self):
        return sum(zone.capacity() for zone in self.zones)

    def admitcar(self):
        pass

    def releasecar(self):
        pass


@dataclass
class puzzlepiece():
    id: int

    def isedge(self):
        pass

@dataclass
class jigsaw():
    pieces: list[puzzlepiece]

    def fitswith(self, pieceone, piecetwo):
        pass


if __name__ == '__main__':
    # deckone = deck(1)
    # decktwo = deck(2, 2)
    # blackjackone = blackjack(1, decktwo, 5)
    # blackjackone.dealhands()
    # for handnumber, hand in enumerate(blackjackone.hands):
    #     while blackjackone.valuehand(hand) < 17:
    #         blackjackone.dealcard(handnumber)
    #     print(hand, blackjackone.valuehand(hand))


    pl = parkinglot([parkingzone([parkingspot(10,5)]*25)]*5)
    print(pl.capacity())
    pass
