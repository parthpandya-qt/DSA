class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Update value if key exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def remove(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i} -> {bucket}")

ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 5)
ht.insert("orange", 7)
ht.insert("apple", 15)  # Update value for "apple"

print("Hash Table:")
ht.display()

print("\nValue for 'banana':", ht.get("banana"))

ht.remove("banana")
print("\nAfter removing 'banana':")
ht.display()
