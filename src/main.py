from keyboard import *
from Global import *

counter_dict['start_time'] = time.time()
counter_dict['time_for_string'] = time.time()


while process:
    counter_dict['counter'] += 1
    main_font = fonts[0] + '.otf'
    display.fill((255, 255, 255))
    len_txt_string = len(txt_string)
    if exit_button.draw(1400, 770, '   exit', press_register) is True:
        process = False
        if counter_dict['litters/minute']:
            record_statistics(counter_dict)

    for event in pygame.event.get():  # перебираем события

        if event.type == pygame.QUIT:
            process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
            if counter_dict['litters/minute']:
                record_statistics(counter_dict)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_txt = input_txt[:-1]

            elif len_txt_string == len(input_txt):
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:

                    count(len_txt_string, txt_string, counter_dict)
                    input_txt = ''

                    if len(txt_list) > 1:
                        txt_list.pop(0)
                        txt_short_list = [txt_list[i] for i in range(5)] if len(txt_list) >= 5 else [i for i in txt_list]
                        txt_string = txt_short_list[0]
                    else:
                        txt_short_list = ['']
                        txt_string = 'End!'
                else:
                    mist_sound()

            elif event.unicode and event.key != pygame.K_ESCAPE:

                tmp_unicode, tmp_letter = event.unicode, txt_string[len(input_txt)]
                if tmp_letter != tmp_unicode:
                    counter_dict['mistakes_counter'] += 1
                    counter_dict['mistakes_in_str'] += 1
                    mist_sound()
                    # input_txt += tmp_unicode
                    key_dict[tmp_letter.upper()].mists = min(65, key_dict[tmp_letter.upper()].mists + 5)
                    if tmp_letter.isupper():
                        if key_dict[tmp_letter.upper()].shift == 'L':
                            left_shift.mists = min(65, left_shift.mists + 5)
                        else:
                            right_shift.mists = min(65, right_shift.mists + 5)

                else:

                    input_txt += tmp_unicode
                    key_dict[tmp_unicode.upper()].mists = max(0, key_dict[tmp_unicode.upper()].mists - 1)
                    if tmp_unicode.isupper():
                        if key_dict[tmp_unicode.upper()].shift == 'L':
                            left_shift.mists = max(0, left_shift.mists - 1)
                        else:
                            right_shift.mists = max(0, right_shift.mists - 1)

    len_input_txt = len(input_txt)

    print_txt(txt_string, 50, 200, main_font, (200, 200, 200))
    print_txt(input_txt, 50, 200, main_font) if counter_dict['counter'] // 25 % 2 else print_txt(input_txt, 50, 200, main_font, condition=True)

    change_font_button.draw(100, 50, 'next font', change_font)
    new_txt = add_button.draw(240, 50, 'add text', add_txt)
    statistics_button.draw(380, 50, 'statistics', watch_stat)
    draw_keyboard()
    statistics_table(counter_dict)

    for i in range(100):
        display.blit(pygame.image.load('asserts/Textures/x.png'), (16 * i, 240))

    for i in range(len(txt_short_list)):
        print_txt(txt_short_list[i], 50, 266 + 30 * i, main_font)

    if new_txt is not None:
        txt_list = new_txt
        txt_short_list = [txt_list[i] for i in range(5 if len(txt_list) >= 5 else len(txt_list))]
        txt_string = txt_short_list[0]

    if len_input_txt < len_txt_string:
        key_dict[txt_string[len_input_txt].upper()].draw(condition=True)
        if txt_string[len_input_txt] != ' ' and txt_string[len_input_txt].isupper():
            if key_dict[txt_string[len_input_txt].upper()].shift == 'L':
                left_shift.draw(condition=True)
            else:
                right_shift.draw(condition=True)

    pygame.display.update()
    counter_dict['counter'] %= 1000
