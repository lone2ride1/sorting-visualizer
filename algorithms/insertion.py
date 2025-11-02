from functions import animate_swap

def insertion_sort(arr, visualizer, visual_rect, screen, clock):
    """Insertion Sort implementation with visualization."""
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            # animate_swap performs the swap on the array 'arr'
            animate_swap(arr, j, j - 1, visualizer, visual_rect, screen, clock)
            j -= 1