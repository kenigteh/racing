import random
import pygame

# Специальная команда, которая говорит комьютеру, что мы будем рабоать с играми на Python
pygame.init()

# Создаём окошко для игры c нужными размерами и добавляем название
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Fast racing')

# Прописываем размеры, местоположение и скорость машинки
width = 40
height = 80
x = 240
y = 420
speed = 5

# Получаем картинку машинки
car_img = pygame.image.load('img/car.png')
car_img = pygame.transform.scale(car_img, (width, height))

# Загружаем встречные машины
cars_img = [
    pygame.transform.scale(pygame.image.load('img/car1.png'), (40, 80)),
    pygame.transform.scale(pygame.image.load('img/car2.png'), (40, 70)),
    pygame.transform.scale(pygame.image.load('img/car3.png'), (45, 90)),
]

# Получаем картинку фона
fon_img = pygame.image.load('img/fon.png')
fon_img = pygame.transform.scale(fon_img, (500, 500))

# Получаем картинку окончания игры
end_img = pygame.image.load('img/end.png')
end_img = pygame.transform.scale(end_img, (290, 180))


# Окончание игры
def show_end_screen():
    # Рисуем картинку конца игры
    win.blit(end_img, (105, 120))
    pygame.display.flip()

    # Ждём, пока нажмут на крестик
    waiting = True
    while waiting:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


class Car:
    def __init__(self):
        self.x = random.uniform(120, 380)
        self.y = 5
        self.car_img = random.choice(cars_img)
        self.weight = self.car_img.get_size()[0]
        self.height = self.car_img.get_size()[1]
        self.speed = random.uniform(5, 15)

    def draw(self, win):
        win.blit(self.car_img, (self.x, self.y))


all_cars = []


# Функция изменения изображений на экране
def draw_window():
    # Заливаем фон черным цветом
    win.blit(fon_img, (0, 0))

    # Рисуем машинку в нужном месте с нашими размерами
    win.blit(car_img, (x, y))

    for car in all_cars:
        car.y += car.speed
        car.draw(win)

    # Перерисовываем картинку в окне
    pygame.display.update()


# Создаём переменную для времени
clock = pygame.time.Clock()

# Бесконечный цикл для проверки событий и изменения графики
run = True
while run:
    clock.tick(30)

    # Цикл, в котором мы перебираем все события в игре
    for event in pygame.event.get():
        # Проверяем, какое событие случилось
        if event.type == pygame.QUIT:
            run = False

    if random.uniform(1, 100) > 98:
        all_cars.append(Car())

    # Перебираем машины для проверки на столкновение
    for car in all_cars:
        x1 = x
        x2 = x + width
        x3 = car.x
        x4 = car.x + car.weight

        # Если столкнулись
        if car.y + car.height > y > car.y and (x1 < x3 < x2 or x1 < x4 < x2):
            show_end_screen()

        # Если машинка уехала, удаляем
        if car.y > 500:
            all_cars.remove(car)

    # Получаем список кнопок
    keys = pygame.key.get_pressed()

    # Проверяем, какая кнопка нажата, и меняем местоположение игрока, если не вышли за экран
    if keys[pygame.K_LEFT] and x > 100:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 100:
        x += speed
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        y += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed

    draw_window()
