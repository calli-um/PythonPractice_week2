import pygame
import sys
import time
from functions import Main  # class Main containing all helper methods

pygame.init()

# Screen Setup
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Test")

# Fonts and Colors
FONT = pygame.font.SysFont("Timesnewroman", 28)
BIG_FONT = pygame.font.SysFont("Timesnewroman", 42, bold=True)
WHITE = (230, 230, 230)
BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
GRAY = (180, 180, 180)
BLUE = (0, 0, 100)
DARK_GRAY = (60, 60, 60)
HOVER_BLUE = (0, 0, 150)

clock = pygame.time.Clock()

# State Variables
difficulty = None
sentence = ""
state = Main.reset()
input_active = False
test_started = False

# Button Function
def draw_button(text, x, y, w, h, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    current_color = hover_color if x < mouse[0] < x + w and y < mouse[1] < y + h else color

    pygame.draw.rect(screen, current_color, (x, y, w, h), border_radius=10)
    button_text = FONT.render(text, True, WHITE)
    screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        if click[0] == 1 and action:
            pygame.time.wait(200)
            action()

# Start Typing Test
def start_test(selected_level):
    global difficulty, sentence, state, input_active, test_started
    difficulty = selected_level
    sentence = Main.LoadRandomSentence(difficulty)
    state = Main.reset()
    input_active = True
    test_started = True

# Main Menu
def show_main_menu():
    screen.fill(WHITE)
    title = BIG_FONT.render("Typing Speed Test", True, BLUE)
    screen.blit(title, ((WIDTH - title.get_width()) // 2, 80))

    # Buttons
    button_width = 140
    button_height = 50
    gap = 40
    total_width = 3 * button_width + 2 * gap
    start_x = (WIDTH - total_width) // 2
    y_pos = 200

    draw_button("Easy", start_x, y_pos, button_width, button_height, BLUE, HOVER_BLUE, lambda: start_test("easy"))
    draw_button("Medium", start_x + button_width + gap, y_pos, button_width, button_height, BLUE, HOVER_BLUE, lambda: start_test("medium"))
    draw_button("Hard", start_x + 2 * (button_width + gap), y_pos, button_width, button_height, BLUE, HOVER_BLUE, lambda: start_test("hard"))

# Typing Test Screen
def draw_typing_test():
    screen.fill(WHITE)
    global input_active, sentence, state

    margin_x, margin_y = 50, 80
    sentence_words = sentence.split()
    input_words = state["input_text"].split()
    x, y = margin_x, margin_y

    for i, word in enumerate(sentence_words):
        if i < len(input_words):
            typed_word = input_words[i]
            color = GREEN if typed_word == word else RED
        else:
            color = BLACK

        word_surface = FONT.render(word, True, color)
        word_width = word_surface.get_width()

        if x + word_width >= WIDTH - margin_x:
            x = margin_x
            y += FONT.get_height() + 5

        screen.blit(word_surface, (x, y))
        x += word_width + FONT.size(' ')[0]

    # Typing Area
    screen.blit(BIG_FONT.render("Start Typing Below:", True, BLUE), (margin_x, y + 50))
    typed_text_surface = FONT.render(state["input_text"], True, BLACK)
    input_y = y + 100
    screen.blit(typed_text_surface, (margin_x, input_y))

    # Placeholder
    if state["input_text"] == "" and input_active:
        placeholder = FONT.render("Start typing here...", True, DARK_GRAY)
        screen.blit(placeholder, (margin_x, input_y))

    # Blinking Cursor
    if input_active and pygame.time.get_ticks() % 1000 < 500:
        cursor_x = margin_x + FONT.size(state["input_text"])[0]
        pygame.draw.line(screen, BLACK, (cursor_x, input_y), (cursor_x, input_y + FONT.get_height()), 2)

    # Results
    if not input_active and state["end_time"] != 0:
        total_typed = len(state["input_text"])
        correct_chars = sum(1 for i, c in enumerate(state["input_text"]) if i < len(sentence) and c == sentence[i])
        time_taken = Main.timeTrack(state["start_time"], state["end_time"])
        accuracy = Main.accuracyCheck(total_typed, correct_chars)
        wpm = Main.WPM_calculate(total_typed, time_taken)

        results = [
            f"Time Taken: {round(time_taken, 2)} sec",
            f"Accuracy: {round(accuracy, 2)}%",
            f"WPM: {round(wpm, 2)}"
        ]

        for i, line in enumerate(results):
            result_surface = FONT.render(line, True, BLACK)
            screen.blit(result_surface, (margin_x, input_y + 60 + i * 30))

        draw_button("Restart", WIDTH - 160, HEIGHT - 70, 120, 45, BLUE, HOVER_BLUE, lambda: start_test(difficulty))

# Game Loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif test_started and input_active and event.type == pygame.KEYDOWN:
            if state["start_time"] == 0:
                state["start_time"] = time.time()

            if event.key == pygame.K_BACKSPACE:
                state["input_text"] = state["input_text"][:-1]
            elif event.key == pygame.K_RETURN:
                state["end_time"] = time.time()
                input_active = False
            elif event.key == pygame.K_ESCAPE:
                test_started = False
                state = Main.reset()
            else:
                state["input_text"] += event.unicode

    if not test_started:
        show_main_menu()
    else:
        draw_typing_test()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
