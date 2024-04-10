import pygame
import sys
import math

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera 3D com Pygame")

# Defina as coordenadas 3D da esfera
radius = 200
num_points = 100
points = []
for i in range(num_points + 1):
    theta = 2 * math.pi * i / num_points
    for j in range(num_points + 1):
        phi = math.pi * j / num_points
        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)
        points.append((x, y, z))

# Defina as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Defina a função de rotação
def rotate(points, angle_x, angle_y, angle_z):
    rotated_points = []
    for point in points:
        x, y, z = point
        # Rotação em torno do eixo x
        new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
        y, z = new_y, new_z
        # Rotação em torno do eixo y
        new_x = x * math.cos(angle_y) + z * math.sin(angle_y)
        new_z = -x * math.sin(angle_y) + z * math.cos(angle_y)
        x, z = new_x, new_z
        # Rotação em torno do eixo z
        new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
        new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
        x, y = new_x, new_y
        rotated_points.append((x, y, z))
    return rotated_points


# Loop principal
clock = pygame.time.Clock()
angle_x = 0
angle_y = 0
angle_z = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Rotação da esfera

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        angle_x += 0.2
    if keys[pygame.K_s]:
        angle_x -= 0.2
    if keys[pygame.K_a]:
        angle_y += 0.2
    if keys[pygame.K_d]:
        angle_y -= 0.2

    # Rotação dos pontos
    rotated_points = rotate(points, angle_x, angle_y, angle_z)

    # Desenhe os pontos na tela
    for point in rotated_points:
        x, y, z = point
        # Projeção dos pontos 3D para 2D
        scale = 400 / (400 + z)
        screen_x = int(x * scale) + WIDTH // 2
        screen_y = int(y * scale) + HEIGHT // 2
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 2)

    pygame.display.flip()
    clock.tick(60)
