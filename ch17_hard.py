from collections import defaultdict
import heapq
from random import randint, sample


def addnumbers(n1, n2):
    answer = []

    carryover = 0
    while n1 or n2 or carryover:
        digit_n1 = n1 % 2
        digit_n2 = n2 % 2
        
        answer.append(str(digit_n1 ^ digit_n2 ^ carryover))
        carryover = (digit_n1 and digit_n2) or (digit_n1 and carryover) or (digit_n2 and carryover)

        n1 >>= 1
        n2 >>= 1
    return int("".join(reversed(answer)), 2)


def addnumbers(n1, n2):
    if not n2:
        return n1

    justsum = n1 ^ n2
    justcarry = (n1 & n2) << 1
    return addnumbers(justsum, justcarry)


def subtractnumbers(n1, n2):
    if not n2:
        return n1
    justsum = n1 ^ n2
    justcarry = (~n1 & n2) << 1
    return subtractnumbers(justsum, justcarry)


def shuffle(array):
    length = len(array)
    for i in range(length):
        swapindex = randint(0, length-1)
        array[i], array[swapindex] = array[swapindex], array[i]
    return array


def randomset(array, n):
    return sample(array, n)


def randomset(array, n):
    returnarray = []
    for _ in range(n):
        randindex = randint(0, len(array) - 1)
        returnarray.append(array[randindex])
        del array[randindex]
    return returnarray


def missingnumber(array):
    indexcap = (int(len(array)**.5)+1)**2 - 1
    array += [i for i in range(len(array)+1, indexcap)]
    print(array)
    missing = 0
    for element in array:
        missing ^= element
    return missing


def lettersandnumbers(array):
    difference = defaultdict(list)
    lettercount = 0
    numbercount = 0
    for index, char in enumerate(array):
        if type(char) is str:
            lettercount += 1
        if type(char) is int:
            numbercount += 1
        difference[numbercount - lettercount].append(index)

    maxrange_start = 0
    maxrange_end = 0
    for diff, indices in difference.items():
        if indices[-1] - indices[0] > maxrange_end - maxrange_start:
            maxrange_end = indices[-1]
            maxrange_start = indices[0]
    # return difference
    return (maxrange_start, maxrange_end-1)


def majorityelement(array):
    subarray_start = 0
    while subarray_start < len(array):
        majoritycandidate = array[subarray_start]
        candidatecount = 0
        for i in range(subarray_start, len(array)):
            if array[i] == majoritycandidate:
                candidatecount += 1
            else:
                candidatecount -= 1
            subarray_start = i + 1
            if candidatecount == 0:
                majoritycandidate = None
                break

    # print(array.count(majoritycandidate))
    if array.count(majoritycandidate)/len(array) > .5:
        return majoritycandidate
    else:
        return None


def build_circustower(lastperson, peopleavailable, tallesttower):
    if lastperson:
        peopleavailable = [person for person in peopleavailable if person[0] <= lastperson[0] and person[1] <= lastperson[1]]

    if not peopleavailable:
        return tallesttower

    if (
        len(peopleavailable) > 1 and
        peopleavailable[0][0] >= peopleavailable[1][0] and 
        peopleavailable[0][1] >= peopleavailable[1][1]
        ):
        tallesttower = build_circustower(peopleavailable[0], peopleavailable[1:], tallesttower+1)
    else:
        results = []
        for i in range(len(peopleavailable)):
            results.append(build_circustower(peopleavailable[i], peopleavailable[:i] + peopleavailable[i+1:], tallesttower+1))
        tallesttower = max(results)   

    return tallesttower


def build_circustower(height_weight_pairs):
    if not height_weight_pairs:
        return 0
    # sort on second dimension in decreasing order
    height_weight_pairs.sort(key=lambda x: -x[1])
    # then, problem is lis in first dimension
    dp = [1 for _ in range(len(height_weight_pairs))]
    for i in range(1, len(height_weight_pairs)):
        # look at the elements in the range [0,i-1] (does not include i)
        choices = [1]
        for j in range(0, i):
            if height_weight_pairs[i][0] < height_weight_pairs[j][0]:
                # then feasible candidate
                choices.append(1 + dp[j])
        dp[i] = max(choices)
    return max(dp)
    

# kth element such that: e = 3^a * 5^b * 7^c 
# 1, 3, 5, 7, 9, 15, 25, 27, 35
# (0,0,0), (1,0,0), (0,1,0), (0,0,1), (2,0,0), (1,1,0), (1,0,1), (0,2,0), (3,0,0), (0,1,1)
def kthmultiple(k):
    if k == 0:
        return 1
    candidates = {}
    candidates[3] = [3]
    candidates[5] = [5]
    candidates[7] = [7]

    index = 0
    while index < k:
        minvalue = min(candidates[3][0], candidates[5][0], candidates[7][0])
        if candidates[3][0] == minvalue:
            candidates[3] = candidates[3][1:]
            candidates[3].append(minvalue * 3)
            candidates[5].append(minvalue * 5)
            candidates[7].append(minvalue * 7)
        if candidates[5][0] == minvalue:
            candidates[5] = candidates[5][1:]
            candidates[5].append(minvalue * 5)
            candidates[7].append(minvalue * 7)
        if candidates[7][0] == minvalue:
            candidates[7] = candidates[7][1:]
            candidates[7].append(minvalue * 7)
            
        index += 1

    return minvalue


if __name__ == "__main__":
    # print(addnumbers(18,3))
    # print(subtractnumbers(14, 7))

    # first10 = [1,2,3,4,5,6,7,8,9,10]
    # print(shuffle(first10))
    # print(randomset(first10, 3))

    # print(missingnumber([0,2,1,3]))
    # print(lettersandnumbers(["a","a","a","a",1,1,"a",1,1,"a","a",1,"a","a",1,"a","a","a","a"]))

    # print(majorityelement([1,3,1,2,1,3,1,3,1]))

    # input = [(25, 75), (75, 25), (25, 25), (100,100), (50,60), (65, 55)]
    # print(build_circustower(None, sorted(input, reverse=True), 0))
    # print(find_max_people(input))

    print(kthmultiple(12))

