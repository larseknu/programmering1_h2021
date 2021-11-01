import pygame


# Avatar class that is used to create avatars
class Avatar:
    # Avatar-class constructor. Configures the avatar in relation to the game
    def __init__(self, game):
        # Get the screen configuration and rectangle from the game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load image and get its rectangle
        self.image = pygame.image.load("mario.png")
        self.rect = self.image.get_rect()

        # Specify the avatars starting position (middle of the bottom of the screen)
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags. Signals what movement state the avatar is currently in
        self.moving_left = False
        self.moving_right = False

        self.jumping_up = False
        self.jumping_down = False
        self.jump_height = 200
        self.jump_duration = 0

    # Method that draws the avatar on the screen
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # Method that handles updates to the avatars position and movement states
    def update(self):
        # Moving left or right
        if self.moving_left:
            self.rect.x -= 2
        if self.moving_right:
            self.rect.x += 2

        # Jumping
        if self.jumping_up:
            # Move up and increase duration
            self.rect.y -= 2
            self.jump_duration += 2
            # Start falling down when jump height is reached
            if self.jump_duration >= self.jump_height:
                self.jumping_up = False
                self.jumping_down = True
        if self.jumping_down:
            # Move down and increase duration
            self.rect.y += 2
            self.jump_duration += 2
            # Stop moving and reset duration when jump is finished
            if self.jump_duration >= self.jump_height*2:
                self.jumping_down = False
                self.jump_duration = 0
