class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = (key, val)

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def print_table(self):
        for index, item in enumerate(self.arr):
            if item is not None:
                print(f"Index {index}: Key = {item[0]}, Value = {item[1]}")

table = HashTable()
table['march 6'] = 130
table['march 1'] = 24
table['dec 17'] = 80

table.print_table()
