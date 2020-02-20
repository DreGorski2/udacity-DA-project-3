
# In this problem, we will look for smallest and largest
# integer from a list of unsorted integers.
# The code should run in O(n) time. Do not use Python's
# inbuilt functions to find min and max.



def get_min_max(ints):
    """
       Return a tuple(min, max) out of list of unsorted integers.

       Args:
          ints(list): list of integers containing one or more integers
       """
    if not isinstance(ints, list):
        return None, None

    # Define variables for min and max value and initialize to None
    min_value = None
    max_value = None

    for index, value in enumerate(ints):

        if index == 0:
            min_value = value
            max_value = value

        # if the current index value is less then the current value we have assigned for min_value
        # update the current value to be that min value and vize versa for the max value
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value

    return min_value, max_value


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Test Case 1 Random Array")
print("Expected:" "Pass")
print("Output:"+" Pass" if ((0, 9) == get_min_max(l)) else "Output:" + " Fail")
print("---------------")
print("Test Case 2 string input")
print("Expected:" "Pass")
print("Output:"+" Pass" if ((None, None) == get_min_max('Cat')) else "Output:" + " Fail")
print("---------------")
print("Test Case 3 Array with 1 Element")
print("Expected:" "Pass")
print("Output:"+" Pass" if ((1, 1) == get_min_max([1])) else "Output:" + " Fail")
print("---------------")
print("Test Case 4 Empty Array")
print("Expected:" "Pass")
print("Output:"+" Pass" if((None, None) == get_min_max([])) else "Output:" + " Fail")
print("---------------")

