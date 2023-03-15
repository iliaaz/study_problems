from bisect import bisect
from collections import defaultdict, Counter
from dataclasses import dataclass, field
import random
import heapq


def numberswapper(n1, n2):
    n1 ^= n2
    n2 ^= n1
    n1 ^= n2

    return n1, n2


def tictactoe_won(board):
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][0] == board[i][1]) or (
            board[0][i] == board[1][i] and board[0][i] == board[2][i]
        ):
            return True
    if (
        board[0][0] == board[1][1]
        and board[0][0] == board[2][2]
        or board[2][0] == board[1][1]
        and board[2][0] == board[0][2]
    ):
        return True
    return False


def factorialzeros(n):
    factorsoffive = 0
    divisor = 5

    while n >= divisor:
        factorsoffive += n // divisor
        divisor *= 5
    return factorsoffive


def smallestdifference(arr1, arr2):
    if len(arr1) > len(arr2):
        smaller = arr2
        larger = arr1
    else:
        smaller = arr1
        larger = arr2

    smaller.sort()
    smallestdifference = abs(arr1[0] - arr2[0])
    for num in larger:
        insertionindex = bisect(smaller, num)
        if abs(smaller[insertionindex - 1] - num) < smallestdifference:
            smallestdifference = abs(smaller[insertionindex - 1] - num)
        if (
            insertionindex < len(smaller)
            and abs(smaller[insertionindex] - num) < smallestdifference
        ):
            smallestdifference = abs(smaller[insertionindex] - num)
    return smallestdifference


def trickmax(n1, n2):
    return [n1, n2][(int(n1 - n2) - abs(n1 - n2)) // (abs(n1 - n2) ** abs(n1 - n2))]


def matches_pattern(pattern, value):
    count_first = pattern.count(pattern[0])
    pattern_first = pattern[0]
    if pattern[0] == "a":
        pattern_second = "b"
        count_second = pattern.count("b")
    else:
        pattern_second = "a"
        count_second = pattern.count("a")

    print(pattern_first, count_first, pattern_second, count_second)

    maxlength_first = (len(value) - count_second) // count_first
    for i in range(1, maxlength_first + 1):
        firstword = value[:i]

        firstword_occurances = value.count(firstword)
        print(firstword, firstword_occurances)
        if firstword_occurances != count_first:
            continue

        subvalue = value.replace(firstword, "")
        print(subvalue)
        if subvalue == "":
            return True
        elif len(subvalue) % count_second != 0:
            continue

        secondword = subvalue[: (len(subvalue) // count_second)]

        candidate = ""
        for char in pattern:
            if char == pattern_first:
                candidate += firstword
            else:
                candidate += secondword

        print(f"Candidate: {candidate}")
        if candidate == value:
            return True

    return False


def divingboard(length1, length2, planks):
    possiblelengths = set()
    for n in range(planks + 1):
        possiblelengths.add(length1 * n + length2 * (planks - n))
    return sorted(list(possiblelengths))


def divingboard_recursive(
    length1, length2, planks, state, visited={}, possiblelengths=set()
):
    if state in visited:
        return
    else:
        visited[state] = True

    if state[0] + state[1] == planks:
        possiblelengths.add(state[0] * length1 + state[1] * length2)
        return

    divingboard_recursive(length1, length2, planks, (state[0] + 1, state[1]))
    divingboard_recursive(length1, length2, planks, (state[0], state[1] + 1))

    return sorted(list(possiblelengths))


def maxlivingpeople(livesinfo):
    lifevectors = defaultdict(int)
    for lifeinfo in livesinfo:
        lifevectors[lifeinfo[0]] += 1
        lifevectors[lifeinfo[1] + 1] -= 1

    maxaliveyear = None
    maxalive = 0
    alivecounter = 0
    for year in sorted(list(lifevectors)):
        alivecounter += lifevectors[year]
        if alivecounter > maxalive:
            maxalive = alivecounter
            maxaliveyear = year
    return maxaliveyear


def bestline(points):
    slopesfromapoint = defaultdict(dict)

    maxslopes = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if (points[j][0] - points[i][0]) != 0:
                slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            else:
                slope = "inf"
            if slope in slopesfromapoint[i]:
                slopesfromapoint[i][slope] += 1
            else:
                slopesfromapoint[i][slope] = 1
            if slopesfromapoint[i][slope] > maxslopes:
                maxslopes = slopesfromapoint[i][slope]
                solution = [points[i], points[j]]
    return solution


def subsort(array):

    smallestsortedindex = 0
    maxthusfar = 0
    for i, n in enumerate(array):
        maxthusfar = max(maxthusfar, n)
        if n != maxthusfar:
            smallestsortedindex = min(len(array) - 1, i)

    greatestsortedindex = len(array) - 1
    minthusfar = 9999999
    for i in range(len(array) - 1, -1, -1):
        minthusfar = min(minthusfar, array[i])
        if array[i] != minthusfar:
            greatestsortedindex = max(0, i)

    return greatestsortedindex, smallestsortedindex


def contiguoussequence(array):
    runningmax = array[1]
    runningsum = 0

    for n in array:
        runningsum += n
        if runningsum > runningmax:
            runningmax = runningsum
        if runningsum < 0:
            runningsum = 0
    return runningmax


def buildwaterandadjacency(topologymap):
    adjacency = defaultdict(list)
    water = []

    for y, row in enumerate(topologymap):
        for x in range(len(row)):
            if topologymap[y][x] == 0:
                water.append((y, x))
                if y - 1 > 0:
                    if topologymap[y - 1][x] == 0:
                        adjacency[(y, x)].append((y - 1, x))
                if y + 1 < len(topologymap):
                    if topologymap[y + 1][x] == 0:
                        adjacency[(y, x)].append((y + 1, x))
                if x - 1 > 0:
                    if topologymap[y][x - 1] == 0:
                        adjacency[(y, x)].append((y, x - 1))
                if x + 1 < len(row):
                    if topologymap[y][x + 1] == 0:
                        adjacency[(y, x)].append((y, x + 1))

    return water, adjacency


def exploreponds(water, adjacency):
    visited = {}
    pondsizes = []
    for wetspot in water:
        pondsize = 0
        tovisit = [wetspot]
        while tovisit:
            visiting = tovisit.pop()
            if visiting in visited:
                continue
            visited[visiting] = True
            pondsize += 1
            tovisit = adjacency[visiting] + tovisit
        if pondsize > 0:
            pondsizes.append(pondsize)
    return pondsizes


def sizeponds(topologymap):
    water, adjacency = buildwaterandadjacency(topologymap)
    ponds = exploreponds(water, adjacency)
    return ponds


def bigger(array1, array2):
    if len(array2) > len(array1):
        return array2, array1
    else:
        return array1, array2


def sumswap(array1, array2):
    biggerarray, smallerarray = bigger(array1, array2)
    difference = sum(biggerarray) - sum(smallerarray)

    if difference % 2 == 1:
        return "Impossible"

    biggernums = {}
    for n in biggerarray:
        biggernums[n] = True

    for n in smallerarray:
        if (n + difference // 2) in biggernums:
            return (n, n + difference // 2)

    return "Impossible"


@dataclass
class letternode:
    letter: str
    children: dict = field(default_factory=dict)

    def insertword(self, word):
        cursor = self
        for char in word:
            if char not in cursor.children:
                cursor.children[char] = letternode(char)
            cursor = cursor.children[char]
        return self


def generatetrie(words):
    trie = letternode("*")
    for word in words:
        trie.insertword(word)
    return trie


def numbertoletters(number):
    conversion = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    return conversion[number]


def searchtrie(corpus, input, assembly, solutions=[]):
    if input == "":
        solutions.append(assembly)
        return solutions

    for char in numbertoletters(input[0]):
        if char in corpus.children:
            searchtrie(corpus.children[char], input[1:], assembly + char)

    return solutions


def t9(input):
    words = [
        "apple",
        "about",
        "asked",
        "ask",
        "bake",
        "big",
        "blue",
        "book",
        "box",
        "burn",
        "buy",
        "cake",
        "call",
        "cold",
        "come",
        "copy",
        "day",
        "desk",
        "dog",
        "door",
        "down",
        "draw",
        "drink",
        "drive",
        "easy",
        "eat",
        "egg",
        "end",
        "far",
        "fast",
        "feed",
        "few",
        "fire",
        "fish",
        "five",
        "fix",
        "flag",
        "flat",
        "fly",
        "food",
        "foot",
        "four",
        "free",
        "from",
        "full",
        "gain",
        "game",
        "get",
        "give",
        "tree",
        "used",
    ]
    corpus = generatetrie(words)
    return searchtrie(corpus, str(input), "")


def turn(direction, rotation):
    return (direction + rotation) % 4


def move(pos_y, pos_x, direction):
    if direction == 0:
        return pos_y - 1, pos_x
    if direction == 1:
        return pos_y, pos_x + 1
    if direction == 2:
        return pos_y + 1, pos_x
    if direction == 3:
        return pos_y, pos_x - 1


def langstonant(k):
    grid = defaultdict(lambda: defaultdict(bool))
    direction = 1
    pos_x = 0
    pos_y = 0
    max_x = 0

    for _ in range(k):
        grid[pos_y][pos_x] ^= True
        direction = turn(direction, [-1, 1][grid[pos_y][pos_x]])
        pos_y, pos_x = move(pos_y, pos_x, direction)
        if pos_x > max_x:
            max_x = pos_x

    for row in grid.values():
        output = []
        for i in range(-max_x, max_x+1):
            output.append(["W", "B"][row[i]])
        print(output)


def rand7():
    # return sum([random.randint(0,5) for _ in range(7)]) % 7

    while True:
        candidate = random.randint(0, 4)*5 + random.randint(0, 4)
        if candidate < 21:
            return candidate % 7


def pairswithsum(array, k):
    solutions = []
    c = Counter()
    for n in array:
        c[n] += 1
    for value, count in c.items():
        if k - value == value:
            for _ in range(count - 1):
                solutions.append((value, value))
        elif k - value in c and k - value > value:
            for _ in range(count * c[k - value]):
                solutions.append((value, k - value))
    return solutions


@dataclass
class LRUcache:
    maxsize: int
    memory: dict = field(default_factory=dict)
    history: list = field(default_factory=list)
    time: int = 0

    def insert(self, key, value):
        self.time += 1

        usage = [self.time, key, True]
        if self.memory and len(self.memory) >= self.maxsize:
            lastused = heapq.heappushpop(self.history, usage)
            while not lastused[2]:
                lastused = heapq.heappushpop(self.history, usage)
            del self.memory[lastused[1]]
        else:
            heapq.heappush(self.history, usage)
        self.memory[key] = [value, usage]

    def read(self, key):
        self.time += 1
        self.memory[key][1][2] = False
        usage = [self.time, key, True]
        self.memory[key][1] = usage
        heapq.heappush(self.history, usage)
        return self.memory[key][0]


if __name__ == "__main__":
    # print(numberswapper(5,9))
    # print(tictactoe_won([[1,2,1],[0,1,0],[2,0,2]]))
    # print(factorialzeros(29))
    # print(smallestdifference([1,3,15,11,2],[23,127,235,19,8]))
    # print(trickmax(1, 2))
    # print(matches_pattern("abab", "arfdogarfdog"))
    # print(matches_pattern("bbaba", "catcatgocatgo"))
    # print(divingboard(3,5,3))
    # print(divingboard_recursive(3, 5, 3, (0,0)))
    # print(maxlivingpeople([[1921, 1976],[1911, 1959],[1957, 1987]]))
    # print(bestline([[1,1],[2,2],[3,3],[4,4],[1,4],[2,3],[3,5]]))
    # print(subsort([1,2,4,7,10,11,7,12,6,7,16,18,19]))
    # print(contiguoussequence([2,-8,3,-2,4,-10,6,-100,14,2]))
    # print(contiguoussequence([-7,-8,-3,-2,-4,-10]))
    # print(sizeponds([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))
    # print(sumswap([4,1,2,1,1,2], [2,60,3,3]))
    # print(t9(2665))
    # langstonant(61)

    # c = Counter()
    # for _ in range(int(1E5)):
    #     c.update(str(rand7()))
    # print(c)

    # print(pairswithsum([5,1,3,5,4,1,2,7,6], 7))

    # cache = LRUcache(3)
    # cache.insert("ellen", 36)
    # cache.insert("mischa", 42)
    # cache.insert("bronwen", 37)
    # cache.read("ellen")
    # cache.insert("frances", 73)
    pass
