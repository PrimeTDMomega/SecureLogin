import hashlib
import socket
import threading
import pygame

# Initialize Pygame
pygame.init()

# Define the color palette for the dark mode UI
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (70, 70, 70)
WHITE = (255, 255, 255)

# Set up the window size and title
window_size = (400, 300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dark Mode Login")

# Define font styles
username_font = pygame.font.Font(None, 36)
password_font = pygame.font.Font(None, 24)

# Function to render text on the screen
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    window.blit(text_surface, text_rect)

# Function to handle connections
def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024).decode()
    password = hashlib.sha256(password.encode()).hexdigest()

    # Login logic
    if username == "Ekagra" and password == hashlib.sha256("EkagraPass".encode()).hexdigest():
        c.send("Login Successful!".encode())
        # secrets
        # services
    else:
        c.send("Login Failure!".encode())

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

# Start the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    window.fill(DARK_GRAY)

    # Draw the "Username" text
    render_text("Username:", username_font, WHITE, 20, 20)

    # Draw the "Password" text
    render_text("Password:", password_font, WHITE, 20, 100)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
