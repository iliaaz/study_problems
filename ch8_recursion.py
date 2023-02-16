def fibonacci_bottom(num):
    prev_fnum = 0
    current_fnum = 1

    for _ in range(num - 1):
        new_fnum = prev_fnum + current_fnum
        prev_fnum = current_fnum
        current_fnum = new_fnum
    return new_fnum


def fibonacci_top(num, memo={}):
    if num == 1 or num == 0:
        return num

    if (num-1) in memo:
        fnum_minusone = memo[num-1]
    else:
        fnum_minusone = fibonacci_top(num-1)
        memo[num-1] = fnum_minusone

    if (num-2) in memo:
        fnum_minustwo = memo[num-2]
    else:
        fnum_minustwo = fibonacci_top(num-2)
        memo[num-2] = fnum_minustwo

    return fnum_minustwo + fnum_minusone


def triplestep(numberofsteps):
    if numberofsteps == 0:
        return 1

    if numberofsteps > 2:
        return (
            triplestep(numberofsteps-3) +
            triplestep(numberofsteps-2) +
            triplestep(numberofsteps-1)
            )
    elif numberofsteps == 2:
        return triplestep(numberofsteps-2) + triplestep(numberofsteps-1)
    elif numberofsteps == 1:
        return triplestep(numberofsteps-1)


def powerset(superset, memo={}):
    result = []
    for i in range(len(superset)):
        subset = superset[0:i]+superset[i+1:]
        if subset:
            subsetstring = "".join([str(num) for num in subset])
            if subsetstring not in memo:
                result.append(subset)
                result.extend(powerset(subset))
                memo[subsetstring] = 1
    return result


def recursivemultiply_On(num1, num2, sum=0):
    if num2 > 0:
        return recursivemultiply_On(num1, num2-1, sum+num1)
    else:
        return sum


def recursivemultiply_logn(num1, num2):
    smaller = min(num1, num2)
    larger = max(num1, num2)

    if smaller == 0:
        return 0
    elif smaller == 1:
        return larger

    halfofsmaller = smaller >> 1
    halfproduct = recursivemultiply_logn(larger, halfofsmaller)
    if smaller % 2 == 0:
        return halfproduct + halfproduct
    else:
        return halfproduct + halfproduct + larger


if __name__ == '__main__':
    # print(fibonacci_bottom(333))
    # print(fibonacci_top(333))

    # print(triplestep(3))

    # print(powerset([3,7,9,1]))

    # print(recursivemultiply_On(9, 3))
    print(recursivemultiply_logn(9, 3))
