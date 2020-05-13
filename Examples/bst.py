class BSTnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
        def insert(self, value):
            pass

    # Return True if the tree contains the value
    # False if it does not
        def contains(self, target):
            # when we start searching, self will be the root
            # compare the target against self
            #
            # Criteria for returning False: we know we need to go in dir
            # but there's nothing in the left or right direction
            if target == self.value:
                return True
            if target < self.value:
                # go left if left is a BSTNode
                if not self.left:
                    return False
                return self.left.contains(target)
            else:
                # go right if right is a BSTNode
                if not self.right:
                    return False
                return self.right.contains(target)

        # Return the maximum value found in the tree
        def get_max(self):
            pass

        # Call the function 'fn' on the value of each node
        def for_each(self, fn):
            pass
