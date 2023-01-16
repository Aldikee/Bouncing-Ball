import random  #добавляем библиотеку random
from tkinter import * #из библиотеки tkinter добавили *
import time #добавляем библиотеку time
pow = Tk()
pow.resizable(0, 0)
pow.title('Circle_bounce')
screen = Canvas(pow, width=650, height=450, highlightthickness=0)
screen.pack()
pow.update()
class Circle: #созадем класс
    def __init__(self, screen, platform, total_score, colour):  #создаем функцию
        self.screen = screen
        self.platform = platform
        self.total_score = total_score
        self.proportions = screen.create_oval(10,10, 25, 25, fill=colour)
        self.screen.move(self.proportions, 245, 100)
        begin = [-2, -1, 1, 2]

        self.dx = begin[random.randint(0, len(begin) - 1)]
        self.dy = -2
        self.screen_height = self.screen.winfo_height()
        self.screen_width = self.screen.winfo_width()
        self.end = False
    def touch_platform(self, coordinates):
        platform_coordinates = self.screen.coords(self.platform.proportions)
        if coordinates[2] >= platform_coordinates[0] and coordinates[0] <= platform_coordinates[2]:
            if coordinates[3] >= platform_coordinates[1] and coordinates[3] <= platform_coordinates[3]:
                self.total_score.hit()
                return True
        return False
    def draw(self):
        self.screen.move(self.proportions, self.dx, self.dy)
        coordinates = self.screen.coords(self.proportions)
        if coordinates[1] <= 0:
            self.dy = 2
        if coordinates[3] >= self.screen_height:
            self.end = True
            screen.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
        if self.touch_platform(coordinates) == True:
            self.dy = -2
        if coordinates[0] <= 0:
            self.dx = 2
        if coordinates[2] >= self.screen_width:
            self.dx = -2
class Platform:
    def __init__(self, screen, colour):
        self.screen = screen
        self.proportions = screen.create_rectangle(0, 0, 100, 10, fill=colour)
        beginning = [40, 60, 90, 120, 150, 180, 200]
        self.starting_point_x =  beginning[random.randint(0, len(beginning) - 1)]
        self.screen.move(self.proportions, self.starting_point_x, 300)
        self.dx = 0
        self.screen_width = self.screen.winfo_width()
        self.screen.bind_all('<KeyPress-Right>', self.rightward)
        self.screen.bind_all('<KeyPress-Left>', self.leftward)
        self.started = False
        self.screen.bind_all('<KeyPress-Return>', self.begin_game)
    def rightward(self, event):
        self.dx = 2
    def leftward(self, event):
        self.dx = -2
    def begin_game(self, event):
        self.started = True
    def draw(self):
        self.screen.move(self.proportions, self.dx, 0)
        coordinates = self.screen.coords(self.proportions)
        if coordinates[0] <= 0:
            self.dx = 0
        elif coordinates[2] >= self.screen_width:
            self.dx = 0
class Total_score:
    def __init__(self, screen, colour):
        self.total_score = 0
        self.screen = screen
        self.proportions = screen.create_text(450, 10, text="score:" +str(self.total_score), font=('Courier', 15), fill=colour)
    def hit(self):
        self.total_score = self.total_score + 1
        self.screen.itemconfig(self.proportions, text="score:" +str(self.total_score))
total_score = Total_score(screen, 'Red')
platform = Platform(screen, 'Black')
circle = Circle(screen, platform, total_score, 'blue')
while not circle.end:
    if platform.started == True:
        circle.draw()
        platform.draw()
    pow.update_idletasks()
    pow.update()
    time.sleep(0.01)
time.sleep(3)
