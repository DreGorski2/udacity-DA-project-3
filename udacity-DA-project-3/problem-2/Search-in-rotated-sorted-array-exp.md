
Knowing we need to adhere to a time complexity of O(log(n)) I chose to use binary search to 
cut the array in half so we can rule out half of the items in the array each time which 
allows us to more efficiently find our answer. space complexity for this problem is 
independent of the input variables and only requires that we're keeping track of pointers making 
the space complexity for this problem O(1)