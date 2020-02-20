# Rearrange Array Elements so as to form two number such that their
# sum is maximum. Return these two numbers. You can assume that all
# array elements are in the range [0, 9]. The number of digits in both
# the numbers cannot differ by more than 1. You're not allowed to use
# 'any sorting function that Python provides and the expected time complexity'
#  is O(nlog(n)).

# for e.g. [1, 2, 3, 4, 5]
#
# The expected answer would be [531, 42]. Another expected answer can
# be [542, 31]. In scenarios such as these when there are more than one
# possible answers, return any one.
#
# Here is some boilerplate code and test cases to start with:



def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list or len(input_list) <= 1:
        return input_list
    sorted_list = mergesort(input_list)

    # take even indicies from sorted list and combine them into one int
    even = int(''.join(map(str, sorted_list[::2])))
    # take odd indicies from sorted list and combine them into one int
    odd = int(''.join(map(str, sorted_list[1::2])))
    max_sums = [even, odd]
    return max_sums


def mergesort(input_list):

    # if input_list is 0 or 1 list is already sorted
    if len(input_list) <= 1:
        return input_list

    # else find the mind-point of the list and split it up
    midpoint = len(input_list)//2
    left = input_list[:midpoint]
    right = input_list[midpoint:]

    # recursivly call until condition tell base condition is met
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    # given the two ordered lists, merge them together
    merged = []
    left_index = 0
    right_index = 0

    # iterate over lists until one of the lists has been exhausted
    while left_index < len(left) and right_index < len(right):
        # if the left item is smaller then the right item
        # append the right item to the merged list and
        # increment the right index by one
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index +=1
        # otherwise the right item is smaller so we want to
        # append the left item to the merged list and increment
        # the left index by 1
        else:
            merged.append(left[left_index])
            left_index +=1
    # loop has now been broken so we want to append any leftover items
    # since we know one of the lists is empty and the remaining are sorted
    merged += left[left_index:]
    merged += right[right_index:]

    # this is now the merged list
    return merged



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if output == solution:
        print("Pass")
    elif sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[5], [5]])
test_function([None, None])

