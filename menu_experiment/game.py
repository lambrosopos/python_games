import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = (True, False)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = (False, False, 
                                                                     False, False)
        self.DISPLAY_W, self.DISPLAY_H = (480, 270)
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = ((0, 0, 0), (255, 255, 255))

    def game_loop(self):
        while self.playing:
            print("Inside game loop")
            self.check_events()
            
            if self.START_KEY:
                self.playing = False

            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

