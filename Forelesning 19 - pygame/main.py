import pygame
import sys
from avatar import Avatar


# Game class. Game instance is an object of this class
class Game:
    # Game-class constructor. Configures game screen/window and creates relevant variables
    def __init__(self):
        pygame.init()

        # Configure screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Game!")

        # Define background color
        self.bg_color = (230,230,230)

        # Creates avatar object
        self.avatar = Avatar(self)

    # The game's run method. Handles the game's main loop.
    def run_game(self):
        while True:
            # Check events
            self.check_events()

            # Update screen elements
            self.update_screen()

            # Updates the game's current frame
            pygame.display.flip()

    # Method that handles events
    def check_events(self):
        # Iteratively handles all events at a given time/frame
        for event in pygame.event.get():
            # Quit the game by closing the window
            if event.type == pygame.QUIT:
                sys.exit()
            # Press down a key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.avatar.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.avatar.moving_left = True
                if event.key == pygame.K_UP:
                    self.avatar.jumping_up = True
                '''
                if event.key == pygame.K_DOWN:
                    self.avatar.jumping_down = True
                '''
            # Less go of a key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.avatar.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.avatar.moving_left = False
                '''
                if event.key == pygame.K_UP:
                    self.avatar.jumping_up = False
                if event.key == pygame.K_DOWN:
                    self.avatar.jumping_down = False
                '''

    # Method that updates screen elements
    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.avatar.update()
        self.avatar.draw()


# Create and run the game
game = Game()
game.run_game()