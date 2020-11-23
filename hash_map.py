# Course: CS261 - Data Structures
# Assignment: 5
# Student:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        capacity = self.capacity
        hash_function = self.hash_function


        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = hash_function
        self.size = 0

        # for i in range(capacity):
        #     if self.buckets.get_at_index(i).remove()

    def get_at_index(self, index):
        return self.buckets.get_at_index(index)

    def contains(self, index, key):

        return self.buckets.get_at_index(index).contains(key)

    def insert(self, index, key, value):

        return self.buckets.get_at_index(index).insert(key, value)


    def get(self, key: str) -> object:
        """
        TODO: Write this implementation
        """
        for i in range(self.capacity):
            if self.contains(i, key) is not None:
                return self.contains(i, key).value

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map. If given key already exists, the associated value is replaced
        with the new value. If key is not in hash map, a key/value pair should be added.

        need to do: first determine the hash value, calculate the index, then search for hash value in hash table (DA) at index,
         then search for key in the linked list.
        """

        return self.put_helper_w_capacity(key, value, self.capacity)

    def put_helper_w_capacity(self, key, value, capacity):

        index = self.hash_function(key) % capacity

        if index > capacity:  # if the index is more than the capacity, it can't be in the hash table
            return
        elif self.contains(index, key) is not None:  # index is not empty
            pointer = self.contains(index, key)  # find the key
            pointer.value = value
        elif self.get_at_index(index).length() == 0:  # if the head is none, there index is empty
            self.insert(index, key, value)  # can insert directly
            self.size += 1  # increase the size since there is a new value being added
        else:
            self.insert(index, key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        removes a desired key
        """

        for i in range(self.capacity):
            if self.contains(i, key) is not None:
                self.get_at_index(i).remove(key)
                self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Determine if a key is in a hash table
        """

        for i in range(self.capacity):
            if self.contains(i, key) is not None:
                return True
        return False

    def empty_buckets(self) -> int:
        """
        Returns a number of empty buckets in the hash table.
        """
        count = self.capacity

        for i in range(self.capacity):
            if self.get_at_index(i).length() != 0:
                count -= 1

        return count

    def table_load(self) -> float:
        """
        Returns the current hash table load factor, which is lamda = total number of elements in list/buckets in list
        """

        total_number_of_elements = self.size
        buckets_in_list = self.capacity

        lamda = total_number_of_elements/buckets_in_list

        return lamda

    def get_value(self, key, index):

        return self.contains(index, key).value

    def resize_table(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the internal hash table. All existing key / value pairs must remain in
        the new hash map and all hash table links must be rehashed. If new_capacity is less than 1,
        this method should do nothing.
        """
        if new_capacity < 1:
            return
        else:
            new_hash_map = HashMap(new_capacity, self.hash_function)
            old_capacity = self.capacity
            self.resize_helper(new_capacity, old_capacity, new_hash_map)
            self.update(new_hash_map)


    def resize_helper(self, new_capacity, old_capacity, new_hash_map):

        for i in range(old_capacity):
            if self.get_at_index(i).length() != 0:
                myiter = iter(self.buckets.get_at_index(i))
                while True:
                    try:
                        element = next(myiter)
                        key = element.key
                        value = element.value
                        new_hash_map.put_helper_w_capacity(key, value, new_capacity)
                    except StopIteration:
                        break

    def update(self, new_hash_map):
        self.capacity = new_hash_map.capacity
        self.buckets = new_hash_map.buckets
        self.size = new_hash_map.size



    def get_keys(self) -> DynamicArray:
        """
        TODO: Write this implementation
        """

        return DynamicArray()


# BASIC TESTING
if __name__ == "__main__":

    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())


    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:  # delete if I want it to print EVERYTHING
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
        # for i in range(50):  # add this in if I want everything printed
        #     print(i, m.buckets.get_at_index(i))
    #
    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))

    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)
    #
    #
    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))

    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    #
    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - resize negtive")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(-100)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)
        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')
        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
