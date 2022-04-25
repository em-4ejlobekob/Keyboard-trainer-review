from Global import pygame, display, print_txt


class Key:
    def __init__(self, x, y, litters_, size=1, display_=display):
        self.x = x
        self.y = y
        self.size = size
        self.display = display_
        self.mists = 0
        self.litters = litters_[0]
        self.shift = litters_[1]
        self.wight = 75
        self.height = 75

        self.act_1 = 160
        self.act_2 = 200
        self.act_3 = 60

        self.inactive_colour = (self.act_1, self.act_2, self.act_3)
        self.active_colour = (255, 255, 0)

    def draw(self, condition=False):
        self.act_1 = 160 + self.mists * 1
        self.act_2 = 200 - self.mists * 3
        self.inactive_colour = (self.act_1, self.act_2, self.act_3)
        if condition:
            pygame.draw.rect(self.display, self.active_colour, (self.x, self.y, self.wight * self.size, self.height))
        else:
            pygame.draw.rect(self.display, self.inactive_colour, (self.x, self.y, self.wight * self.size, self.height))
        pygame.draw.rect(self.display, (64, 128, 255), (self.x, self.y, self.wight * self.size, self.height), 4)
        counter_x = 0
        counter_y = 0
        if len(self.litters) == 3:

            print_txt(self.litters[0], self.x + counter_x + 15, self.y + counter_y + 10, 'src/asserts/Fonts/font_1.otf')
            print_txt(self.litters[1], self.x + counter_x + 45, self.y + counter_y + 10, 'src/asserts/Fonts/font_1.otf')
            print_txt(self.litters[2], self.x + counter_x + 25, self.y + counter_y + 40, 'src/asserts/Fonts/font_1.otf')

        elif len(self.litters) == 4:

            print_txt(self.litters[0], self.x + counter_x + 20, self.y + counter_y + 10, 'src/asserts/Fonts/font_1.otf')
            print_txt(self.litters[1], self.x + counter_x + 50, self.y + counter_y + 10, 'src/asserts/Fonts/font_1.otf')
            print_txt(self.litters[2], self.x + counter_x + 20, self.y + counter_y + 40, 'src/asserts/Fonts/font_1.otf')
            print_txt(self.litters[3], self.x + counter_x + 50, self.y + counter_y + 40, 'src/asserts/Fonts/font_1.otf')

        else:

            for i_ in self.litters:
                print_txt(i_, self.x + counter_x + 20, self.y - counter_x + 35, 'src/asserts/Fonts/font_1.otf')
                counter_x += 25


litter_list_1 = [(['`', '~', 'Ё'], 'R'), (['1', '!'], 'R'), (['@', '"', '2'], 'R'), (['#', '№', '3'], 'R'), (['$', ';', '4'], 'R'),
                 (['5', '%'], 'R'), ([':', '^', '6'], 'R'), (['&', '?', '7'], 'L'), (['8', '*'], 'L'), (['9', '('], 'L'),
                 (['0', ')'], 'L'), (['-', '_'], 'L'), (['=', '+'], 'L')]
litter_list_2 = [(['Й', 'Q'], 'R'), (['Ц', 'W'], 'R'), (['У', 'E'], 'R'), (['К', 'R'], 'R'), (['Е', 'T'], 'R'),
                 (['Н', 'Y'], 'L'), (['Г', 'U'], 'L'), (['Ш', 'I'], 'L'), (['Щ', 'O'], 'L'), (['З', 'P'], 'L'),
                 (['[', '{', 'Х'], 'L'), ([']', '}', 'Ъ'], 'L')]
litter_list_3 = [(['Ф', 'A'], 'R'), (['Ы', 'S'], 'R'), (['В', 'D'], 'R'), (['А', 'F'], 'R'), (['П', 'G'], 'R'),
                 (['Р', 'H'], 'L'), (['О', 'J'], 'L'), (['Л', 'K'], 'L'), (['Д', 'L'], 'L'), ([';', ':', 'Ж'], 'L'),
                 (["'", '"', 'Э'], 'L'), (['|', '/', '\\'], 'L')]
litter_list_4 = [(['Я', 'Z'], 'R'), (['Ч', 'X'], 'R'), (['С', 'C'], 'R'), (['М', 'V'], 'R'), (['И', 'B'], 'R'),
                 (['Т', 'N'], 'L'), (['Ь', 'M'], 'L'), ([',', '<', 'Б'], 'L'), (['.', '>', 'Ю'], 'L'), (['?', ',', '/', '.'], 'L')]
litter_list_5 = [([' ', ' '], 'L')]

list_1, list_2, list_3, list_4, list_5 = list(), list(), list(), list(), list()
x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5 = 100, 420, 150, 500, 200, 580, 250, 660, 300, 740
for i in litter_list_1:
    list_1.append(Key(x_1, y_1, i))
    x_1 += 100

for i in litter_list_2:
    list_2.append(Key(x_2, y_2, i))
    x_2 += 100

for i in litter_list_3:
    list_3.append(Key(x_3, y_3, i))
    x_3 += 100

left_shift = Key(x_4 - 170, y_4, (['Shift_L'], 'L'), 2)
list_4.append(left_shift)
for i in litter_list_4:
    list_4.append(Key(x_4, y_4, i))
    x_4 += 100
right_shift = Key(x_4, y_4, (['Shift_R'], 'R'), 2)
list_4.append(right_shift)

for i in litter_list_5:
    list_5.append(Key(x_5, y_5, i, 10))
    x_5 += 100

key_dict = dict()
for litters, key_object in zip(litter_list_1, list_1):
    for i in litters[0]:
        key_dict[i] = key_object
for litters, key_object in zip(litter_list_2, list_2):
    for i in litters[0]:
        key_dict[i] = key_object
for litters, key_object in zip(litter_list_3, list_3):
    for i in litters[0]:
        key_dict[i] = key_object
for litters, key_object in zip(litter_list_4, list_4):
    for i in litters[0]:
        key_dict[i] = key_object
for litters, key_object in zip(litter_list_5, list_5):
    for i in litters[0]:
        key_dict[i] = key_object


def draw_keyboard():
    global list_1, list_2, list_3, list_4, list_5
    for i_ in [list_1, list_2, list_3, list_4, list_5]:
        for j in i_:
            j.draw()
