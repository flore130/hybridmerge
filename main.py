import matplotlib.pyplot as plt
import sorting
import random_list
import wait

# Define range of n values and k values for testing

#precise efficiency
n_values = list(range(0, 251, 5))  
k_values = [5, 15, 35, 50, 75, 100, 150]  # Range of k values to test


#super high level view efficiancy
# n_values = list(range(0, 751, 25))  
# k_values = [35, 75, 100, 150, 200]  # Range of k values to test

#mega super high level view efficiancy
# n_values = list(range(0, 2000, 25))  
# k_values = [35, 75, 100, 150, 200]  # Range of k values to test


# Lists to store timing results
merge_sort_times = []
insertion_sort_times = []
hybrid_sort_times = {k: [] for k in k_values}  # Store timings for each k

# Run tests for each n and k value
for n in n_values:
    data = random_list.generate_random_list(n, seed=42)  # Use a fixed seed for reproducibility
    
    # Timing for Merge Sort
    merge_time = wait.time_sort(sorting.merge_sort, data, number=100)
    merge_sort_times.append(merge_time)
    
    # Timing for Insertion Sort
    insertion_time = wait.time_sort(sorting.insertion_sort, data, number=100)
    insertion_sort_times.append(insertion_time)
    
    # Timing for Hybrid Sort with different values of k
    for k in k_values:
        hybrid_time = wait.time_sort(lambda arr: sorting.hybrid_merge_sort(arr, k), data, number=100)
        hybrid_sort_times[k].append(hybrid_time)

    print(f"n={n}: Merge Sort={merge_time:.6f}s, Insertion Sort={insertion_time:.6f}s")

# Plotting results
plt.figure(figsize=(12, 8))

# Plot Merge Sort and Insertion Sort times
plt.plot(n_values, merge_sort_times, label='Merge Sort', marker='o')
plt.plot(n_values, insertion_sort_times, label='Insertion Sort', marker='s')

# Plot Hybrid Sort times for each k
for k, times in hybrid_sort_times.items():
    plt.plot(n_values, times, label=f'Hybrid Sort (k={k})', linestyle='--')

plt.xlabel('Input Size (n)')
plt.ylabel('Average Time (seconds)')
plt.title('Hybrid Merge Sort vs. Merge Sort vs. Insertion Sort Performance')
plt.legend()
plt.grid(True)
plt.savefig('hybrid_sorting_performance.png')
plt.show()
