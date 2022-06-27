import time
import pygame
import wintheme


pygame.init()
screen = pygame.display.set_mode((640, 480))

wm_info = pygame.display.get_wm_info()
hwnd = int(wm_info.get('window'))
theme = wintheme.get_system_theme()
result = wintheme.set_window_theme(hwnd, theme)
pygame.display.set_caption(
    f'System Theme: {wintheme.theme_to_string[theme]}, Result: {wintheme.error_to_string[result]}'
)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
    time.sleep(1 / 20)

pygame.quit()
