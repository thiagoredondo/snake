import pygame
import random
import sys

# Configuración general
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Colores
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Snake:
    def __init__(self):
        self.body = [pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)]
        self.direction = "RIGHT"
        self.grow_pending = 0

    def move(self):
        head = self.body[0].copy()

        if self.direction == "UP":
            head.y -= CELL_SIZE
        elif self.direction == "DOWN":
            head.y += CELL_SIZE
        elif self.direction == "LEFT":
            head.x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head.x += CELL_SIZE

        self.body.insert(0, head)

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending += 1

    def check_collision(self):
        head = self.body[0]
        return any(segment.colliderect(head) for segment in self.body[1:])

    def out_of_bounds(self):
        head = self.body[0]
        return not (0 <= head.x < SCREEN_WIDTH and 0 <= head.y < SCREEN_HEIGHT)

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, segment)

class Food:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
        self.spawn([])

    def spawn(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            new_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            if all(not segment.colliderect(new_rect) for segment in snake_body):
                self.rect = new_rect
                break

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

    def draw_score(self):
        text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(text, (10, 10))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake.direction != "DOWN":
            self.snake.direction = "UP"
        elif keys[pygame.K_DOWN] and self.snake.direction != "UP":
            self.snake.direction = "DOWN"
        elif keys[pygame.K_LEFT] and self.snake.direction != "RIGHT":
            self.snake.direction = "LEFT"
        elif keys[pygame.K_RIGHT] and self.snake.direction != "LEFT":
            self.snake.direction = "RIGHT"

    def update(self):
        self.snake.move()

        if self.snake.body[0].colliderect(self.food.rect):
            self.snake.grow()
            self.food.spawn(self.snake.body)
            self.score += 1

        if self.snake.check_collision() or self.snake.out_of_bounds():
            print("¡Game Over!")
            pygame.quit()
            sys.exit()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.check_events()
            self.update()
            self.draw()

# Punto de entrada
if __name__ == "__main__":
    Game().run()
