# Keyboard-trainer-review
Клавиатурный тренажёр на python3.

Запуск проекта:

```
sudo apt update 
pip install pygame
python -m pip install easygui
git clone https://github.com/em-4ejlobekob/Keyboard-trainer-review.git -b dev
cd Keyboard-trainer-review/src
python3 main.py
```
Вас встретит один из дефолтных текстов, который уже загружен в проект.

[Главное поле](pictures/main.jpg)


Чтобы поменять текст, нужно нажать кнопку __add text__ и выбрать в проводнике нужный, либо перейти __src__ > __asserts__ > __Texts__ и выбрать один из предложенных текстов.


Кнопка __next font__ метяет шрифт. 

[Нестандартный шрифт](pictures/font2.jpg)

[Рукописный шрифт](pictures/font4.jpg)


Кнопка __statistics__ открывает окно со статистикой за последнее время.

[Статистика](pictures/stat.jpg)


Жёлтым цветом подсвечиваются кнопки, которые нужно сейчас нажать.
Чем чаще вы не попадаете по кнопке, тем она становится краснее. Если удачно попадать на кнопки, которые уже стали красными, то постепенно они снова будут становиться зелёными.

[Тепловая карта](pictures/hitmap.jpg)


