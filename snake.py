import pygame
pygame.init()

# Dibujar pantalla
ancho_pantalla = 1200
alto_pantalla = 800
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
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
        self.direccion_actual = None

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
    
    def actualizar(self):
        self.x += self.velocidadx
        self.y += self.velocidady

    def dibujarse(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.ancho, self.alto))

    def fuera_de_limites(self, ancho_pantalla, alto_pantalla):
        return (
            self.x < 0 or
            self.y < 0 or
            self.x + self.ancho > ancho_pantalla or
            self.y + self.alto > alto_pantalla
        )

# Crear Serpiente
cuadrado = Serpiente(25, 25, 25, 25, 5)
cuadrado.mover_derecha()

# Bucle ppal
jugando = True
while jugando:
    pygame.time.delay(30)

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

    cuadrado.actualizar()

    # Verificar si se fue de la pantalla
    if cuadrado.fuera_de_limites(ancho_pantalla, alto_pantalla):
        jugando = False

    screen.fill((0, 0, 0))
    cuadrado.dibujarse(screen)
    pygame.display.update()

pygame.quit()