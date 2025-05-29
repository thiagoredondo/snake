import pygame
pygame.init()

# Dibujar pantalla
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake")

class Serpiente:
    def __init__(self, x, y, ancho, alto, velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.velocidadx = 0
        self.velocidady = 0
        self.direccion_actual = None  # Direccion inicial

    def mover_derecha(self):
        if self.direccion_actual != 'izquierda':
            self.velocidadx = self.velocidad
            self.velocidady = 0
            self.direccion_actual = 'derecha'

    def mover_izquierda(self):
        if self.direccion_actual != 'derecha':
            self.velocidadx = -self.velocidad
            self.velocidady = 0
            self.direccion_actual = 'izquierda'

    def mover_arriba(self):
        if self.direccion_actual != 'abajo':
            self.velocidadx = 0
            self.velocidady = -self.velocidad
            self.direccion_actual = 'arriba'

    def mover_abajo(self):
        if self.direccion_actual != 'arriba':
            self.velocidadx = 0
            self.velocidady = self.velocidad
            self.direccion_actual = 'abajo'
    
    def dibujarse(self, screen):
        self.x += self.velocidadx
        self.y += self.velocidady
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.ancho, self.alto))

# Crear Serpiente
cuadrado = Serpiente(25, 25, 25, 25, 5)
cuadrado.mover_derecha()  # Dirección inicial

# Bucle ppal
jugando = True
while jugando:
    pygame.time.delay(30)  # Velocidad de la serpiente

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cuadrado.mover_izquierda()
    elif keys[pygame.K_RIGHT]:
        cuadrado.mover_derecha()
    elif keys[pygame.K_UP]:
        cuadrado.mover_arriba()
    elif keys[pygame.K_DOWN]:
        cuadrado.mover_abajo()

    screen.fill((0, 0, 0))
    cuadrado.dibujarse(screen)
    pygame.display.update()

pygame.quit()