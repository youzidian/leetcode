import sys
import pygame
import settings
import ship

class Game():
    """My very first game"""
    def run_game(self):
        # new a setting object
        game_setting = settings.Settings()
        #  init the game and create the screen
        pygame.init()
        screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_hight))
        pygame.display.set_caption("Alien Invation")
        # give it a background color
        bg_color = game_setting.bg_color
        my_ship = ship.Ship(screen)
        # create a ship
        # ship = ship.Ship()
        # start the main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.fill(bg_color)
            my_ship.blitme()
            # here refresh the display inside the while loop
            pygame.display.flip()

# init the game
Game().run_game()