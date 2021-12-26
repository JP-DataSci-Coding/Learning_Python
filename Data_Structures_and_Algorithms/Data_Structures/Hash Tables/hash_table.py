class hashTableClass:

    def __init__(self, size):
        # Creates a list of size elements of None
        self.data = [None] * size

    # A very basic hash function
    def hash(self, key):
        size_of_data = len(self.data)

        if size_of_data == 0:
            return hash(key) % 1
        else:
            return hash(key) % size_of_data

    def set(self, key, value):
        # Add a value to the array using its key as the index
        index = self.hash(key)

        # We need to check if there is no value already in the
        # index
        if self.data[index] is not None:
            for key_value in self.data[index]:
                # If key is found, then update
                # its current value to the new value.
                if key_value[0] == key:
                    key_value[1] = value
                    break
            else:
                # If no values are found for the index
                # then add new value
                self.data[index].append([key, value])
        else:
            # This index is empty. We should initiate
            # a list and append our key value pair to it
            self.data[index] = []
            self.data[index].append([key, value])

    def get(self, key):
        index = self.hash(key)

        if self.data[index] is not None:
            for key_value in self.data[index]:
                if key_value[0] == key:
                    return key_value[1]
        else:
            raise KeyError()

    def remove(self, key):
        index = self.hash(key)

        if self.data[index] is not None:
            for i in range(len(self.data[index])):
                if self.data[index][i][0] == key:
                    self.data[index].pop(i)
        else:
            raise KeyError()

    def keys(self):
        # Checks if any elements are None in list
        none_count = self.data.count(None)

        keys = []

        if none_count == len(self.data):
            return None
        else:
            for i in range(len(self.data)):
                if self.data[i] is not None:
                    for reference in self.data[i]:
                        keys.append(reference[0])
                else:
                    continue

        return keys


hash_table = hashTableClass(5)

hash_table.set(1, 'Hello')
hash_table.set(2, 'Bye')
hash_table.get(1)
print(hash_table.keys())

print(hash_table.data)

hash_table.remove(2)

print(hash_table.data)
