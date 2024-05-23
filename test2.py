import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and fullscreen setup
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
BAR_WIDTH = 5
ARRAY_SIZE = SCREEN_WIDTH // BAR_WIDTH

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("QuickSort Visualization")


def generate_array():
    return [random.randint(1, SCREEN_HEIGHT) for _ in range(ARRAY_SIZE)]


def draw_array(array, color_positions={}):
    screen.fill(WHITE)
    for i, val in enumerate(array):
        color = color_positions.get(i, BLUE)
        pygame.draw.rect(
            screen, color, (i * BAR_WIDTH, SCREEN_HEIGHT - val, BAR_WIDTH, val)
        )
    pygame.display.flip()


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    draw_array(arr, {low: RED, (low + high) // 2: RED, high: RED})
    pygame.time.delay(10)
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]
        draw_array(arr, {i: GREEN, j: GREEN})
        pygame.time.delay(10)


def sort_and_visualize(array):
    quicksort(array, 0, len(array) - 1)


def main():
    sorting = False
    clock = pygame.time.Clock()
    time_since_last_generate = 0
    generate_interval = 5  # 5 seconds

    array = generate_array()
    sort_and_visualize(array)  # Start sorting the initial array

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    return

        draw_array(array)
        clock.tick(60)

        time_since_last_generate += (
            clock.get_rawtime() / 1000
        )  # Convert milliseconds to seconds

        if time_since_last_generate >= generate_interval:
            array = generate_array()
            sort_and_visualize(array)  # Start sorting the newly generated array
            time_since_last_generate = 0


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
