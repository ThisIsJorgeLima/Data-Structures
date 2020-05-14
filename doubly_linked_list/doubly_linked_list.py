"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    # method provided

    def remove_from_head(self):
        # # remove the head
        value = self.head.value
        # # implement
        self.delete(self.head)
        return value
        # if self.head is None:
        #     print("DLL already empty")
        #     return none
        # elif self.head.next is None:
        #     deleted = self.head.value
        #     self.head = self.head.value
        #     return deleted
        # else:
        #     deleted = self.head.value
        #     self.head.next.prev = None
        #     self.head = self.head.next
        #     return deleted

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # make a new node
        new_node = ListNode(value, None, None)
        # increment the length
        self.length += 1
        # check if the list is empty or not:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # the new node becomes the head of our list
            # set the current head's previous to the new node
            new_node.prev = self.tail
            # set the new node's next to the current head
            self.tail.next = new_node
            # reassign self.head to point to the new node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # check if the node is the head:
        if node is self.head:
            return None
        # store a reference to the node we're going to move
        value = node.value
        # lets check if its the tail
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # decrement the length
        # don't decrement if list is empty
        self.length -= 1
        # check if head and tail are pointing properly
        if self.head is self.tail:
            # getting rid of single node by = None:
            self.head = None
            self.tail = None
            # check if the node is the head of the list
        elif self.head is node:
            self.head = node.next
            # Let's delete the node:
            node.delete()
            # check to see if node is previous
        elif self.tail is node:
            self.tail = node.prev
            # delete node:
            node.delete()
            # otherwise, there's no additional references we need to update
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # init a variable that will keep track of the largest
        # element we've seen
        max_value = self.head.value
        current = self.head
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value
        # check if its empty
        # if self.head is None and self.tail is None:
        # return None
        # variable track
        # variable max point
        # current_node = self.head
        # max_val = 0
        # while current_node != None:
        #     if current_node.value > max_val:
        #         max_val = current_node.value
        #         # traverse through the list
        #     current_mode = current_node.next
        # return max_val

#         def print_list(self):
#             current = self.head
#             self.temp = []
#             while current:
#                 self.temp.append(current.value)
#                 current = current.next
#             print(self.temp)
#
#
# if __name__ == '__main__':
#     my_list = DoublyLinkedList()
#     my_list.add_to_head(1)
#     my_list.add_to_head(2)
#     my_list.add_to_head(3)
#     my_list.add_to_head(4)
#     my_list.add_to_head(5)
#     my_list.print_list()
#     my_list.move_to_front(my_list.tail)
#     my_list.print_list()
