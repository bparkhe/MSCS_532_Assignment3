# MSCS_532_Assignment3

# Randomized Quicksort Script

This script implements Randomized Quicksort, which is a variation of the Quicksort algorithm that chooses a pivot randomly to improve average-case performance. This implementation uses in-place sorting, meaning the input array is modified directly.

## Files
- `randomized_quicksort.py`: The main script with the Randomized Quicksort implementation and a test run.

## Requirements
- Python 3.x
- No external libraries are required.

## How to Run the Script

1. Save the code into a file named `randomized_quicksort.py`.
2. Open a terminal or command prompt and navigate to the directory containing `randomized_quicksort.py`.
3. Run the script using Python:

   ```bash
   python randomized_quicksort.py
   
## Expected Output
    Original array: [35, 12, 74, 53, 29, 96, 7, 61, 83, 45]
    Sorted array: [7, 12, 29, 35, 45, 53, 61, 74, 83, 96]

# Chained Hash Table Implementation

This project implements a hash table with separate chaining for collision resolution. The hash table dynamically resizes to maintain an efficient load factor, ensuring optimal performance for insert, search, and delete operations.

## Files
- `chained_hash_table.py`: The main script containing the `ChainedHashTable` class, the hash table operations, and a `main` function to test the performance.

## Features
The `ChainedHashTable` class provides the following functionalities:
- **Add (Insert)**: Adds a key-value pair to the hash table, resizing if necessary to maintain the load factor.
- **Find (Search)**: Retrieves the value associated with a given key.
- **Remove (Delete)**: Removes a key-value pair from the hash table.

## How It Works
This implementation uses separate chaining to handle hash collisions. Each slot in the hash table contains a list (referred to as a "chain") of key-value pairs. If multiple keys hash to the same slot, they are stored in this chain.

The hash table automatically resizes (doubles its capacity) when the load factor (ratio of elements to slots) exceeds `0.7`. This resizing ensures that the chains stay short, maintaining efficient operation times for large data sets.

## Requirements
- Python 3.x
- No external libraries required

## How to Run the Script

1. Save the code into a file named `chained_hash_table.py`.
2. Open a terminal or command prompt and navigate to the directory containing `chained_hash_table.py`.
3. Run the script with the following command:

   ```bash
   python chained_hash_table.py
## Expected Output
   Insertion time for 1000 items: 0.0123 seconds
   Table capacity after insertion: 40
   Load factor after insertion: 0.50
   Search time for 1000 items: 0.0087 seconds
   Deletion time for 1000 items: 0.0092 seconds
   Final table capacity: 40
   Final load factor: 0.00
