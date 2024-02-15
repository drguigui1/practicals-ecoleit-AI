#
# Management of the game
#

import pygame
import random
from typing import List

from bird import Bird, generate_new_birds


class GameManager:
    def __init__(self, board_width: int, board_height: int, play: bool = True):
        self.play = play
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.board_width = board_width
        self.board_height = board_height
        self.background_x = 0
        self.y_speed = 0 # Gravitiy of the bird
        self.score = 0
        self.ground = board_height - 100
        self.xloc = 700
        self.ysize = random.randint(0, 350)
        self.space = random.randint(180, 250)
        self.obspeed = 2.5

    def setup_board(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode((self.board_width, self.board_height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images/background_.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.board_width, self.board_height))
        self.bird_img = pygame.image.load("images/bird.png")
        self.pipe_down_img = pygame.image.load("images/pipe.png").convert_alpha()
        self.pipe_up_img = pygame.transform.rotate(self.pipe_down_img, 180)
        self.font = pygame.font.Font("font/ARCADE_N.TTF", 50)
        self.screen.fill(self.white)

    def initialize_ai_birds(self, nb_birds: int) -> List[Bird]:
        birds = []
        for i in range(nb_birds):
            birds.append(Bird(self.board_width // 2 - 100, 250))

        for i in range(nb_birds):
            birds[i].y -= (self.board_height / nb_birds) * i - 400

        return birds

    def game_loop_manual(self):
        '''
        Flappy bird game loop
        -> manual playing
        '''
        self.x = self.board_width // 2 - 100
        self.y = 250

        running = True
        while running:
            self._draw_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.play and event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        self.y_speed = -6.5

            # Items drawings
            self._draw_obstacle(self.xloc, self.ysize, self.space)
            self._draw_bird(self.x, self.y, self.y_speed)
            self._draw_score(self.score)

            # Apply item movement
            self._apply_single_bird_movement()
            self._apply_obstacle_movements()

            # We want to generate a new obstacle
            self._build_new_obstacle()

            # Check for collisions
            running = self._check_collisions()

            if self.x > self.xloc and self.x < self.xloc + 3:
                # Score info
                self.score += 1

            self.clock.tick(60)
            self.background_x += 0.25
            self.background_x %= self.board_width

            # Gravity
            self.y_speed += 0.2

            # Update the display
            pygame.display.update()

        # Quit Pygame
        pygame.quit()

    def game_loop_with_ai(self, nb_it: int, birds: List[Bird]):
        '''
        Flappy bird game loop played by your AI birds
        '''
        all_bird_dead = False

        for _ in range(nb_it):
            while not all_bird_dead:
                self._draw_background()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                # Draw items
                self._draw_obstacle(self.xloc, self.ysize, self.space)
                self._draw_ai_birds(birds)

                # Check if all the birds are dead
                all_bird_dead = self._check_all_birds_dead(birds)

                # Apply bid movements
                self._move_all_birds(birds=birds)

                # Move the obstacle item on the screen
                self._apply_obstacle_movements()

                # We want to generate a new obstacle
                self._build_new_obstacle()

                # Check birds hit box
                self._check_birds_hit_box(birds=birds)

                self.clock.tick(60)
                self.background_x += 0.25
                self.background_x %= self.board_width
                # Update the display
                pygame.display.update()

            all_bird_dead = False
            birds.sort(key = lambda bird : bird.score, reverse=True)
            print(f"Bird best score: {birds[0].score}")
            print(f"Bird worst score: {birds[-1].score}")
            print(f"Bird avg score: {sum(bird.score for bird in birds) / len(birds)}")
            print("-------")
            birds = generate_new_birds(birds)
            birds = self._reset_ai_birds_pos(birds)

        pygame.quit()

    def _draw_ai_birds(self, birds: List[Bird]):
        '''
        Draw all the AI birds on the screen
        '''
        for b in birds:
            self.screen.blit(b.skins[int(((90 + b.y_speed * 3) / 180) * b.resolution)], (b.x, b.y))

    def _reset_ai_birds_pos(self, birds: List[Bird]) -> List[Bird]:
        for i in range(len(birds)):
            birds[i].y = (self.board_height / len(birds)) * i - 150
            birds[i].x = self.board_width // 2 - 100
            birds[i].alive = True
            birds[i].y_speed = 0
            birds[i].score = 0
            birds[i].nb_jumps = 0

        self.xloc = 700
        self.ysize = random.randint(0, 300)
        self.space = random.randint(180, 250)

        return birds

    def _check_all_birds_dead(self, birds: List[Bird]) -> bool:
        '''
        Check if all the birds are dead
        '''
        for b in birds:
            if b.alive:
                return False
        return True

    def _move_all_birds(self, birds: List[Bird]):
        '''
        Move of the birds (it will use in the backend the prediction from the brain of the bird)
        '''
        for b in birds:
            b.move(self.xloc, self.ysize + self.space // 2)

    def _check_birds_hit_box(self, birds: List[Bird]):
        for b in birds:
            b.check_alive(
                ground=self.ground,
                x_obs=self.xloc,
                ysize=self.ysize,
                space=self.space,
            )

    def _apply_single_bird_movement(self):
        '''
        Apply the movement of a single bird
        '''
        self.y += self.y_speed

    def _apply_obstacle_movements(self):
        '''
        Move the obstacle on the screen
        '''
        self.xloc -= self.obspeed

    def _build_new_obstacle(self):
        '''
        Build the new obstacle: size and space
        '''
        if self.xloc < -90: # New obstacle
            self.xloc = 700
            self.space = random.randint(180, 250)
            
            max_ysize = self.board_height - self.space - self.pipe_up_img.get_height() - self.pipe_down_img.get_height()
            
            if max_ysize > 0:
                self.ysize = random.randint(0, max_ysize)
            else:
                self.ysize = random.randint(0, self.board_height - self.space)

    def _check_collisions(self) -> bool:
        '''
        Check if the current bird has hit something
        '''
        if self.y >= self.ground + 20:
            self.y_speed, self.obspeed = 0, 0
            return False

        if self.xloc + 130 >= self.x + 65 >= self.xloc:
            if self.y + 5 < self.ysize or self.y + 50 > self.ysize + self.space:
                self.y_speed, self.obspeed = 0, 0
                return False

        return True

    def _draw_bird(self, x: float, y: float, y_speed: float):
        '''
        Display the bird at position (x, y)
        '''
        self.screen.blit(pygame.transform.rotate(self.bird_img, -y_speed * 3), (x, y))

    def _draw_obstacle(self, xloc: float, ysize: float, space: float):
        '''
        Draw obstacle at xloc position with ysize
        'space' is for the space between the 2 pipes
        '''
        self.screen.blit(self.pipe_up_img, (xloc, ysize - self.pipe_up_img.get_height()))
        self.screen.blit(self.pipe_down_img, (xloc, ysize + space))

    def _draw_background(self):
        self.screen.blit(self.background, (-self.background_x, 0))
        self.screen.blit(self.background, (self.board_width - self.background_x, 0))

    def _draw_score(self, score: float):
        '''
        Draw the score on the screen
        '''
        text = self.font.render("Score : " + str(score), True, (50, 70, 150))
        self.screen.blit(text, ((self.board_width - text.get_width()) // 2, 15))
