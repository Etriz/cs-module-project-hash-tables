class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.num_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        load factor = num elements / num slots

        Implement this.
        """
        # Your code here
        return self.num_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for k in key:
            hash = (hash * 33) + ord(k)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        new_entry_node = HashTableEntry(key, value)
        index = self.hash_index(key)
        list_entry_node = self.table[index]

        # check to see if index is empty
        if list_entry_node is None:
            self.table[index] = new_entry_node
            self.num_items += 1
            self.check_if_needs_resize()
            return

        # if index is not empty
        while list_entry_node.next is not None and list_entry_node.key != key:
            list_entry_node = list_entry_node.next
        # overwrite if key already exists
        if list_entry_node.key == key:
            list_entry_node.value = value
        # or add new entry to tail if key doesnt exist
        else:
            list_entry_node.next = new_entry_node
            self.num_items += 1
            self.check_if_needs_resize()
        return

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        list_entry_node = self.table[index]
        prev_node = None

        if list_entry_node is None:
            print(f"Key not found")
            return

        while list_entry_node.next is not None and list_entry_node.key != key:
            prev_node = list_entry_node
            list_entry_node = list_entry_node.next

        if list_entry_node.key == key:
            # if we find it at head
            if prev_node is None:
                self.table[index] = list_entry_node.next
            else:
                prev_node.next = list_entry_node.next

            self.num_items -= 1
            self.check_if_needs_resize()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        list_entry_node = self.table[index]
        # return none if no list is found at index
        if list_entry_node is None:
            return None

        # look through list to find node with key
        while list_entry_node.next is not None and list_entry_node.key != key:
            list_entry_node = list_entry_node.next

        if list_entry_node.key == key:
            return list_entry_node.value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        current_table = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity

        for item in current_table:
            if item is not None:
                self.put(item.key, item.value)

    def check_if_needs_resize(self):
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

        # elif self.get_load_factor() < 0.2:
        #     if self.capacity > MIN_CAPACITY * 2:
        #         self.resize((self.capacity + 1) // 2)


if __name__ == "__main__":
    ht = HashTable(8)

    print(f"start with {ht.get_num_slots()} slots")
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    # print(ht.get_load_factor())
    # print(f"{ht.get_num_slots()} slots")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")
    # print(ht.get("line_1"))
    # print(f"{ht.get_num_slots()} slots")


"""
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    # ht.resize(1024)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
"""
