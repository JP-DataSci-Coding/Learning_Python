class arrayClass:
    # Constructor
    def __init__(self):
        self.length = 0
        self.data = {}

    def get_all(self):
        return self.data

    def get(self, index):
        return self.data[index]

    def push(self, element):
        self.data[self.length] = element

        self.length += 1

        return self.length

    def pop(self):
        # del keyword deletes an object in Python
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]

        self.length -= 1

        return last_item

    def delete(self, index):
        deleted_item = self.data[index]

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]

        self.length -= 1

        return deleted_item


new_array = arrayClass()
new_array.push('Hi')
new_array.push('Bye')
new_array.push('!')
new_array.delete(0)
new_array.pop()
print(new_array.get_all())
