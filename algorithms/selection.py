from functions import animate_swap

def selection_sort(arr, visualizer, visual_rect, screen, clock):
    """Selection Sort implementation with visualization."""
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Find index of the minimum element

        # Only animate if a swap is necessary
        if min_index != i:
            # Swap the found minimum element with the first unsorted element
            animate_swap(arr, min_index, i, visualizer, visual_rect, screen, clock)

    return arr