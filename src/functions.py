import pygame
from ui.rectangle import rectangle

# Color
NEON_AQUA = (0, 255, 255)    
NEON_PINK = (255, 0, 255)    
NEON_GREEN = (0, 255, 150)   
DARK_GREY = (50, 50, 50)     
DEEP_BLUE = (0, 150, 255)

# Constants
BASE_X = 5 # Starting X position for the first bar on the visualizer surface
BASE_Y = 590 # Baseline Y position for the bottom of the bars (approx 630 - 40 margin)
HEIGHT_SCALE = 550 # Max height for a bar

SCREEN_BLIT_AREA = pygame.Rect(5, 90, 1190, 630)

font = pygame.font.Font(pygame.font.get_default_font(), 24)
table_title = pygame.font.Font(pygame.font.get_default_font(), 30)


def gen_elements(nums):
    """Generates a list of numbers from 1 to nums_count + 10."""
    return [n + 10 for n in range(1,nums + 1)]

def draw_elements(nums, visualizer):
    """Draws the current state of the array as vertical bars (standard draw, no specific highlighting)."""
    if not nums:
        visualizer.fill((0, 0, 0, 0))
        return
    
    # Clear the visualizer surface completely (essential for correct redraws)
    visualizer.fill((0, 0, 0, 0))
    
    # Calculate bar dimensions
    bar_height = HEIGHT_SCALE // (len(nums) + 10)
    bar_width = 1000 // len(nums)
    spacing = bar_width + 1
    
    for i, val in enumerate(nums):
        x = BASE_X + i * spacing
        height = val * bar_height
        y = BASE_Y - val * bar_height

        # Draw the bar
        pygame.draw.rect(visualizer, NEON_AQUA, rectangle(x, y, bar_width, height), border_radius=0)

def animate_swap(nums, i, j, visualizer, visual_rect, screen, clock, speed=8):
    """Smoothly swap bar at index i with bar at index j."""
    if i >= len(nums) or j >= len(nums) or i == j:
        return

    # Compute positions
    bar_height = HEIGHT_SCALE // (len(nums) + 10)
    bar_width = 1000 // len(nums)
    spacing = bar_width + 1

    # Compute start and end X positions
    start_x_i = BASE_X + i * spacing
    start_x_j = BASE_X + j * spacing
    distance = start_x_j - start_x_i

    # Determine the number of visual steps for smooth movement
    steps = max(1, abs(distance) // speed)

    # val_i, val_j = nums[i], nums[j]

    for step in range(steps + 1):
        pygame.event.pump()  # keep window responsive
        visualizer.fill((0, 0, 0, 0))

        for k, val in enumerate(nums):
            x = BASE_X + k * spacing
            height = val * bar_height
            y = BASE_Y - height

            # Only move the two swapping bars
            color = NEON_AQUA
            if k == i:
                x = start_x_i + (distance / steps) * step
                color = DEEP_BLUE
            elif k == j:
                x = start_x_j - (distance / steps) * step
                color = DEEP_BLUE



            pygame.draw.rect(visualizer, color, rectangle(x, y, bar_width, height))

        # Redraw base & update screen
        visual_rect()
        # pygame.draw.rect(visualizer, NEON_AQUA, rectangle(BASE_X, BASE_Y, 1000, 5))
        screen.blit(visualizer, (5, 90))
        pygame.display.update(SCREEN_BLIT_AREA)
        clock.tick(60)

    # After animation completes, swap values in list
    nums[i], nums[j] = nums[j], nums[i]

def selection_detials(panel, average, best, worst, space):
    """Draws the complexity table onto the control panel."""
    # Table Structure
    # Complexity
    complexity_surf = table_title.render("Complexity", True, DEEP_BLUE)
    complexity_rect = complexity_surf.get_rect(topleft=(65, 60))
    panel.blit(complexity_surf,complexity_rect)

    # Average Case
    average_surf = font.render("Average Case", True, DEEP_BLUE)
    average_rect = average_surf.get_rect(topleft=(60, 110))
    panel.blit(average_surf,average_rect)

    avg_ans_surf = font.render(average, True, DEEP_BLUE)
    avg_ans_rect = avg_ans_surf.get_rect(topleft=(367, 110))
    panel.blit(avg_ans_surf,avg_ans_rect)

    # Best Case
    best_surf = font.render("Best Case", True, DEEP_BLUE)
    best_rect = best_surf.get_rect(topleft=(60, 150))
    panel.blit(best_surf,best_rect)

    bst_ans_surf = font.render(best, True, DEEP_BLUE)
    bst_ans_rect = bst_ans_surf.get_rect(topleft=(367, 150))
    panel.blit(bst_ans_surf,bst_ans_rect)

    # Worst Case
    worst_surf = font.render("Worst Case", True, DEEP_BLUE)
    worst_rect = worst_surf.get_rect(topleft=(60, 190))
    panel.blit(worst_surf,worst_rect)

    worst_ans_surf = font.render(worst, True, DEEP_BLUE)
    worst_and_rect = worst_ans_surf.get_rect(topleft=(367, 190))
    panel.blit(worst_ans_surf,worst_and_rect)

    # Space Complexity
    space_surf = font.render("Space Complexity", True, DEEP_BLUE)
    space_rect = space_surf.get_rect(topleft=(60, 230))
    panel.blit(space_surf,space_rect)

    space_ans_surf = font.render(space, True, DEEP_BLUE)
    space_ans_rect = space_ans_surf.get_rect(topleft=(367, 230))
    panel.blit(space_ans_surf,space_ans_rect)

    pygame.draw.rect(panel, NEON_GREEN, rectangle(300, 105, 3, 160), border_radius=0)
    pygame.draw.rect(panel, NEON_GREEN, rectangle(34, 140, 450, 3), border_radius=0)
    pygame.draw.rect(panel, NEON_GREEN, rectangle(35, 180, 450, 3), border_radius=0)
    pygame.draw.rect(panel, NEON_GREEN, rectangle(35, 220, 450, 3), border_radius=0)


def complexity_detials(panel, average, best, worst, space):
    """
    Draws the complexity table onto the control panel using a data-driven loop 
    with enhanced aesthetics, addressing the text overflow issue.
    """
    
    # Data structure for the complexity rows (Label, Value, Y position)
    complexity_data = [
        ("Average Case", average, 110),
        ("Best Case", best, 150),
        ("Worst Case", worst, 190),
        ("Space Complexity", space, 230),
    ]
    
    # --- CONSTANTS FOR TABLE LAYOUT ---
    LABEL_X = 60
    VALUE_X = 350 # Adjusted left to give more room for complexity values (was 367)
    LINE_START_X = 35
    LINE_END_X = 450
    VERT_LINE_X = 300
    
    # --- 1. Draw Title ---
    complexity_surf = table_title.render("Complexity", True, DEEP_BLUE)
    panel.blit(complexity_surf, complexity_surf.get_rect(topleft=(65, 60)))

    # --- 2. Draw Rows and Horizontal Separators ---
    for label, value, y_pos in complexity_data:
        # Draw the label (Deep Blue)
        label_surf = font.render(label, True, DEEP_BLUE)
        panel.blit(label_surf, label_surf.get_rect(topleft=(LABEL_X, y_pos)))

        # Draw the value (Neon Aqua)
        value_surf = font.render(value, True, NEON_AQUA)
        panel.blit(value_surf, value_surf.get_rect(topleft=(VALUE_X, y_pos)))
        
        # Draw horizontal separator line (below the row, but not below the last one)
        if y_pos < 230:
            # Use NEON_GREEN line
            pygame.draw.rect(panel, NEON_GREEN, rectangle(LINE_START_X, y_pos + 35, LINE_END_X, 3), border_radius=0)
            
    # --- 3. Draw Vertical Separator ---
    # This separates label column from value column, spanning the row height
    pygame.draw.rect(panel, NEON_GREEN, rectangle(VERT_LINE_X, 105, 3, 160), border_radius=0)

def selection_details_2(panel, average, best, worst, space):
    """Draws a visually clean and symmetrical complexity table on the control panel."""

    # Title
    title_surf = table_title.render("Complexity", True, DEEP_BLUE)
    title_rect = title_surf.get_rect(topleft=(65, 60))
    panel.blit(title_surf, title_rect)

    # Table Data
    entries = [
        ("Average Case", average),
        ("Best Case", best),
        ("Worst Case", worst),
        ("Space Complexity", space)
    ]

    # Table layout settings
    table_x = 50
    table_y = 100
    col1_width = 250
    col2_width = 180
    row_height = 45
    border_thickness = 2

    # Draw table border
    total_width = col1_width + col2_width
    total_height = len(entries) * row_height
    pygame.draw.rect(panel, NEON_GREEN,
                     pygame.Rect(table_x, table_y, total_width, total_height),
                     border_thickness, border_radius=2)

    # Draw horizontal lines
    for i in range(1, len(entries)):
        y = table_y + i * row_height
        pygame.draw.line(panel, NEON_GREEN, (table_x, y), (table_x + total_width, y), border_thickness)

    # Draw vertical line (column divider)
    pygame.draw.line(panel, NEON_GREEN,
                     (table_x + col1_width, table_y),
                     (table_x + col1_width, table_y + total_height),
                     border_thickness)

    # Render each cell text
    for i, (label, value) in enumerate(entries):
        y = table_y + i * row_height + 10  # padding from top

        label_surf = font.render(label, True, DEEP_BLUE)
        panel.blit(label_surf, (table_x + 15, y))  # small left padding

        value_surf = font.render(value, True, DEEP_BLUE)
        value_rect = value_surf.get_rect(right=table_x + total_width - 15, top=y)
        panel.blit(value_surf, value_rect)
