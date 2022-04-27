from Global import pygame, display, print_txt, rect_colour, keyboard_font, lists, litter_lists


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
        colour = self.active_colour if condition else self.inactive_colour
        pygame.draw.rect(self.display, colour, (self.x, self.y, self.wight * self.size, self.height))
        pygame.draw.rect(self.display, rect_colour, (self.x, self.y, self.wight * self.size, self.height), 4)
        counter_x = counter_y = 0
        if len(self.litters) == 3:

            print_txt(self.litters[0], self.x + counter_x + 15, self.y + counter_y + 10, keyboard_font)
            print_txt(self.litters[1], self.x + counter_x + 45, self.y + counter_y + 10, keyboard_font)
            print_txt(self.litters[2], self.x + counter_x + 25, self.y + counter_y + 40, keyboard_font)

        elif len(self.litters) == 4:

            print_txt(self.litters[0], self.x + counter_x + 20, self.y + counter_y + 10, keyboard_font)
            print_txt(self.litters[1], self.x + counter_x + 50, self.y + counter_y + 10, keyboard_font)
            print_txt(self.litters[2], self.x + counter_x + 20, self.y + counter_y + 40, keyboard_font)
            print_txt(self.litters[3], self.x + counter_x + 50, self.y + counter_y + 40, keyboard_font)

        else:

            for litter in self.litters:
                print_txt(litter, self.x + counter_x + 20, self.y - counter_x + 35, keyboard_font)
                counter_x += 25


x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4 = 100, 420, 150, 500, 200, 580, 250, 660
for litter_list in litter_lists[0]:
    lists[0].append(Key(x_1, y_1, litter_list))
    x_1 += 100
for litter_list in litter_lists[1]:
    lists[1].append(Key(x_2, y_2, litter_list))
    x_2 += 100
for litter_list in litter_lists[2]:
    lists[2].append(Key(x_3, y_3, litter_list))
    x_3 += 100
for litter_list in litter_lists[3]:
    lists[3].append(Key(x_4, y_4, litter_list))
    x_4 += 100

key_dict = dict()
for litter_list_i, list_i in zip(litter_lists, lists):
    for litters, key_object in zip(litter_list_i, list_i):
        for i in litters[0]:
            key_dict[i] = key_object

left_shift = Key(80, 660, (['Shift_L'], 'L'), 2)
right_shift = Key(1250, 660, (['Shift_R'], 'R'), 2)
space = Key(300, 740, ([' ', ' '], 'L'), 10)

key_dict[' '] = space
key_dict['Shift_L'] = left_shift
key_dict['Shift_R'] = right_shift


def draw_keyboard():
    space.draw(), left_shift.draw(), right_shift.draw()
    for key_list in lists:
        for key in key_list:
            key.draw()
