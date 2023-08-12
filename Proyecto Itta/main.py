import pygame
import random
import sys

pygame.init()

# Configuración de la pantalla
width, height = 660, 380
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Math go!")

#musica de fondo
pygame.mixer.music.load("y2mate.com - pet in tv OST  M2.mp3")
pygame.mixer.music.play(-1)

# Colores
white=(255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

#imagen del fondo
imagen=pygame.image.load("c99e5a11d3c6e40fd35914767adb4da8.png").convert()

# Variables del juego
lives = 3
score = 0

# Función para generar una pregunta aleatoria
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2
    
    question_text = f"{num1} {operator} {num2} = ?"
    return question_text, answer

# Función para mostrar texto en la pantalla
def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Pantalla de inicio
def show_start_screen():
    screen.blit(imagen, [0, 0])
    draw_text("Bienvenido ah Math go! :D", 170, 120, black)
    draw_text("Objetivo: Llegar a 10 de puntuacion para ganar", 50, 170, black)
    draw_text("Presiona cualquier tecla para comenzar", 100, 210, black)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
        # Actualizar la ventana
    pygame.display.flip()

# Pantalla de juego
def game_loop():
    global lives, score
    running = True
    while running:
        question, answer = generate_question()
        user_input = ""
        correct_answer = False
        while not correct_answer:
            screen.blit(imagen, [0, 0])
            draw_text(question, 150, 150, black)
            draw_text(f"Puntuación: {score} Vidas: {lives}", 150, 200, black)
            draw_text(user_input, 150, 250, black)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            if int(user_input) == answer:
                                score += 1
                                if score >= 10:
                                    game_win()
                                else:
                                    question, answer = generate_question()
                                    user_input = ""
                            else:
                                lives -= 1
                                if lives == 0:
                                    game_over()
                                else:
                                    question, answer = generate_question()
                                    user_input = ""
                            break
                        except ValueError:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
            # Actualizar la ventana
    pygame.display.flip()

# Pantalla de fin de juego
def game_over():
    screen.blit(imagen, [0, 0])
    draw_text("Game Over D:", 250, 130, black)
    draw_text(f"Puntuación final: {score}", 210, 190, black)
    draw_text("Presiona cualquier tecla para salir", 140, 220, black)
    pygame.mixer.music.load("y2mate.com - Trompeta Meme  Sound Effect HD.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        # Actualizar la ventana
    pygame.display.flip()

# Pantalla de victoria
def game_win():
    screen.blit(imagen, [0, 0])
    draw_text("¡Ganaste! :D", 250, 130, black)
    draw_text(f"Puntuación final: {score}", 210, 190, black)
    draw_text("Presiona cualquier tecla para salir", 140, 220, black)
    pygame.mixer.music.load("y2mate.com - SONIDO RESPUESTA CORRECTA.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        # Actualizar la ventana
    pygame.display.flip()

# Función principal
def main():
    show_start_screen()
    game_loop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    