from Global import pygame, display, main_font, fonts, max_str_len
import time
import easygui
from datetime import datetime


def print_txt(message, x, y, font_type=main_font, font_color=(0, 0, 0), font_size=26, condition=False, dspl=display):
    font_type = pygame.font.Font(font_type, font_size)
    message += '|' if condition else ''
    txt = font_type.render(message, True, font_color)
    dspl.blit(txt, (x, y))


def add_txt(txt=None):

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
            elif len(string) + len(word) < max_str_len:
                string = ' '.join([string, word])
            else:
                strings.append(string)
                string = word
        strings.append(string)
    return strings


def statistics_table(counter_dict,  x=1200, y=20):
    print_txt('Ошибки: ' + str(counter_dict['mistakes_counter']), x, y)  # ошибки
    print_txt('Символов в минуту в строке: ' + str(counter_dict['letters_in_str_speed']), x, y + 30)
    print_txt('Слов в минуту в строке: ' + str(counter_dict['words_in_str_speed']), x, y + 60)
    print_txt('Символов в минуту: ' + str(counter_dict['litters/minute']), x, y + 90)
    print_txt('Слов в минуту: ' + str(counter_dict['words/minute']), x, y + 120)

    if counter_dict['letters_counter'] > 0:
        mistakes = counter_dict['mistakes_counter']
        typed = (counter_dict['letters_counter'] + counter_dict['mistakes_counter'])
        print_txt('Ошибки: ' + str(int(100 * mistakes / typed)) + '%', x, y + 150)
    else:
        print_txt('Ошибки: 0%', x, y + 150)


def mist_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound('asserts/Sounds/mist_click.mp3'))


def change_font():
    fonts.append(fonts.pop(0))


def press_register():
    return True


def watch_stat():
    from Global import exit_button

    with open('asserts/Texts/statictics.txt', 'r') as f:
        a = f.read().split('\n')
    while len(a) > 20:
        a.pop(0)

    start = True
    while start:
        display.fill((255, 255, 255))
        x, y = 10, 10
        print_txt('Символов в минутy', x, y)
        print_txt('% ошибок', x + 500, y)
        print_txt(' гггг-мм-дд   чч-мм-сс', x + 1000, y)

        if exit_button.draw(1400, 770, '   exit', press_register()) is True:
            start = False
        for i in a:
            if i:
                y += 50
                b = i.split(' ')
                print_txt(' ' * 12 + b[0], x, y)
                print_txt('  ' + b[1], x + 500, y)
                print_txt(b[2] + ' ' + b[3], x + 1000, y)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                start = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        pygame.display.update()


def count(len_txt_string, txt_string, counter_dict: dict):
    counter_dict['letters_in_str_speed'] = int(60 * len_txt_string / (time.time() - counter_dict['time_for_string']))
    counter_dict['words_in_str_speed'] = int(60 * len(txt_string.split()) / (time.time() - counter_dict['time_for_string']))
    counter_dict['letters_counter'] += len_txt_string
    counter_dict['words_counter'] += len(txt_string.split())
    counter_dict['letters_counter_str'] = len_txt_string
    counter_dict['mistakes_in_str '] = 0
    counter_dict['words/minute'] = int(60 * counter_dict['words_counter'] / (time.time() - counter_dict['start_time']))
    counter_dict['litters/minute'] = int(60 * counter_dict['letters_counter'] / (time.time() - counter_dict['start_time']))
    counter_dict['time_for_string'] = time.time()


def record_statistics(counter_dict):
    with open('asserts/Texts/statictics.txt', 'a') as f:
        f.write(str(counter_dict['litters/minute']) + ' ' +
                str(int(100 * counter_dict['mistakes_counter'] / (counter_dict['letters_counter'] + 1))) + ' ' +
                str(datetime.now())[:-7] + '\n')
