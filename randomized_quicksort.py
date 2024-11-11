import random

def partition_random(arr, start, end):
    # Select a random pivot index and swap with the end element
    rand_pivot_idx = random.randint(start, end)
    arr[rand_pivot_idx], arr[end] = arr[end], arr[rand_pivot_idx]
    
    # Use the last element as the pivot
    pivot_value = arr[end]
    smaller_index = start - 1
    
    # Reorganize elements based on pivot
    for current_index in range(start, end):
        if arr[current_index] < pivot_value:
            smaller_index += 1
            arr[smaller_index], arr[current_index] = arr[current_index], arr[smaller_index]
    
    # Place the pivot at its correct position
    arr[smaller_index + 1], arr[end] = arr[end], arr[smaller_index + 1]
    return smaller_index + 1

def quicksort_random(arr, start, end):
    if start < end:
        # Partition around a random pivot and get new pivot index
        pivot_index = partition_random(arr, start, end)
        
        # Recursively apply Randomized Quicksort to the subarrays
        quicksort_random(arr, start, pivot_index - 1)
        quicksort_random(arr, pivot_index + 1, end)

# Helper function to sort array with Randomized Quicksort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr  # No sorting needed for empty or single-element arrays
    quicksort_random(arr, 0, len(arr) - 1)
    return arr

# Main function to execute the Randomized Quicksort on a sample array
def main():
    # Generate a random array of integers
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Original array:", arr)
    
    # Sort the array using Randomized Quicksort
    sorted_arr = randomized_quick_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()


