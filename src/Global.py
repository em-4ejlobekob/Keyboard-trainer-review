import pygame


pygame.init()
process = True

fonts = ['asserts/Fonts/font_1', 'asserts/Fonts/font_2', 'asserts/Fonts/font_3', 'asserts/Fonts/font_4',
         'asserts/Fonts/font_5']
main_font = fonts[0] + '.otf'
max_str_len = 80
display = pygame.display.set_mode((1600, 900))

rect_colour = (64, 128, 255)
keyboard_font = main_font
litter_list_1 = [(['`', '~', 'Ё'], 'R'), (['1', '!'], 'R'), (['@', '"', '2'], 'R'), (['#', '№', '3'], 'R'),
                 (['$', ';', '4'], 'R'), (['5', '%'], 'R'), ([':', '^', '6'], 'R'), (['&', '?', '7'], 'L'),
                 (['8', '*'], 'L'), (['9', '('], 'L'), (['0', ')'], 'L'), (['-', '_'], 'L'), (['=', '+'], 'L')]
litter_list_2 = [(['Й', 'Q'], 'R'), (['Ц', 'W'], 'R'), (['У', 'E'], 'R'), (['К', 'R'], 'R'), (['Е', 'T'], 'R'),
                 (['Н', 'Y'], 'L'), (['Г', 'U'], 'L'), (['Ш', 'I'], 'L'), (['Щ', 'O'], 'L'), (['З', 'P'], 'L'),
                 (['[', '{', 'Х'], 'L'), ([']', '}', 'Ъ'], 'L')]
litter_list_3 = [(['Ф', 'A'], 'R'), (['Ы', 'S'], 'R'), (['В', 'D'], 'R'), (['А', 'F'], 'R'), (['П', 'G'], 'R'),
                 (['Р', 'H'], 'L'), (['О', 'J'], 'L'), (['Л', 'K'], 'L'), (['Д', 'L'], 'L'), ([';', ':', 'Ж'], 'L'),
                 (["'", '"', 'Э'], 'L'), (['|', '/', '\\'], 'L')]
litter_list_4 = [(['Я', 'Z'], 'R'), (['Ч', 'X'], 'R'), (['С', 'C'], 'R'), (['М', 'V'], 'R'), (['И', 'B'], 'R'),
                 (['Т', 'N'], 'L'), (['Ь', 'M'], 'L'), ([',', '<', 'Б'], 'L'), (['.', '>', 'Ю'], 'L'),
                 (['?', ',', '/', '.'], 'L')]
litter_list_5 = [([' ', ' '], 'L')]
litter_lists = [litter_list_1, litter_list_2, litter_list_3, litter_list_4, litter_list_5]
lists = [list_1, list_2, list_3, list_4, list_5] = [list(), list(), list(), list(), list()]

from functions import *
from Button import Button

add_button = Button(120, 50)
change_font_button = Button(120, 50)
statistics_button = Button(120, 50)
exit_button = Button(100, 50)

txt_list = add_txt('asserts/Texts/text1.txt')
txt_short_list = [txt_list[i] for i in range(5)]
txt_string = txt_short_list[0]
input_txt = ''
counter_dict = dict.fromkeys(['mistakes_counter',
                              'letters_in_str_speed', 'words_in_str_speed',
                              'letters_counter', 'words_counter', 'letters_counter_str', 'mistakes_in_str',
                              'words/minute', 'litters/minute', 'time_for_string',
                              'start_time', 'counter'], 0)
