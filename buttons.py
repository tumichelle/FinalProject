import pygame

#pygame.init()


# display_width = 700
# display_height = 391
# game_display = pygame.display.set_mode((display_width,display_height))

#checks if button is clicked, does action
def button_check(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button['rect'].collidepoint(mouse):
        if click[0] == 1 and button['action']:
            button['action']()

#changes button when moused over
def button_draw(button, font, width, height, display):
    mouse = pygame.mouse.get_pos()
    if button['rect'].collidepoint(mouse):
        color = button['ic']
    else:
        color = button['ac']

    pygame.draw.rect(game_display, color, button['rect'])

    image, rect = textWhite(button['msg'], font)
    rect.center = button['rect'].center
    game_display.blit(image, rect)


def textWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def textRed(text, font):
    textStart = font.render(text, True, red)
    return textStart, textStart.get_rect()
