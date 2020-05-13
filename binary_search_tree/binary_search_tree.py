"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Less then we go left
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # Greater or equal we go right:
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

                # Return True if the tree contains the value
                # False if it does not

    def contains(self, target):
        """
    To search a given key within our
    binary search tree, we should first compare
    with root. If the key is present at the root, we will return root. If key
    is greater than our roots key, we will head right to our subtree of our
     root node.
        """
        if target == self.value:
            return True

        if target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)
        else:
            if not self.left:
                return False
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # will go right of our root until infinity
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # You may use a recursive or iterative approach
        # each node at once
        # Search left
        # Seart right
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        pass

        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
