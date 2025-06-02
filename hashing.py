class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists (chaining)

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))  # Append (key, value) pair

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Not found

    def printhashtable(self):
        """Prints the entire hash table in a readable format."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Usage
ht = HashTable(10)
ht.insert(15, "Data1")
ht.insert(25, "Data2")  # Collision with 15
ht.insert(5, "Data3")
ht.insert(35, "Data4")  # Another collision with index 5

print(ht.search(15))  # Output: "Data1"
print(ht.search(25))  # Output: "Data2"
print("\nHash Table Contents:")
ht.printhashtable()
