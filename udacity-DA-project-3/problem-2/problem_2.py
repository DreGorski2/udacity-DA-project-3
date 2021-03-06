# You are given a sorted array which is rotated at some random pivot point.
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must
# be in the order of O(log n).
#
# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

# Binary Search Algorithm
# find index of pivot element divide the array into two halfs


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1
    while start_index <= end_index:

        mid_index = (start_index + end_index) // 2
        if number == input_list[mid_index]:
            return mid_index
        if input_list[start_index] < input_list[mid_index]:
            if input_list[start_index] <= number <= input_list[mid_index]:
                end_index = mid_index-1
            else:
                start_index = mid_index+1
        else:
            if input_list[start_index] <= number <= input_list[mid_index]:
                start_index = mid_index+1
            else:
                end_index = mid_index-1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[],0])
test_function([[1],1])

