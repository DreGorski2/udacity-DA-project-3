

# A RouteTrie will store our routes and their associated handlers
class RouteTrieNode(object):
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path):
        if path not in self.children:
            self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, block, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path in block:
            node.insert(path)
            node = node.children[path]

        node.handler = handler

    def find(self, block):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path in block:
            if path not in node.children:
                return None
            node = node.children[path]

        return node.handler

class Router:
    def __init__(self, root_handler, not_found_handler):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, full_path, handler):
    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
        path = self.split_path(full_path)
        self.router.insert(block=path, handler=handler)

    def lookup(self, raw_path):
    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        path = self.split_path(raw_path)

        if len(path) == 0:
            return self.router.handler

        search = self.router.find(block=path)

        if search is None:
            return self.not_found_handler
        else:
            return search

    def split_path(self, raw_path):
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
        result_temp = raw_path.split(sep='/')
        return [element for element in result_temp if element != '']



# create the router and add a route
router = Router("root handler" ,
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about" , "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))# should print 'not found handler' or None if you did not implement one

