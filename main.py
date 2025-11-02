import pygame
import random
from ui.rectangle import rectangle, heading_rect, control_rect
from ui.rectangle import visual_rect, element_base
from ui.button import Button
from functions import gen_elements, draw_elements
from functions import selection_detials, complexity_detials, selection_details_2
from algorithms.bubble import bubble_sort
from algorithms.insertion import insertion_sort
from algorithms.selection import selection_sort
from algorithms.merge import merge_sort
from algorithms.quick import quick_sort

# --- Global Setup and Constants ---
pygame.init()
clock = pygame.time.Clock()

# Screen Dimensions
SC_WIDTH = 1200
SC_HEIGHT = 1000

# Fonts
font = pygame.font.Font(pygame.font.get_default_font(), 24)
table_title = pygame.font.Font(pygame.font.get_default_font(), 30)
title_font = pygame.font.Font(pygame.font.get_default_font(), 64)
nums = []

# Pygame Setup
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
icon = pygame.image.load('./assets/logo.png')
pygame.display.set_icon(icon)


# Color (High-Contrast Cyberpunk Palette)
NEON_AQUA = (0, 255, 255)    
DARK_GREY = (50, 50, 50)     
NEON_PINK = (255, 0, 255)    
NEON_GREEN = (0, 255, 150)   
DEEP_BLUE = (0, 150, 255)    
SURFACE_BG = (30, 30, 30)    


# Offset
CONTROL_PANEL_OFFSET = (0, 730)

# -------------------- TEXT --------------------
no_of_array = font.render("No. of Element:", True, NEON_AQUA)
num_area = no_of_array.get_rect(center=(830, 105))
head_text = title_font.render("Sorting Visualizer", True, NEON_PINK)
head_area = head_text.get_rect(center=(600, 40))



# UI Surface
heading = pygame.Surface((1190, 80), pygame.SRCALPHA)
visualizer = pygame.Surface((1190, 630), pygame.SRCALPHA)
control_panel = pygame.Surface((1190, 270), pygame.SRCALPHA)


# -------------------- GAME FUNCTIONS --------------------

def shuff(arr):
    """Shuffles the array in place."""
    random.shuffle(arr)
    return arr

# -------------------- BUTTONS --------------------
# Algorithm Btns
algo_btn = []
algo_btn.append(Button("Selection", 33, 20, 200, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : selection_sort(nums, visualizer, visual_rect, screen, clock), avg="O(n²)", best="O(n²)", worst="O(n²)",space="O(1)"))
algo_btn.append(Button("Insertion", 266, 20, 200, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : insertion_sort(nums, visualizer, visual_rect, screen, clock), avg="O(n²)", best="O(n)", worst="O(n²)",space="O(1)"))
algo_btn.append(Button("Bubble", 499, 20, 200, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : bubble_sort(nums, visualizer, visual_rect, screen, clock), avg="O(n²)", best="O(n)", worst="O(n²)",space="O(1)"))
algo_btn.append(Button("Merge", 732, 20, 200, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : merge_sort(nums, visualizer, visual_rect, screen, clock), avg="O(n × log n)", best="O(n × log n)", worst="O(n × log n)",space="O(n)"))
algo_btn.append(Button("Quick", 965, 20, 200, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : quick_sort(nums, visualizer, visual_rect, screen, clock), avg="O(n × log n)", best="O(n × log n)", worst="O(n²)",space="O(n)"))

# Operation Btns
gen_btn = Button("Generate", 732, 150, 200, 30, NEON_PINK, DARK_GREY, NEON_GREEN, NEON_PINK, offset=CONTROL_PANEL_OFFSET, action=gen_elements)
sort_btn = Button("Sort", 732, 200, 433, 30, NEON_PINK, DARK_GREY, NEON_GREEN, NEON_PINK, offset=CONTROL_PANEL_OFFSET)
shuffle_btn = Button("Shuffle",965, 150, 200, 30, NEON_PINK, DARK_GREY, NEON_GREEN, NEON_PINK, offset=CONTROL_PANEL_OFFSET, action= shuff)

# No. of elements btn
num_of_elements = []
num_of_elements.append(Button("30",955, 90, 50, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : 30))
num_of_elements.append(Button("50",1035, 90, 50, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : 50))
num_of_elements.append(Button("80",1115, 90, 50, 30, NEON_PINK, DARK_GREY, NEON_PINK, NEON_GREEN, offset=CONTROL_PANEL_OFFSET, action= lambda : 80))


# -------------------- GAME LOOP --------------------
running = True
while running:

    # --- 1. Timing and Screen Clear ---
    df = clock.tick(60)
    screen.fill((0, 0, 0))

    
    visual_rect()  # Grey frame around visualizer

    # --- 2. Surface Clears (Crucial for Redrawing UI) ---
    # Clear the surfaces to prevent text/graphics overlap
    heading.fill(SURFACE_BG) 
    visualizer.fill(DARK_GREY)
    control_panel.fill(SURFACE_BG)

    # --- 3. Event Handling ---
    events = pygame.event.get()
    for event in events:
        # App quit event
        if event.type == pygame.QUIT:
            running = False
        
        # Button events
        for btn in algo_btn:
            if btn.is_clicked(event):
                # Toggle selection state
                if btn.selected:
                    btn.selected = False
                else:
                    for other_btn in algo_btn:
                        other_btn.selected = False
                    btn.selected = True

        for btn in num_of_elements:
            if btn.is_clicked(event):
                # Toggle selection state
                if btn.selected:
                    btn.selected = False
                else:
                    for other_btn in num_of_elements:
                        other_btn.selected = False
                    btn.selected = True
        
        if gen_btn.is_clicked(event):
            element_btn = next((b for b in num_of_elements if b.selected), None)
            if element_btn and element_btn.action:
                nums = gen_btn.action(element_btn.action())
            else:
                # Default to 30 if no count button is explicitly selected
                nums = gen_btn.action(30)
                # Select the '30' button visually
                if num_of_elements:
                    for other_btn in num_of_elements:
                        other_btn.selected = False
                    num_of_elements[0].selected = True 

        if shuffle_btn.is_clicked(event):
            if nums:
                nums = shuff(nums)

        if sort_btn.is_clicked(event): 
            selected_btn = next((b for b in algo_btn if b.selected), None)
            if selected_btn and selected_btn.action and nums:
                # Execute the sorting algorithm action
                selected_btn.action()



    # --- 4. Drawing Content onto Surfaces (Redrawn every frame) ---

    # Draw the elements onto the visualizer surface
    draw_elements(nums, visualizer) 

    # Complexity Details (Draw only if an algorithm is selected)
    selected_algo_btn = next((b for b in algo_btn if b.selected), None)
    if selected_algo_btn:
        selection_detials(
            control_panel, 
            selected_algo_btn.average, 
            selected_algo_btn.best, 
            selected_algo_btn.worst, 
            selected_algo_btn.space
        )

    # Button Render
    for btn in algo_btn + num_of_elements +[gen_btn, sort_btn, shuffle_btn]:
        btn.draw(control_panel)

    # Text Rendering on Control Panel and Heading
    control_panel.blit(no_of_array, num_area)
    heading.blit(head_text, head_area)

    # --- 5. Blit Surfaces to Main Screen ---
    # Copy the content of the surfaces onto the main screen
    screen.blit(heading, (5, 0))
    screen.blit(visualizer, (5, 90))
    screen.blit(control_panel, (5, 730))

    # --- 6. Draw Frames (ON TOP) ---
    # Draw the decorative rectangles directly onto the screen AFTER the content surfaces have been blitted.
    heading_rect() # White frame around heading
    control_rect() # White frame around control panel

    # --- 7. Update Display ---
    pygame.display.update()

pygame.quit()
