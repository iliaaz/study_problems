
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


def nextnumber_bf(n):
    ones = bin(n).count("1")

    next_higher = n + 1
    while bin(next_higher).count("1") != ones:
        next_higher += 1

    next_lower = n - 1
    while bin(next_lower).count("1") != ones:
        next_lower -= 1

    return next_lower, bin(next_lower), next_higher, bin(next_higher)


def conversion_str(n1, n2):
    flips = 0
    for bit in bin(n1 ^ n2)[2:]:
        if bit == "1":
            flips += 1
    return flips


def conversion_bitshift(n1, n2):
    flips = 0
    binsolution = n1 ^ n2
    while binsolution:
        flips += binsolution & 1
        binsolution >>= 1
    return flips


def conversion_bitmath(n1, n2):
    flips = 0
    binsolution = n1 ^ n2
    while binsolution:
        binsolution = binsolution & (binsolution - 1)
        flips += 1
    return flips


def pairwiseswap(n):
    oddmask = 0b01010101010101010101010101010101
    evenmask = 0b10101010101010101010101010101010
    return ((n >> 1) & oddmask) + ((n << 1) & evenmask)


# def drawline(screen, width, x1, x2, y):
#     start_offset = x1 % 8
#     first_fullbyte = x1 // 8
#     if start_offset != 0:
#         first_fullbyte += 1

#     end_offset = x2 % 8
#     last_fullbyte = x2 // 8
#     if end_offset != 7:
#         last_fullbyte -= 1

#     if start_offset != 0:
#         start_mask = (1 << (8 - start_offset + 1)) - 1
#     if end_offset != 0:
#         end_mask = (0xFF << (8 - end_offset)) & 0xFF

#     for i in range(first_fullbyte, last_fullbyte + 1):
#         screen[y * (width / 8) + i] = 0xFF


if __name__ == '__main__':
    # print(bin(insertion(0b10110011000, 0b10011, 2, 6)))
    # print(realtobinary(.625))

    # print(flipbittowin(1775))
    # print(flipbittowin(3535))

    # print(nextnumber_bf(0b101))

    # print(conversion_str(29, 15))
    # print(conversion_bitshift(29, 15))
    # print(conversion_bitmath(29, 15))

    print(bin(pairwiseswap(0b100110)))
