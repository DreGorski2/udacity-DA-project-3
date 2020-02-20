
Trying to keep time and space down we need to consider what this trie needs to do and since we know
we're going to need to both search and insert it makes sense to initialize the node with a dict to keep
track of our characters and allow them to point to one another. Determining the time complexity will 
depend on the length of the word that is being searched/inserted *A* and the total number of words we have
in the list *N*. which gives us *O(A * N)*. Worst case is when all words are unique in that they share no
characters in that case we would end up with a space complexity of O(n) since each character would end up
with its own node.
