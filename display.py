import pygame
import random


def quicksort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    if arr[0] > arr[mid]:
        arr[0], arr[mid] = arr[mid], arr[0]
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    if arr[mid] > arr[-1]:
        arr[mid], arr[-1] = arr[-1], arr[mid]
    pivot = arr[mid]
    less, equal, greater = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return quicksort(less) + equal + quicksort(greater)


def main():
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    clock = pygame.time.Clock()
    display_window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Quick Sort Visualizer")
    random_array = [random.randint(0, 50) for _ in range(20)]
    pygame_loop(random_array, display_window, clock, HEIGHT, WIDTH)
    pygame.quit()


def pygame_loop(
    random_array: list,
    screen: pygame.Surface,
    clock: pygame.time.Clock,
    HEIGHT: int,
    WIDTH: int,
):
    ...
    # Display the array as bars
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
        screen.fill((255, 255, 255))
        [
            pygame.draw.rect(
                screen,
                (9, 50, 175),
                (
                    i * WIDTH // len(random_array),
                    HEIGHT - j * 10,
                    WIDTH // len(random_array),
                    j * 10,
                ),
            )
            for i, j in enumerate(random_array)
        ]
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
