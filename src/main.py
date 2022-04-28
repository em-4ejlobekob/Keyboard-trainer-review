import time
import pygame
import functions as func
import variables as var

from buttons import exit_button
from Global import counter_dict, fonts, display, process
from keyboard import left_shift, right_shift, key_dict


input_txt = ''
txt_list = func.add_txt('asserts/Texts/text1.txt')
txt_short_list = [txt_list[i] for i in range(var.lines)]
txt_string = txt_short_list[0]
counter_dict['start_time'] = time.time()
counter_dict['time_for_string'] = time.time()


while process:
    counter_dict['counter'] += 1
    main_font = fonts[0] + '.otf'
    display.fill(var.dspl_color)

    if exit_button.draw(var.exit_x, var.exit_y, '   exit', func.press_register) is True:
        process = func.exit_func(counter_dict)

    for event in pygame.event.get():  # перебираем события

        if event.type == pygame.QUIT:
            process = func.exit_func(counter_dict)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_txt = input_txt[:-1]

            elif len(txt_string) == len(input_txt):
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    func.count(txt_string, counter_dict)
                    input_txt = ''

                    if len(txt_list) > 1:
                        txt_list.pop(0)
                        txt_short_list = [txt_list[i] for i in range(min(var.lines, len(txt_list)))]
                        txt_string = txt_short_list[0]
                    else:
                        txt_short_list = [input_txt]
                        txt_string = 'End!'
                else:
                    func.mist_sound()

            elif event.unicode and event.key != pygame.K_ESCAPE:
                tmp_unicode, tmp_letter = event.unicode, txt_string[len(input_txt)]
                if tmp_letter != tmp_unicode:
                    counter_dict['mistakes_counter'] += 1
                    counter_dict['mistakes_in_str'] += 1
                    func.mist_sound()
                    key_dict[tmp_letter.upper()].mists = min(var.mist_limit, key_dict[tmp_letter.upper()].mists + var.mist_fine)
                    if tmp_letter.isupper():
                        if key_dict[tmp_letter.upper()].shift == 'L':
                            left_shift.mists = min(var.mist_limit, left_shift.mists + var.mist_fine)
                        else:
                            right_shift.mists = min(var.mist_limit, right_shift.mists + var.mist_fine)

                else:
                    input_txt += tmp_unicode
                    key_dict[tmp_unicode.upper()].mists = max(0, key_dict[tmp_unicode.upper()].mists - var.mist_bonus)
                    if tmp_unicode.isupper():
                        if key_dict[tmp_unicode.upper()].shift == 'L':
                            left_shift.mists = max(0, left_shift.mists - var.mist_bonus)
                        else:
                            right_shift.mists = max(0, right_shift.mists - var.mist_bonus)

    new_txt = func.draw_interface(counter_dict, txt_short_list, txt_string, input_txt, main_font)
    if new_txt is not None:
        txt_list, txt_short_list, txt_string = func.add_new_txt(new_txt)

    counter_dict['counter'] %= var.counter_division
    pygame.display.update()
