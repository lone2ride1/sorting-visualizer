from functions import animate_swap, draw_elements

import pygame

# Define colors used for dynamic visualization (relying on colors defined in visualizer_app.py)
# NOTE: These are defined here for the merge_sort function's internal drawing logic.
NEON_AQUA = (0, 255, 255) 
NEON_PINK = (255, 0, 255)    
DEEP_BLUE = (0, 150, 255)


# Constants pulled from functions.py for calculation clarity (Assumes constants from functions.py)
BASE_X = 5 
BASE_Y = 590
HEIGHT_SCALE = 550
# Define the area of the visualizer on the screen for optimized updates
SCREEN_BLIT_AREA = pygame.Rect(5, 90, 1190, 630) 

def merge_sort(arr, visualizer, visual_rect, screen, clock):
    """Merge sort implementation with enhanced visualization."""
    
    # Helper function to manually draw the current state with specific colors
    def _draw_merge_state(arr, visualizer, left, right, placed_index=None):
        from ui.rectangle import rectangle # Import here to avoid circular dependency issues
        
        visualizer.fill((0, 0, 0, 0)) # Clear the surface
        
        # Calculate bar dimensions
        max_val = (len(arr) + 10) 
        bar_height_unit = HEIGHT_SCALE // max_val
        bar_width = 1000 // len(arr)
        spacing = bar_width + 1
        width = max(1, bar_width - 1)

        # Process Pygame events to keep the window responsive during sorting
        pygame.event.pump() 

        for i, val in enumerate(arr):
            x = BASE_X + i * spacing
            height = val * bar_height_unit
            y = BASE_Y - height
            
            color = NEON_AQUA
            
            # 1. Highlight the active merging range (Blue)
            if left <= i <= right:
                color = DEEP_BLUE

            # 2. Highlight the element just placed (Red)
            if i == placed_index:
                color = NEON_PINK
            
            pygame.draw.rect(visualizer, color, rectangle(x, y, width, height), border_radius=0)

        # Update screen to show the new visual state
        visual_rect() # Redraw the visualizer frame
        screen.blit(visualizer, (5, 90)) # Blit the updated surface
        pygame.display.update(SCREEN_BLIT_AREA) # Update only the visual area
        clock.tick(60) # Control the speed (slows the sorting process down)


    def merge(arr, left, mid, right):
        """Merges two sorted sub-arrays: arr[left...mid] and arr[mid+1...right]."""
        
        # Copy data to temp arrays L[] and R[]
        L = arr[left : mid + 1]
        R = arr[mid + 1 : right + 1]

        i = j = 0   # Initial index of first and second subarrays
        k = left    # Initial index of merged subarray

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            
            # --- Visualization Update: Show placed bar in Red and active segment in Blue ---
            _draw_merge_state(arr, visualizer, left, right, k)
            # --- End Visualization Update ---
            
            k += 1

        # Copy the remaining elements of L[]/R[], if any
        while i < len(L):
            arr[k] = L[i]
            # Show placement of remaining element
            _draw_merge_state(arr, visualizer, left, right, k) 
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            # Show placement of remaining element
            _draw_merge_state(arr, visualizer, left, right, k) 
            j += 1
            k += 1
            
    def merge_sort_rec(arr, left, right):
        """Recursive function to perform merge sort (Division Phase)."""
        if left >= right:
            return

        mid = (left + right) // 2
        merge_sort_rec(arr, left, mid)
        merge_sort_rec(arr, mid + 1, right)
        # Conquer Phase (where the merging and visualization happens)
        merge(arr, left, mid, right)

    # Start merge sort on the whole array
    merge_sort_rec(arr, 0, len(arr) - 1)
    
    # Final redraw (all white bars)
    draw_elements(arr, visualizer)
    return arr