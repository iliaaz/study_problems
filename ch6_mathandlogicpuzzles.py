def heavypill():
    return ("Number the bottles 1 to 20. Take a number of pills equal to"
    "the number of the bottle and weigh all 210 pills together. The"
    "# of the heavy bottle = (total weight - 210) / .1")


def basketball():
    return """The probability of making one shot is p. The probability of
    making 2 shots out of 3 is:
    P011 + P11 + P101 = (1-p)*p*p + p*p + p*(1-p)*p 
    = p^2-p^3 + p^2 + p^2-p^3 = p^2(3 - 2p)

    The probability is better for one shot when p > p^2(3 - 2p)
    p^2(3 - 2p) - p < 0
    -2p^2 + 3p - 1 < 0
    (-2p+1)(p-1) < 0 => p < 1/2

    If p < 1/2, take one shot. If > 1/2, take 2 shots out of three.
    """


def dominos():
    return """A chess board has an equal number of black and white squares.
    Removing two opposing corners means removing two squares of one colour.
    Any domino must cover two adjacent squares: one black and one white. It's
    impossible to cover a board with unequally coloured squares with dominos.
    """

def antswalking():
    return """Collision occurs when any two ants walk in opposite directions.
    Therefore, collision does not occur when all ants walk in the same
    direction. If there are only two directions, the probability that they
    all walk in one direction is (1/2)^n, where n is the number of vertices.
    The probability that they all walk in the same direction is double that:
    2*1/2^n. For a triangle, that is 2*(1/8) = 1/4. The probably of collision
    is 1-1/4 = 3/4.
    """

def jugs():
    return """Fill the 5L jug. Use it to fill the 3L jug: 2/5, 3/3.
    Empty the 3L jug. Pour the 2L from the 5L just in to the 3L jug: 0/5, 2/3
    Fill the 5L jug. Use the 5L jug to fill the 3L jug: 4/5, 3/4.
    """


def blueeyedisland():
    return """Prove by induction. If there were only one blue-eyed person,
    they would see no blue eyes and, knowing that there had to be one,
    realize that they had blue eyes and leave. Knowing that, anyone who
    sees one person with blue eyes knows that there are at most two people
    (if they have blue eyes) and, if no one leaves on the first day, realize
    that they have blue eyes and both people will leave on the second day.
    If there were three people with blue eyes and no one left on the second day,
    they would know that there are three people and all would leave on the
    third day. It would thus take n days for n people with blue eyes to leave.
    """

def apocolypse():
    return """There is 1/4 chance of one boy, 1/8 chance of 2 boys, 1/16
    chance of 3 boys, etc. Summing all these to infinity equals 1.
    Alternatively, consider the amalgam of all these births: a sequence of
    boys and girls, each with a 50/50 chance.
    """

def eggdrop():
    return """Generally, we want to tackle this by using one eggs to find
    the group of floors where an eggs will break and then the second egg
    to determine on exactly which floor this occurs. Optimizing for the worst
    case, we want to balance the drops between these two stages. If we go
    up by groups of ten, for example, we could require 20 drops if it only
    breaks at floor 100. Ideally, we start at floor x and ascend by x-1 floors
    for every group: x + (x-1) + ... + 1 = 100 => x(x+1)/2 = 100 => x = 13.5
    x = 14 provides better performance because the 14th drop would bring you to
    floor 99.
    """


def onehundredlockers():
    return """Lockers are open when they have an odd number of factors.
    Only perfect squares will have this because it's root will represent
    a single a divisor. There are ten perfect squares from 1-100 (1-10 squared)
    so there will be ten lockers open.
    """


def poison():
    return """There are 1000 bottles and thus every bottle can be represented
    by a ten digit binary number (2^10 = 1024). Encoding each bottle value
    into binary, distrbute the drops accordingly over the ten strips. On Day 7,
    the strips that show poison correspond to the binary value of the poison
    bottle.
    """


if __name__ == '__main__':
    print("I'm better at math and logic puzzles than I am at codingg.")
