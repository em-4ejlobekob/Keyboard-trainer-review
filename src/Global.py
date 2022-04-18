import time
import easygui
from datetime import datetime
import pygame


pygame.init()
process = True
fonts = ['asserts/Fonts/font_1', 'asserts/Fonts/font_2', 'asserts/Fonts/font_3', 'asserts/Fonts/font_4', 'asserts/Fonts/font_5']
main_font = fonts[0] + '.otf'
display = pygame.display.set_mode((1600, 900))

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
