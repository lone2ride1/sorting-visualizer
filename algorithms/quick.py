from functions import animate_swap

def quick_sort(arr, visualizer, visual_rect, screen, clock):
    """Quick sort with visualized swaps."""
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    # Animate swap and update array
                    animate_swap(arr, i, j, visualizer, visual_rect, screen, clock)

        # Swap pivot (arr[high]) with the element at i+1
        if i + 1 != high:
            # Animate swap and update array
            animate_swap(arr, i + 1, high, visualizer, visual_rect, screen, clock)
        
        return i + 1

    def quick_sort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

    # Start quick sort on the whole array
    quick_sort_rec(0, len(arr) - 1)
    
    # Final redraw
    # draw_elements(arr, visualizer)
    return arr
