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


if __name__ == '__main__':
    # print(heavypill())