from Global import pygame, display, keyboard_font, lists, litter_lists, main_font

import variables as var


class Key:
    """Класс Клавиша

    Экземпляром класса является клавиша. Она отрисовывается на экране методом draw. На клавишу выводятся
    символы, которым она соответствует на клавиатуре. Если на клавишу надо нажать, то она подсвечивается
    цветом active_color.

    """

    def __init__(self, x, y, litters_, size=1, dspl=display):
        self.x = x
        self.y = y
        self.size = size
        self.display = dspl
        self.mists = 0
        self.litters = litters_[0]
        self.shift = litters_[1]
        self.wight = var.key_wight
        self.height = var.key_height

        self.inactive_1 = var.inactive_key_1
        self.inactive_2 = var.inactive_key_2
        self.inactive_3 = var.inactive_key_3

        self.inactive_colour = (self.inactive_1, self.inactive_2, self.inactive_3)
        self.active_color = var.active_key_color

    def key_txt(self, message, x, y, font_type=main_font, font_color=(0, 0, 0), font_size=var.key_font_size):
        """Выводит символы или название кнопки на саму кнопку"""
        font_type = pygame.font.Font(font_type, font_size)
        txt = font_type.render(message, True, font_color)
        self.display.blit(txt, (x, y))

    def draw(self, condition=False):
        """Рисует клавишу на поле.

        Если condition=True, то кнопка горит цветом active_color_key - значит на неё надо сейчас нажать. В противном
        случае кнопка горит цветом inactive_color_key. Клавиша может содержать разное количество символов, поэтому
        в зависимости от их количества, они печатаются в разных местах квадратной клавиши (для эстетичности конечно).

        """
        self.inactive_colour = (self.inactive_1 + self.mists * 1, self.inactive_2 - self.mists * var.penalty_coef, self.inactive_3)
        colour = self.active_color if condition else self.inactive_colour
        pygame.draw.rect(self.display, colour, (self.x, self.y, self.wight * self.size, self.height))
        pygame.draw.rect(self.display, var.key_rect_colour, (self.x, self.y, self.wight * self.size, self.height), 4)
        if len(self.litters) == 3:

            self.key_txt(self.litters[0], self.x + var.keylit_3_x_up_left, self.y + var.keylit_3_y_up, keyboard_font)
            self.key_txt(self.litters[1], self.x + var.keylit_3_x_up_right, self.y + var.keylit_3_y_up, keyboard_font)
            self.key_txt(self.litters[2], self.x + var.keylit_3_x_down, self.y + var.keylit_3_y_down, keyboard_font)

        elif len(self.litters) == 4:

            self.key_txt(self.litters[0], self.x + var.keylit_4_x_left, self.y + var.keylit_4_y_up, keyboard_font)
            self.key_txt(self.litters[1], self.x + var.keylit_4_x_right, self.y + var.keylit_4_y_up, keyboard_font)
            self.key_txt(self.litters[2], self.x + var.keylit_4_x_left, self.y + var.keylit_4_y_down, keyboard_font)
            self.key_txt(self.litters[3], self.x + var.keylit_4_x_right, self.y + var.keylit_4_y_down, keyboard_font)

        else:
            counter = 0
            for litter in self.litters:
                self.key_txt(litter, self.x + counter + var.keylit_2_x, self.y - counter + var.keylit_2_y, keyboard_font)
                counter += var.litter_2_dist


key_dict = dict()
for line in range(var.keyboard_lines):
    for litter_list in litter_lists[line]:
        lists[line].append(Key(var.dict_keys_line_x[line], var.dict_keys_line_y[line], litter_list))
        var.dict_keys_line_x[line] += var.next_dist_key

for litter_list_i, list_i in zip(litter_lists, lists):
    for litters, key_object in zip(litter_list_i, list_i):
        for i in litters[0]:
            key_dict[i] = key_object

left_shift = Key(var.left_shift_x, var.left_shift_y, (['Shift_L'], 'L'), var.left_shift_len)
right_shift = Key(var.right_shift_x, var.right_shift_y, (['Shift_R'], 'R'), var.right_shift_len)
space = Key(var.space_x, var.space_y, ([' ', ' '], 'L'), var.space_len)

key_dict[' '] = space
key_dict['Shift_L'] = left_shift
key_dict['Shift_R'] = right_shift


def draw_keyboard():
    """Рисует клавиутру"""
    space.draw(), left_shift.draw(), right_shift.draw()
    for key_list in lists:
        for key in key_list:
            key.draw()


def draw_active_keys(txt_string, len_input_txt):
    """Подсвечивает клавиши другим цветом, если на них надо нажать"""
    key_dict[txt_string[len_input_txt].upper()].draw(condition=True)
    if txt_string[len_input_txt] != ' ' and txt_string[len_input_txt].isupper():
        if key_dict[txt_string[len_input_txt].upper()].shift == 'L':
            left_shift.draw(condition=True)
        else:
            right_shift.draw(condition=True)
