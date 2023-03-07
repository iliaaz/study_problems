from bisect import bisect
from collections import defaultdict


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
    print(sizeponds([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))
