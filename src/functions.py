import time
import easygui
import variables as var

from datetime import datetime
from keyboard import draw_keyboard, draw_active_keys
from Global import pygame, display, main_font, fonts
from buttons import add_button, change_font_button, statistics_button, exit_button


def print_txt(message, x, y, font_type=main_font, font_color=(0, 0, 0),
              font_size=var.txt_font_size, condition=False, dspl=display):
    """Выводит текст в указанной точке (х, у)"""
    font_type = pygame.font.Font(font_type, font_size)
    message += '|' if condition else ''
    txt = font_type.render(message, True, font_color)
    dspl.blit(txt, (x, y))


def add_txt(txt=None):
    """Загружает текст в поле для печати, если выбран текстовый файл, иначе возвращает значение None"""
    if txt is None:
        txt = easygui.fileopenbox()
    if txt is None or len(txt) < 4 or txt[-4:len(txt)] != '.txt':
        return None

    with open(txt, 'r') as f:
        strings, string = list(), ''
        file_strings = ' '.join('-'.join(f.read().split('—')).split('\n')).split(' ')
        # Разбиваем текстовый файл по символам '—' (его нет на клавиатуре) и собираем в исходный файл с символом '-',
        # который есть на клавиатуре. Затем разбиваем весь файл на отдельные строки
        for word in [string for string in file_strings if string != '']:
            if len(string) == 0:
                string = word
            elif len(string) + len(word) < var.max_str_len:
                string = ' '.join([string, word])
            else:
                strings.append(string)
                string = word
        strings.append(string)
    return strings


def draw_statistics_table(counter_dict,  x=var.statistics_table_x, y=var.statistics_table_y):
    """Выводит статистику печати в точку (х, у)"""
    print_txt('Символов в минуту в строке: ' + str(counter_dict['letters_in_str_speed']), x, y + var.indention * 1)
    print_txt('Слов в минуту в строке: ' + str(counter_dict['words_in_str_speed']), x, y + var.indention * 2)
    print_txt('Символов в минуту: ' + str(counter_dict['litters/minute']), x, y + var.indention * 3)
    print_txt('Слов в минуту: ' + str(counter_dict['words/minute']), x, y + var.indention * 4)

    mistakes = counter_dict['mistakes_counter']
    if counter_dict['letters_counter'] + counter_dict['mistakes_counter']:
        typed = (counter_dict['letters_counter'] + counter_dict['mistakes_counter'])
    else:
        typed = 1
    per_of_mistakes = str(int(var.to_percent * mistakes / typed))
    print_txt('Ошибки: ' + str(mistakes) + ' (' + per_of_mistakes + '%)', x, y)


def mist_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound(var.mist_sound_path))


def change_font():
    fonts.append(fonts.pop(0))


def press_register():
    return True


def watch_stat():
    """Открывает окно со статистикой за последнее время"""
    with open(var.statistics_path, 'r') as f:
        stat_strs = f.read().split('\n')
    while len(stat_strs) > var.last_stat:
        stat_strs.pop(0)

    start = True
    while start:
        display.fill(var.dspl_color)
        x, y = var.stat_x, var.stat_y
        print_txt('Символов в минутy', x, y)
        print_txt('% ошибок', x + var.indention_stat_x * 1, y)
        print_txt('ГГГГ-ММ-ДД ЧЧ-ММ-СС', x + var.indention_stat_x * 2, y)

        if exit_button.draw(var.exit_x, var.exit_y, '   exit', press_register) is True:
            start = False
        for string in stat_strs:
            if string:
                y += var.indention_stat_y
                info = string.split(' ')
                print_txt(' ' * var.stat_space_dist + info[0], x, y)
                print_txt('   ' + info[1], x + var.indention_stat_x * 1, y)
                print_txt(info[2] + '     ' + info[3], x + var.indention_stat_x * 2, y)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                start = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        pygame.display.update()


def count(txt_string, counter_dict: dict):
    """Подсчитывает данные статистики и записывает в словарь counter_dict"""
    len_txt_string = len(txt_string)
    time_for_string = time.time() - counter_dict['time_for_string']
    all_time = time.time() - counter_dict['start_time']
    counter_dict['letters_counter'] += len_txt_string
    counter_dict['words_counter'] += len(txt_string.split())
    counter_dict['letters_counter_str'] = len_txt_string
    counter_dict['mistakes_in_str '] = 0
    counter_dict['time_for_string'] = time.time()
    counter_dict['letters_in_str_speed'] = int(var.seconds * len_txt_string / time_for_string)
    counter_dict['words_in_str_speed'] = int(var.seconds * len(txt_string.split()) / time_for_string)
    counter_dict['words/minute'] = int(var.seconds * counter_dict['words_counter'] / all_time)
    counter_dict['litters/minute'] = int(var.seconds * counter_dict['letters_counter'] / all_time)


def record_statistics(counter_dict):
    """Записывает статистику набора текста в файл со статистикой"""
    with open(var.statistics_path, 'a') as f:
        litters_in_min = str(counter_dict['litters/minute'])
        per_of_mistakes = str(int(var.to_percent * counter_dict['mistakes_counter'] / (counter_dict['letters_counter'] + 1)))
        date = str(datetime.now())[:var.exact_time]
        f.write(litters_in_min + ' ' + per_of_mistakes + ' ' + date + '\n')


def exit_func(counter_dict: dict):
    if counter_dict['litters/minute']:
        record_statistics(counter_dict)
    return False


def draw_dividing_line():
    """Рисует линию, которая разделяет напечатанныйл текст и текст, который надо напечатать"""
    for i in range(var.number_of_links):
        display.blit(pygame.image.load(var.sep_line_path), (var.separator_x * i, var.separator_y))


def draw_next_strings(txt_short_list, font):
    """Печатает ближайшие 5 строк, которые надо напечатать"""
    for i in range(len(txt_short_list)):
        print_txt(txt_short_list[i], var.start_txt_x, var.start_txt_y + var.indention * i, font)


def add_new_txt(new_txt):
    """Загружает новый текст либо возвращает None, если текста нет"""
    txt_list = new_txt
    txt_short_list = [txt_list[i] for i in range(var.lines if len(txt_list) >= var.lines else len(txt_list))]
    txt_string = txt_short_list[0]
    return txt_list, txt_short_list, txt_string


def draw_main_line(txt_string, counter_dict, input_text, font):
    """Печатает строку, в которую вводятся символы"""
    print_txt(txt_string, var.input_str_x, var.input_str_y, font, var.back_input_color)
    condition = True if counter_dict['counter'] // var.end_line_division % 2 else False
    print_txt(input_text, var.input_str_x, var.input_str_y, font, condition=condition)


def draw_buttons():
    """Рисует кнопки изменения шрифта, вывода статистики и загрузки нового текста"""
    change_font_button.draw(var.change_font_x, var.change_font_y, 'next font', change_font)
    statistics_button.draw(var.statistics_x, var.statistics_y, 'statistics', watch_stat)
    return add_button.draw(var.add_x, var.add_y, 'add text', add_txt)


def draw_interface(counter_dict, txt_short_list, txt_string, input_text, font):
    """Рисует интерфейс"""
    draw_keyboard()
    draw_dividing_line()
    draw_statistics_table(counter_dict)
    draw_next_strings(txt_short_list, font)
    draw_main_line(txt_string, counter_dict, input_text, font)
    if len(input_text) < len(txt_string):
        draw_active_keys(txt_string, len(input_text))
    return draw_buttons()
