# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
# You're not allowed to use any sorting function that Python provides.
# #
# # Note: O(n) does not necessarily mean single-traversal.
# For e.g. if you traverse the array twice, that would still be an O(n)
#  solution but it will not count as single traversal.
# #
# # Here is some boilerplate code and test cases to start with:

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list:
        return

    next_pos_0 = 0
    end_index = len(input_list) - 1

    start_index = 0

    while start_index <= end_index:
        if input_list[start_index] == 0:
            input_list[start_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            start_index += 1
        elif input_list[start_index] == 2:
            input_list[start_index] = input_list[end_index]
            input_list[end_index] = 2
            end_index -= 1
        else:
            start_index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([None])