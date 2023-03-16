from collections import defaultdict
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


if __name__ == "__main__":
    # print(addnumbers(18,3))
    # print(subtractnumbers(14, 7))

    # first10 = [1,2,3,4,5,6,7,8,9,10]
    # print(shuffle(first10))
    # print(randomset(first10, 3))

    # print(missingnumber([0,2,1,3]))
    print(lettersandnumbers(["a","a","a","a",1,1,"a",1,1,"a","a",1,"a","a",1,"a","a","a","a"]))

