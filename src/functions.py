from Global import display, main_font, fonts, time, pygame, easygui


def print_txt(message, x, y, font_type=main_font, font_color=(0, 0, 0), font_size=26, condition=False, dspl=display):
    font_type = pygame.font.Font(font_type, font_size)
    message += '|' if condition else ''
    txt = font_type.render(message, True, font_color)
    dspl.blit(txt, (x, y))


def add_txt(txt=None):

    if txt is None:
        txt = easygui.fileopenbox()
    if txt is None or len(txt) < 4:
        return None
    elif txt[-4:len(txt)] != '.txt':
        return None
    print(txt)
    with open(txt, 'r') as f:
        a, s = list(), ''
        for i in [i for i in ' '.join('-'.join(f.read().split('—')).split('\n')).split(' ') if i != '']:
            if len(s) == 0:
                s = i
            elif len(s) + len(i) < 80:
                s = ' '.join([s, i])
            else:
                a.append(s)
                s = i
        a.append(s)
    return a


def statistics_table(counter_dict,  x=1200, y=20):
    print_txt('mistakes: ' + str(counter_dict['mistakes_counter']), x, y, 'asserts/Fonts/font_1.otf')  # ошибки
    print_txt('letters/minute in str: ' + str(counter_dict['letters_in_str_speed']), x, y + 30, 'asserts/Fonts/font_1.otf')
    print_txt('words/minute in str: ' + str(counter_dict['words_in_str_speed']), x, y + 60, 'asserts/Fonts/font_1.otf')
    print_txt('litters/minute: ' + str(counter_dict['letters_counter']), x, y + 90, 'asserts/Fonts/font_1.otf')
    print_txt('words/minute: ' + str(counter_dict['words_counter']), x, y + 120, 'asserts/Fonts/font_1.otf')

    if counter_dict['letters_counter_str'] > 0:
        print_txt('% of fails in string: ' +
                  str(int(100 * counter_dict['mistakes_in_str'] / counter_dict['letters_counter_str'])) +
                  '%', x, y + 150, 'asserts/Fonts/font_1.otf')
    else:
        print_txt('% of fails in string: 0%', x, y + 150, 'asserts/Fonts/font_1.otf')

    if counter_dict['letters_counter'] > 0:
        print_txt('total % of fails: ' +
                  str(int(100 * counter_dict['mistakes_counter'] / counter_dict['letters_counter'])) +
                  '%', x, y + 180, 'asserts/Fonts/font_1.otf')
    else:
        print_txt('total % of fails: 0%', x, y + 180, 'asserts/Fonts/font_1.otf')


def mist_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound('asserts/Sounds/mist_click.mp3'))


def change_font():
    fonts.append(fonts.pop(0))


def true_func():
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
        print_txt('Символов в минута', x, y)
        print_txt('% ошибок', x + 500, y)
        print_txt(' гггг-мм-дд   чч-мм-сс', x + 1000, y)

        if exit_button.draw(1400, 770, '   exit', true_func) is True:
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
