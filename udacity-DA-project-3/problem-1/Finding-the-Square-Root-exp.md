
Was originally thinking about using a simple equation (number ** 0.5) to find the square root
but the time complexity of this algorithm does not satisfy the O(log(n)). Knowing we need to do this in O(log(n)) 
I chose to implement binary search were we start at one and multiply the start position by itself adding 1 to the
start number through each iteration until we get to a point where the start times start is larger or equal to our input number
at which point we return the start number -1 which gives us our floor. Since we're only keeping track of our current
value the space complexity is independent of the input giving us a space complexity of O(1)
