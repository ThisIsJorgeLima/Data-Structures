
class node:
    def __init__(self, data=None):
        """
        where we will be storing  the past data point.
        """

        self.data = data
        """
        This is where will be storing the pointer to the next node.
        """
        self.next = None  # constructor initializing to none


"""
Next data structure is our linked list class. Which is our
wrapper that wraps over the node class. This is just going
to be a sublcass of the linked list.
"""


class linked_list:
    def __init__(self):
        """
        We want to have our head node available inside of the linked list
        the head node is never going to contain any actual data, and it's
        not going to be indexable the user won't be able to access this
        head node.simply used as a placeholder to allow us to point to the
        first element in the list.
        """

        self.head = node()

    def append(self, data):
        # We're gonna be creating a new node of the class node
        # and passing the data into that.
        # This will set the data going inside of the node
        new_node = node(data)
        # now will be creating a variable to store the node
        # that we're currently looking at
        cur = self.head
        # iterating while the next element of the current node
        # is not equal to none
        while cur.next != None:  # if cond is not None:
            # just traverse through the list
            cur = cur.next
        # now were at the last element of the list
        # we can set the next node equal
        cur.next = new_node

        """
        Next were going to mplement is a function to figure out the
        length of our linked list. Which is useful if you're trying
        to manage the nodes in the list or to figure out how large the data
        structure is that we are working with.
        """
        # not passing any parameters
        # only the instance of the class

    def length(self):
        # create another variable to point to our
        # current node.
        cur = self.head
        total = 0
        while cur.next != None:  # if cond is not
                # incrementing the total
            total += 1
            # traversing to the next node
            cur = cur.next
            # once we're done will be exiting
            # you'll know because the next node
            # will be equal to none
            return total

            # Next will be creating a helper function
            # to display the current contents of our list

    def display(self):
        elems = []
        # set a new variable for our crrent node
        cur_node = self.head
        # traversing over the nodes
        while cur_node.next != None:  # if cond is not
            # set the current node equal to the next node
            cur_node = cur_node.next
            # then append the data of the current node
            # to our list of elements
            elems.append(cur_node.data)
            print(elems)


# my_list = linked_list()

# my_list.display()
# my_list.append(1)
# my_list.append(2)
# my_list.display()

# extractor function
# which will allow us to pull out a data point
# at a certain index from our linked list


    def get(self, index):
        if index >= self.length():
            print("ERROR 'Get' Index out of range!")
            return None
        # creating a variable to contain
        # the current index
        cur_idx = 0
        cur_node = self.head
        while True:
            # incrementing current node by setting the current node
            # equal to the next node
            cur_code = cur_node.next
            # here we're going to check if the current index is equal
            # to the index that was provided by the user
            if cur_idx == index:
                return cur_node.data
                cur_idx += 1


# # helper function
# my_list = linked_list()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)

# my_list.display()
#******************#
#*****HELP********#
#**^^ABOVE^^*****#

# print("element at 2nd index: %d" % my_list.get(2)

# implementing in our linked lis
# erase function to erase a node at a
# certain provided index so

    def erase(self, index):
        print("ERROR: 'Erase' Index out of range!")
        return
        cur_idx = 0
        cur_node = self.head
        # starting our loop:
        while True:
            # saving the current node
            # as our last node:
            last_node = cur_node
            """
            When we erase a node we have to
            do a little bit of bookkeeping to make sure
            after we've erased three the next node
            in two points to the appropriate spot at four
            so last node equals current node.
            """
            # increment current node by setting it
            # equal to the next node
            cur_node = cur_node.next
            # checking to see if were at the index that
            # the user provided
            if cur_idx == index:
                last_node.next = cur_node.next
            # effectively this is going to be a racing current mode
                return
            cur_idx += 1

            # adding some helper code to make sure our erase function
            # works properly
my_list = linked_list()
# append some data
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
# erase element at index one
my_list.erase(1)

my_list.display()
