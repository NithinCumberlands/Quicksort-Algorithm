import random
import time
from quicksort import quicksort, randomized_quicksort  # Assuming quicksort.py is in the same directory

# Function to measure the running time of an algorithm
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
    print("Testing on random arrays:")
    # Test both versions of Quicksort on random arrays
    test_quicksort()
    
    print("\nTesting on sorted and reverse sorted arrays:")
    # Test the performance of Quicksort on different input distributions (sorted and reverse sorted)
    test_input_distributions()
