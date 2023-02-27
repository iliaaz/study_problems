from copy import deepcopy


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


def getpath(grid, row, column, path=[], visited = {}):
    if (
        row < 0 or
        column < 0 or
        grid[row][column] is None or
        (row, column) in visited
    ):
        return False

    if (
        (row == 0 and column ==0) or 
        getpath(grid, row-1, column) or 
        getpath(grid, row, column-1)
    ):
        path.append((row, column))
        return path

    visited[(row, column)] = True
    return False


def robotinagrid(grid):
    if grid is None or (len(grid) != len(grid[0])):
        return None
    path = getpath(grid, len(grid)-1, len(grid)-1)
    if path:
        return path
    else:
        return None


def magicindex(array, start, end):
    if start > end:
        return None

    midindex = (end + start)//2
    if array[midindex] == midindex:
        return midindex
    elif array[midindex] > midindex: #magicindex can't be to the right
        return magicindex(array, start, midindex-1)
    else: #magicindex can't be to the left
        return magicindex(array, midindex+1, end)


def movedisc(towers, origin, destination):
    newtowers = deepcopy(towers)
    disc = newtowers[origin].pop()
    newtowers[destination].append(disc)
    return newtowers


def towerstohashable(towers):
    return (
        "".join([str(disc) for disc in towers[0]]),
        "".join([str(disc) for disc in towers[1]]),
        "".join([str(disc) for disc in towers[2]])
        )


def findsolution(towers, solution=[], visitedstates={}):
    # print(visitedstates)
    if towerstohashable(towers) in visitedstates:
        return False

    visitedstates[towerstohashable(towers)] = True

    n = len(towers[0]+towers[1]+towers[2])
    # print(towers)
    if towers[0] == list(reversed(range(0,n))):
        return True

    if len(towers[2]) > 0:
        if len(towers[0]) > 0:
            if towers[2][-1] < towers[0][-1]:
                if findsolution(movedisc(towers,2,0)):
                    solution.append((0,2))
                    return solution
        else:
            if findsolution(movedisc(towers,2,0)):
                solution.append((0,2))
                return solution
        if len(towers[1]) > 0:
            if towers[2][-1] < towers[1][-1]:
                if findsolution(movedisc(towers,2,1)):
                    solution.append((1,2))
                    return solution
        else:
            if findsolution(movedisc(towers,2,1)):
                solution.append((1,2))
                return solution
    if len(towers[1]) > 0:
        if len(towers[0]) > 0:
            if towers[1][-1] < towers[0][-1]:
                if findsolution(movedisc(towers,1,0)):
                    solution.append((0,1))
                    return solution
        else:
            if findsolution(movedisc(towers,1,0)):
                solution.append((0,1))
                return solution
        if len(towers[2]) > 0:
            if towers[1][-1] < towers[2][-1]:
                if findsolution(movedisc(towers,1,2)):
                    solution.append((2,1))
                    return solution
        else:
            if findsolution(movedisc(towers,1,2)):
                solution.append((2,1))
                return solution
    if len(towers[0]) > 0:
        if len(towers[1]) > 0:
            if towers[0][-1] < towers[1][-1]:
                if findsolution(movedisc(towers,0,1)):
                    solution.append((1,0))
                    return solution
        else:
            if findsolution(movedisc(towers,0,1)):
                solution.append((1,0))
                return solution

        if len(towers[2]) > 0:
            if towers[0][-1] < towers[2][-1]:
                if findsolution(movedisc(towers,0,2)):
                    solution.append((2,0))
                    return solution
        else:
            if findsolution(movedisc(towers,0,2)):
                solution.append((2,0))
                return solution
    return False


def towersofhanoi(n):
    solution = findsolution([[],[],list(reversed(range(0,n)))])
    if solution:
        return solution
    else:
        return None


def findpermutations(uniquechars, permutations=None):
    if not uniquechars:
        return permutations

    newchar = uniquechars[0]
    if permutations is None:
        permutations = [newchar]
    else:
        newpermutations  = []
        for string in permutations:
            for i in range(len(string)+1):
                newpermutation = string[:i]+newchar+string[i:]
                if newpermutation not in newpermutations:
                    newpermutations.append(newpermutation)
        permutations = newpermutations

    return findpermutations(uniquechars[1:], permutations)


def parens(n, leftparen, rightparen, parenstring, solutions):
    # if leftparen > n or rightparen > n or rightparen > leftparen:
    #     return solutions
    if leftparen == n and rightparen == n:
        solutions.append(parenstring)
        return solutions

    if leftparen < n:
        solutions = parens(n, leftparen+1, rightparen, parenstring + "(", solutions)
    if rightparen < n and rightparen < leftparen:
        solutions = parens(n, leftparen, rightparen+1, parenstring + ")", solutions)

    return solutions


def coins(n, quarters, dimes, nickels, pennies, solutions = [], visited = {}):
    if n < 0 or (quarters, dimes, nickels, pennies) in visited:
        return
    visited[(quarters, dimes, nickels, pennies)] = True
    if n == 0:
        solutions.append((quarters, dimes, nickels, pennies))
        return
    if n >= 25:
        coins(n-25, quarters+1, dimes, nickels, pennies)
    if n >= 10:
        coins(n-10, quarters, dimes+1, nickels, pennies)
    if n >= 5:
        coins(n-5, quarters, dimes, nickels+1, pennies)
    coins(n-1, quarters, dimes, nickels, pennies+1)

    return solutions


def checkforconflicts(placementcolumns, newrow, newcol):
    for row, column in enumerate(placementcolumns):
        if abs(newrow - row) == abs(newcol - column):
            return True
    return False


def eightqueens(rowtofill, placementcolumns, solutions=[]):
    if rowtofill == 8:
        solutions.append(placementcolumns)
        return solutions

    potentialcolumns = set(range(8)) - set(placementcolumns)    
    for col in potentialcolumns:
        if not checkforconflicts(placementcolumns, rowtofill, col):
            eightqueens(rowtofill+1, placementcolumns+[col])
    return solutions


if __name__ == '__main__':
    # print(fibonacci_bottom(333))
    # print(fibonacci_top(333))

    # print(triplestep(3))

    # print(powerset([3,7,9,1]))

    # print(recursivemultiply_On(9, 3))
    # print(recursivemultiply_logn(9, 3))

    # grid = [[True,None,None,True],[True,True,True,True],[True,None,None,True],[None,True,True,True]]
    # print(robotinagrid(grid))
    
    # print(magicindex([-10,-5, 0, 3, 9], 0, 4))

    # print(towersofhanoi(2))

    # print(findpermutations("abbd"))

    # print(parens(3, 0, 0, "", []))

    # print(coins(25,0,0,0,0))

    print(eightqueens(0, []))