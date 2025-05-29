import pygame
import random

pygame.init()

# Configuracion
tamano_celda = 25
ancho_pantalla = 49 * tamano_celda
alto_pantalla = 33 * tamano_celda
velocidad_movimiento = tamano_celda * 6  # milisegundos entre cambios de direccion
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

class Serpiente:
    def __init__(self, x, y, tamano):
        self.x = x
        self.y = y
        self.tamano = tamano
        self.direccion_actual = 'derecha'

    def mover(self):
        if self.direccion_actual == 'derecha':
            self.x += self.tamano
        elif self.direccion_actual == 'izquierda':
            self.x -= self.tamano
        elif self.direccion_actual == 'arriba':
            self.y -= self.tamano
        elif self.direccion_actual == 'abajo':
            self.y += self.tamano

    def cambiar_direccion(self, nueva_direccion):
        opuestas = {
            'derecha': 'izquierda',
            'izquierda': 'derecha',
            'arriba': 'abajo',
            'abajo': 'arriba'
        }
        if nueva_direccion != opuestas.get(self.direccion_actual):
            self.direccion_actual = nueva_direccion

    def dibujarse(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.tamano, self.tamano))

    def fuera_de_limites(self, ancho_pantalla, alto_pantalla):
        return (
            self.x < 0 or
            self.y < 0 or
            self.x + self.tamano > ancho_pantalla or
            self.y + self.tamano > alto_pantalla
        )

class Comida:
    def __init__(self, tamano, ancho_pantalla, alto_pantalla):
        self.tamano = tamano
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.x = 0
        self.y = 0
        self.generar_nueva_posicion()

    def generar_nueva_posicion(self):
        columnas = self.ancho_pantalla // self.tamano
        filas = self.alto_pantalla // self.tamano
        self.x = random.randint(0, columnas - 1) * self.tamano
        self.y = random.randint(0, filas - 1) * self.tamano

    def dibujarse(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.tamano, self.tamano))

# Crear objetos
cuadrado = Serpiente(tamano_celda, tamano_celda, tamano_celda)
comida = Comida(tamano_celda, ancho_pantalla, alto_pantalla)

# Control de tiempo
ultimo_movimiento = pygame.time.get_ticks()

# Bucle ppal
jugando = True
while jugando:
    clock.tick(60)  # 60 FPS fijos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cuadrado.cambiar_direccion('izquierda')
    elif keys[pygame.K_RIGHT]:
        cuadrado.cambiar_direccion('derecha')
    elif keys[pygame.K_UP]:
        cuadrado.cambiar_direccion('arriba')
    elif keys[pygame.K_DOWN]:
        cuadrado.cambiar_direccion('abajo')

    # Movimiento controlado por tiempo
    ahora = pygame.time.get_ticks()
    if ahora - ultimo_movimiento >= velocidad_movimiento:
        cuadrado.mover()
        ultimo_movimiento = ahora

        if cuadrado.fuera_de_limites(ancho_pantalla, alto_pantalla):
            jugando = False

    screen.fill((0, 0, 0))
    cuadrado.dibujarse(screen)
    comida.dibujarse(screen)
    pygame.display.update()

pygame.quit()