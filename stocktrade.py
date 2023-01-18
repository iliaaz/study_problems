test_input_1 = [10, 7, 5, 8, 11, 9]
test_input_2 = [10, 7, 5, 8, 11, 9, 1, 4, 9, 7, 2, 8]
test_input_3 = [10, 7, 6, 3]
test_input_4 = [5, 7, 9, 1]
test_input_5 = [651]


# Greedy algorithm stores max profit, must execute a trade
def find_maxprofit(price_history):
    if len(price_history) < 2:
        return "At least two prices are required"

    min_value = price_history[0]
    max_delta = price_history[1] - price_history[0]
    for price in price_history:
        if price == min_value:
            continue
        elif price < min_value:
            if max_delta < 0:
                max_delta = max(max_delta, price - min_value)
            min_value = price
        else:
            max_delta = max(max_delta, price - min_value)

    return max_delta


if __name__ == "__main__":
    assert find_maxprofit(test_input_1) == 6
    assert find_maxprofit(test_input_2) == 8
    assert find_maxprofit(test_input_3) == -1
    assert find_maxprofit(test_input_4) == 4
    assert find_maxprofit(test_input_5) == "At least two prices are required"
