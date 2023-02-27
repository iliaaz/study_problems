from bisect import bisect


def numberswapper(n1, n2):
    n1 ^= n2
    n2 ^= n1
    n1 ^= n2

    return n1, n2


def tictactoe_won(board):
    for i in range(3):
        if (
            (board[i][0] == board[i][1] and board[i][0] == board[i][1]) or
            (board[0][i] == board[1][i] and board[0][i] == board[2][i])
            ):
            return True
    if (
        board[0][0] == board[1][1] and board[0][0] == board[2][2] or
        board[2][0] == board[1][1] and board[2][0] == board[0][2]
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
        if insertionindex < len(smaller) and abs(smaller[insertionindex] - num) < smallestdifference:
            smallestdifference = abs(smaller[insertionindex] - num)
    return smallestdifference


if __name__ == "__main__":
    # print(numberswapper(5,9))
    # print(tictactoe_won([[1,2,1],[0,1,0],[2,0,2]]))
    # print(factorialzeros(29))
    print(smallestdifference([1,3,15,11,2],[23,127,235,19,8]))