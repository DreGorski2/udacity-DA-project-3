# Find the square root of the integer without using any Python library.
# You have to find the floor value of the square root.
#
# For example if the given number is 16, then the answer would be 4.
# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
#
# The expected time complexity is O(log(n))
#

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number <= 0 or number == 1):
        return number
    start = 1
    result = 1
    while result <= number:
        start +=1
        result = start * start

    return start -1
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (789 == sqrt(622521)) else "Fail")
print("Pass" if (-1 == sqrt(-1)) else "Fail")