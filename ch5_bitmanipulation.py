
def addtrailingones(bitnumber, onestoadd):
    for _ in range(onestoadd):
        bitnumber = bitnumber * 2 + 1
    return bitnumber


def insertion(n1, n2, i, j):
    clearmask = addtrailingones((2 ** (len(bin(n1)) - 1-j-i) - 1) << (j-1), i)
    setmask = n2 << i
    return (n1 & clearmask) | setmask


def realtobinary(realnumber):
    remainder = realnumber
    place = 1
    binarystring = []

    while remainder > 0 and len(binarystring) < 32:
        if remainder >= 2**(-place):
            binarystring.append(str(1))
            remainder = remainder - 2**(-place)
        else:
            binarystring.append(str(0))
        place += 1

    # print(binarystring)
    if len(binarystring) == 32:
        raise Exception("ERROR")
    return "".join(binarystring)


def flipbittowin(num):
    bin_num = bin(num)
    current_streak = 0
    last_streak = 0
    max_superstreak = 1
    for i in range(2, len(bin_num)):
        print(bin_num[i], current_streak, last_streak, max_superstreak)
        if bin_num[i] == "1":
            current_streak += 1
        else:
            if last_streak + current_streak + 1 > max_superstreak:
                max_superstreak = last_streak + current_streak + 1
            if i < len(bin_num)-1:
                if bin_num[i+1] == "0":
                    last_streak = 0
                else:
                    last_streak = current_streak
            current_streak = 0
    if last_streak + current_streak + 1 > max_superstreak:
        max_superstreak = last_streak + current_streak + 1
    return max_superstreak


if __name__ == '__main__':
    # print(bin(insertion(0b10110011000, 0b10011, 2, 6)))
    # print(realtobinary(.625))

    print(flipbittowin(1775))
    print(flipbittowin(3535))
