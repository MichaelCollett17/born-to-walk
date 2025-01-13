import pygame
import math

# Initialize PyGame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Differentially Driven Vehicle Simulation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Vehicle parameters
vehicle_width = 40
vehicle_height = 60
x, y = width // 2, height // 2
angle = 0
left_speed = 0
right_speed = 0

# Simulation parameters
clock = pygame.time.Clock()
running = True


def draw_vehicle(screen, x, y, angle):
    # Calculate the corners of the vehicle
    corners = [
        (-vehicle_width // 2, -vehicle_height // 2),
        (vehicle_width // 2, -vehicle_height // 2),
        (vehicle_width // 2, vehicle_height // 2),
        (-vehicle_width // 2, vehicle_height // 2),
    ]
    rotated_corners = []
    for corner in corners:
        rotated_x = corner[0] * math.cos(angle) - corner[1] * math.sin(angle)
        rotated_y = corner[0] * math.sin(angle) + corner[1] * math.cos(angle)
        rotated_corners.append((rotated_x + x, rotated_y + y))

    pygame.draw.polygon(screen, red, rotated_corners)

    # Calculate the front indicator position
    front_x = x + (vehicle_height // 2) * math.cos(angle)
    front_y = y + (vehicle_height // 2) * math.sin(angle)

    # Draw the front indicator
    pygame.draw.circle(screen, white, (int(front_x), int(front_y)), 5)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        left_speed = 5
    elif keys[pygame.K_z]:
        left_speed = -5
    else:
        left_speed = 0

    if keys[pygame.K_s]:
        right_speed = 5
    elif keys[pygame.K_x]:
        right_speed = -5
    else:
        right_speed = 0

    # Calculate the average speed and angular velocity
    speed = (left_speed + right_speed) / 2
    angular_velocity = (right_speed - left_speed) / vehicle_width

    # Update vehicle position and angle
    angle += angular_velocity
    x += speed * math.cos(angle)
    y += speed * math.sin(angle)

    # Clear screen
    screen.fill(black)

    # Draw vehicle
    draw_vehicle(screen, x, y, angle)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
