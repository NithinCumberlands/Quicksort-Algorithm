import random
import time

# Optimized Deterministic Quicksort: Using median-of-three pivot
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # Median of first, middle, and last element as pivot
    first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, middle, last])[1]  # Take the median of these three
    pivot_index = arr.index(pivot)  # Find the index of the pivot
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]  # Swap pivot with the last element

    # Partition the array
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Random pivot selection
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]  # Swap pivot with last element
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return randomized_quicksort(less) + [pivot] + randomized_quicksort(greater)

# Measure the running time of an algorithm
def measure_time(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    return time.time() - start_time

# Function to test Quicksort with various input sizes
def test_quicksort():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        arr = random.sample(range(size), size)  # Generating a random array
        print(f"Array size: {size}")
        
        # Time deterministic quicksort
        time_deterministic = measure_time(quicksort, arr)
        print(f"Deterministic Quicksort time: {time_deterministic:.5f} seconds")
        
        # Time randomized quicksort
        time_randomized = measure_time(randomized_quicksort, arr)
        print(f"Randomized Quicksort time: {time_randomized:.5f} seconds")

# Test different input distributions (sorted and reverse sorted)
def test_input_distributions():
    sizes = [100, 1000, 5000, 10000]
    
    # Sorted array test
    for size in sizes:
        sorted_arr = list(range(size))
        print(f"Sorted Array (size {size})")
        time_sorted_deterministic = measure_time(quicksort, sorted_arr)
        print(f"Deterministic Quicksort time: {time_sorted_deterministic:.5f} seconds")
        time_sorted_randomized = measure_time(randomized_quicksort, sorted_arr)
        print(f"Randomized Quicksort time: {time_sorted_randomized:.5f} seconds")
    
    # Reverse-sorted array test
    for size in sizes:
        reverse_sorted_arr = list(range(size, 0, -1))
        print(f"Reverse Sorted Array (size {size})")
        time_reverse_sorted_deterministic = measure_time(quicksort, reverse_sorted_arr)
        print(f"Deterministic Quicksort time: {time_reverse_sorted_deterministic:.5f} seconds")
        time_reverse_sorted_randomized = measure_time(randomized_quicksort, reverse_sorted_arr)
        print(f"Randomized Quicksort time: {time_reverse_sorted_randomized:.5f} seconds")

# Main function to run the tests
if __name__ == "__main__":
    # Test both versions of Quicksort on random arrays
    test_quicksort()
    
    # Test the performance of Quicksort on different input distributions (sorted and reverse sorted)
    test_input_distributions()
