# бесконечный цикл
# выход по нажатию кнопки
import os
import shutil
import platform
from games.victory import victory
from games.account import accaunt
from func.functions import *

CREATOR = 'Pavel & Co'
OLD_DIR = os.getcwd()

while True:
    print('\nМеню (Консольный файловый менеджер): ')
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выбрать исходную директорию')
    print('13. Выход')
    print('-'*30)

    choice = input('Выберите пункт меню: ')
    # Создать папку
    if choice == '1':
        create_folder()
        wait_input()
    # Удалить (файл/папку)
    if choice == '2':
        delete_file_folder()
        wait_input()
    # Копировать (файл/папку)
    if choice == '3':
        copy_file_folder()
        wait_input()
    # Просмотр содержимого рабочей директории
    if choice == '4':
        print(f'Содержимое дериктории {os.getcwd()}:')
        print(os.listdir(os.getcwd()))
        wait_input()
    # Посмотреть только папки
    if choice == '5':
        print(look_only_folder())
        wait_input()
    # Посмотреть только файлы
    if choice == '6':
        print(look_only_files())
        wait_input()
    # Просмотр информации об операционной системе
    if choice == '7':
        print('Информации об операционной системе:')
        for i in platform.uname():
            print(i)
        wait_input()
    if choice == '8':
        print('Разработчик программного продукта "Консольный файловый менеджер": ', CREATOR)
        wait_input()
    # Играть в викторину'
    if choice == '9':
        print('Вы выбрали меню играть в викторину')
        print('#'*30)
        victory()
    # Мой банковский счет
    if choice == '10':
        print('Вы выбрали меню "Мой банковский счет"')
        print('$'*30)
        accaunt()
    # Смена рабочей директории
    if choice == '11':
        print('Введите директорию в нотиации своей ОС на которую хотите перейти: ')
        path_dir = input('Директория: ')
        os.chdir(path_dir)
        print(f'Текущая директория: {os.getcwd()}')
        wait_input()
    # выход из программы
    if choice == '12':
        print('Возврат к исходной директории ... ')
        os.chdir(OLD_DIR)
        print(f'Текущая директория: {os.getcwd()}')
        wait_input()
    if choice == '13':
        exit()