from functions import animate_swap

def bubble_sort(arr, visualizer, visual_rect, screen, clock):
    """Bubble Sort implementation with visualization."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # animate_swap performs the swap on the array 'arr'
                animate_swap(arr, j, j + 1, visualizer, visual_rect, screen, clock)
                swapped = True
        # Optimization: If no two elements were swapped by inner loop, then the array is sorted
        if not swapped:
            break