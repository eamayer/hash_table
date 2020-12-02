# Course: CS261 - Data Structures
# Assignment: 5
# Student: Elizabeth Mayer
# Description: Create a min_heap data structure with common functionality


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        add a node to a heap
        """

        self.heap.append(node)
        i = self.heap.length() - 1  # since node got appended at end, initial index is 1 less than length

        self.bubble_up(i)

    def parent(self, i):
        """identifies parent node"""

        return (i-1)//2

    def left(self, i):
        """identifies the left child node"""

        return 2*i + 1

    def right(self, i):
        """identifies the right child node"""

        return 2*(i+1)

    def bubble_up(self, i):
        """helper function to be able to ensure that we maintain the heap property when adding nodes"""

        # starts with 2nd to last node and checks that it is smaller
        # than its parents and if it is not, swaps with the parent repeatedly until
        # it is no longer smaller than it's parent
        p = self.parent(i)  # identifies the parent node of i
        while i > 0 and self.heap.get_at_index(i) < self.heap.get_at_index(p):
            self.heap.swap(i, p)
            i = p
            p = self.parent(i)

    def get_min(self) -> object:
        """
        Return the minimum value in heap, which is always index 0
        """
        if self.heap.length() == 0:
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes the min value from the head
        """
        length = self.heap.length()  # finds length of the heap
        x = self.get_min()    # finds the min to be able to return
        self.heap.set_at_index(0, self.heap.get_at_index(length-1))  # takes the value at end and duplicates at front
        self.heap.pop()  # removes the last value which is now a duplicate of the first value
        length -= 1  # makes it one shorter
        self.trickle_down(0)  # re-organizes the heap
        return x

    def trickle_down(self, i):
        """helper function to remove_min to maintain heap property"""
        n = self.heap.length()

        # moves the new root element downwards. Repeatedly compare the element to the 2 children, if
        # it is the smallest of the 3, then the heap property remains. Otherwise, swaps the elements and continue
        while i >= 0:
            j = -1
            r = self.right(i)
            if r < n and self.heap.get_at_index(r) < self.heap.get_at_index(i):
                l = self.left(i)
                if self.heap.get_at_index(l) <= self.heap.get_at_index(r):
                    j = l
                else:
                    j = r
            else:
                l = self.left(i)
                if l < n and self.heap.get_at_index(l) < self.heap.get_at_index(i):
                    j = l
            if j >= 0:
                self.heap.swap(i, j)
            i = j

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a heap from a given array making sure it follows heap property. Replaces the existing heap array
        with new heap array
        """
        da_length = da.length()  # find the length of the desired array

        self.heap = DynamicArray()  # create empty array

        # copies the array values from the desired array to object's array
        for i in range(da_length):
            value = da.get_at_index(i)
            self.heap.append(value)

        starting_index = (da_length//2) - 1  # finding the fist node that could have children

        for j in range(starting_index, -1, -1):  # organize the heap to meet heap requirements
            self.trickle_down(j)


# BASIC TESTING
if __name__ == '__main__':


    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)
    #

    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    # print("\nPDF - get_min example raise exception")
    # print("-----------------------")
    # h = MinHeap()
    # print(h)
    # print(h.get_min(), h.get_min())
    #

    #
    # print("\nPDF - remove_min example 2")
    # print("--------------------------")
    # h = MinHeap([4, 9, 6, 17, 26, 8, 16, 19, 69, 32, 93, 55, 50])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    #


    #
    # print("\nPDF - remove_min example 2")
    # print("--------------------------")
    # h = MinHeap([-984, -962, -961, -954, -954, -918, -942, -943, -924, -932, -954, -829, -866, -922, -792])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    #
    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    # print("\nPDF - remove_min example raise exception")
    # print("--------------------------")
    # h = MinHeap()
    # # while not h.is_empty():
    # #     print(h, end=' ')
    # # print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 500, 200, 10, 100, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
