import random
import time

class ChainedHashTable:
    def __init__(self, initial_slots=10):
        self.num_slots = initial_slots
        self.num_elements = 0
        self.table = [[] for _ in range(self.num_slots)]

    def _compute_hash(self, key):
        # Simple hash calculation with modulus operation for slot indexing
        return hash(key) % self.num_slots

    def add(self, key, value):
        index = self._compute_hash(key)
        chain = self.table[index]
        
        # Check if key already exists; update if it does
        for idx, (k, v) in enumerate(chain):
            if k == key:
                chain[idx] = (key, value)
                return
        
        # Key not found, add new key-value pair
        chain.append((key, value))
        self.num_elements += 1
        
        # Resize if load factor exceeds threshold
        if self.num_elements / self.num_slots > 0.7:
            self._expand_table()

    def find(self, key):
        index = self._compute_hash(key)
        chain = self.table[index]
        
        # Search through the chain at computed index
        for k, v in chain:
            if k == key:
                return v  # Return value if key is found
        return None  # Key not found

    def remove(self, key):
        index = self._compute_hash(key)
        chain = self.table[index]
        
        # Search through chain and delete key-value pair if key exists
        for idx, (k, v) in enumerate(chain):
            if k == key:
                del chain[idx]
                self.num_elements -= 1
                return True  # Key found and deleted
        return False  # Key not found

    def _expand_table(self):
        # Double the table capacity and rehash all existing entries
        new_slots = self.num_slots * 2
        new_table = [[] for _ in range(new_slots)]
        
        for chain in self.table:
            for key, value in chain:
                new_index = hash(key) % new_slots
                new_table[new_index].append((key, value))
        
        self.num_slots = new_slots
        self.table = new_table

# Main function to test the hash table performance
def main():
    # Initialize hash table
    hash_table = ChainedHashTable()

    # Define the number of elements for testing
    element_count = 1000

    # Measure insertion time
    start = time.time()
    for i in range(element_count):
        hash_table.add(f"item{i}", i)
    end = time.time()
    print(f"Insertion time for {element_count} items: {end - start:.4f} seconds")
    print(f"Table capacity after insertion: {hash_table.num_slots}")
    print(f"Load factor after insertion: {hash_table.num_elements / hash_table.num_slots:.2f}")

    # Measure search time for existing elements
    start = time.time()
    for i in range(element_count):
        _ = hash_table.find(f"item{i}")
    end = time.time()
    print(f"Search time for {element_count} items: {end - start:.4f} seconds")

    # Measure deletion time
    start = time.time()
    for i in range(element_count):
        hash_table.remove(f"item{i}")
    end = time.time()
    print(f"Deletion time for {element_count} items: {end - start:.4f} seconds")

    # Final capacity and load factor after deletions
    print(f"Final table capacity: {hash_table.num_slots}")
    print(f"Final load factor: {hash_table.num_elements / hash_table.num_slots:.2f}")

if __name__ == "__main__":
    main()

