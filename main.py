# бесконечный цикл
# выход по нажатию кнопки
import sys
import platform
import games.account as acc
from games.victory import victory
from games.account import account, open_session_history, open_session_balance
from func.functions import *

CREATOR = 'Pavel & Co'
OLD_DIR = os.getcwd()
BALANCE = acc.BALANCE
HISTORY = acc.HISTORY

while True:
    # Пока выполняется программа загружаются последние данные о балансе счета и истории покупок
    total_cash = open_session_balance(BALANCE)
    history = open_session_history(HISTORY)

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
    print('13. Сохранить содержимое рабочей директории в файл')
    print('14. Выход')
    print('-'*30)

    choice = input('Выберите пункт меню: ')
    # Создать папку
    if choice == '1':
        print(f'Содержимое дериктории {os.getcwd()}:')
        folder_name = input('Введине название папки: ')
        print(create_folder(folder_name))
        wait_input()
    # Удалить (файл/папку)
    elif choice == '2':
        rm_folder_or_file = input('Введите название папки или файла: ')
        print(delete_file_folder(rm_folder_or_file))
        wait_input()
    # Копировать (файл/папку)
    elif choice == '3':
        copy_file_folder()
        wait_input()
    # Просмотр содержимого рабочей директории
    elif choice == '4':
        print(f'Содержимое дериктории {os.getcwd()}:')
        print(os.listdir(os.getcwd()))
        wait_input()
    # Посмотреть только папки
    elif choice == '5':
        print(f'Содержимое папок дериктории {os.getcwd()}:')
        print(look_only_folder())
        wait_input()
    # Посмотреть только файлы
    elif choice == '6':
        print(f'Содержимое файлов дериктории {os.getcwd()}:')
        print(look_only_files())
        wait_input()
    # Просмотр информации об операционной системе
    elif choice == '7':
        print('Информации об операционной системе:')
        for i in platform.uname():
            print(i)
        wait_input()
    elif choice == '8':
        print('Разработчик программного продукта "Консольный файловый менеджер": ', CREATOR)
        wait_input()
    # Играть в викторину'
    elif choice == '9':
        print('Вы выбрали меню играть в викторину')
        print('#'*30)
        victory()
    # Мой банковский счет
    elif choice == '10':
        account(total_cash, history)
    # Смена рабочей директории
    elif choice == '11':
        print('Введите директорию в нотиации своей ОС на которую хотите перейти: ')
        path_dir = input('Директория: ')
        os.chdir(path_dir)
        print(f'Текущая директория: {os.getcwd()}')
        wait_input()
    # выход из программы
    elif choice == '12':
        print('Возврат к исходной директории ... ')
        os.chdir(OLD_DIR)
        print(f'Текущая директория: {os.getcwd()}')
        wait_input()
    elif choice == '13':
        print(create_list_dir()[0])
        wait_input()
    elif choice == '14':
        exit()