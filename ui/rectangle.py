import pygame

pygame.init()


# Varibles
SC_WIDTH = 1200
SC_HEIGHT = 1000
WHITE = (255, 255, 255)
GREY = (128,128,128)

# Color (Defining minimal colors needed for borders here)
NEON_AQUA = (0, 255, 255) 
DARK_GREY = (50, 50, 50)  

screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))

def rectangle(x, y, width, height):
    """Simple wrapper for pygame.Rect."""
    return pygame.Rect(x, y, width, height)

def heading_frame(scene):
    """Draws the frame around the heading area."""
    return pygame.draw.rect(scene, NEON_AQUA, rectangle(5, 0, 1190, 80), width=4, border_bottom_left_radius=15, border_bottom_right_radius=15)

def visual_frame(scene):
    """Draws the background for the visualization area."""
    return pygame.draw.rect(scene, DARK_GREY, rectangle(5, 90, 1190, 630), border_radius=15)

def control_frame(scene):
    """Draws the frame around the control panel area."""
    return pygame.draw.rect(scene, NEON_AQUA, rectangle(5, 730, 1190, 270), width=4, border_top_left_radius=15, border_top_right_radius=15)

# UI Rectangle
heading_rect = lambda : pygame.draw.rect(screen, NEON_AQUA, rectangle(5, 0, 1190, 80), width=4, border_bottom_left_radius=15, border_bottom_right_radius=15)
visual_rect = lambda : pygame.draw.rect(screen, DARK_GREY, rectangle(5, 90, 1190, 630), border_radius=15)
control_rect = lambda : pygame.draw.rect(screen, NEON_AQUA, rectangle(5, 730, 1190, 270), width=4, border_top_left_radius=15, border_top_right_radius=15)
# element_base = lambda : pygame.draw.rect(screen, (0, 0, 255), rectangle(100, 700, 1000, 5), border_radius=0)
element_base = lambda : pygame.draw.rect(screen, (0, 0, 255), rectangle(100, 110, 1000, 49), border_radius=0)