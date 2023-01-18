# https://www.interviewcake.com/question/python3/product-of-other-numbers

test_input_1 = [1, 7, 3, 4]
test_input_2 = [9, -3, 7]
test_input_3 = [2, -3, 0, 4]


def get_products_of_all_ints_except_at_index(ints):
    product_array = [1] * len(ints)

    for i in range(1, len(ints)):
        product_array[i] = ints[i - 1] * product_array[i - 1]

    accumulated_product = 1
    for i in range(len(ints) - 2, -1, -1):
        accumulated_product *= ints[i + 1]
        product_array[i] *= accumulated_product

    return product_array


if __name__ == "__main__":
    assert get_products_of_all_ints_except_at_index(test_input_1) == [84, 12, 28, 21]
    assert get_products_of_all_ints_except_at_index(test_input_2) == [-21, 63, -27]
    assert get_products_of_all_ints_except_at_index(test_input_3) == [0, 0, -24, 0]
