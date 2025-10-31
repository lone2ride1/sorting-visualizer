import pygame 

pygame.init()

# Color Palatte
NEON_AQUA = (0, 255, 255)
NEON_PINK = (255, 0, 255)
NEON_GREEN = (0, 255, 150)
VIOLET = (120, 0, 120)
DARK_GREY = (50, 50, 50)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 50, 100)
DARK_RED = (250, 0, 0)


font = pygame.font.Font(pygame.font.get_default_font(), 24)

class Button:
	"""Represents an interactive button in the UI."""
	def __init__(self, text, x, y, width, length, base_color, hover_txt_color, hover_color, selection_color, action=None, offset=(0,0), avg=None, best=None, worst=None, space=None):
		self.text = text
		self.rect_btn = pygame.Rect(x, y, width, length)
		self.base_color = base_color
		self.hover_txt_color = hover_txt_color
		self.selection_color = selection_color
		self.hover_color = hover_color
		self.action = action
		self.offset = offset
		self.selected = False
		self.average = avg
		self.best = best
		self.worst = worst
		self.space = space


	def draw(self, surface):
		"""Draws the button onto the given surface, handling hover and selected states."""
		mouse_x, mouse_y = pygame.mouse.get_pos()
		# Adjust mouse position relative to the surface's offset
		mouse_x -= self.offset[0]
		mouse_y -= self.offset[1]
		is_hover = self.rect_btn.collidepoint(mouse_x, mouse_y)

		# Determine the color based on state
		if self.selected:
			color = self.selection_color
		elif is_hover:
			color = self.hover_color
		else:
			color = self.base_color

		# Draw button background
		pygame.draw.rect(surface, color, self.rect_btn, border_radius=5)
		# Draw button border
		pygame.draw.rect(surface, BLACK, self.rect_btn, width=2, border_radius=5)

		# Determine text color
		if self.selected and is_hover:
			txt_color = DARK_RED
		elif self.selected:
			txt_color = BLACK
		elif is_hover:
			txt_color = self.hover_txt_color
		else:
			txt_color = NEON_AQUA

		txt = font.render(self.text, True, txt_color)
		txt_rect = txt.get_rect(center=self.rect_btn.center)

		surface.blit(txt, txt_rect)
		return is_hover


	def is_clicked(self, event):
		"""Checks if the button was clicked."""
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_x -= self.offset[0]
			mouse_y -= self.offset[1]
			return self.rect_btn.collidepoint(mouse_x, mouse_y)