# бесконечный цикл
# выход по нажатию кнопки
import os

CREATOR = 'Pavel & Co'

while True:
    print('\nМеню (Консольный файловый менеджер): ')
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('5. Посмотреть только файлы')
    print('6. Просмотр информации об операционной системе')
    print('7. Создатель программы')
    print('8. Играть в викторину')
    print('9. Мой банковский счет')
    print('10. Смена рабочей директории')
    print('11. Выход')
    print('-'*30)

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        pass
    if choice == '2':
        pass
    if choice == '3':
        pass
    # Просмотр содержимого рабочей директории
    if choice == '4':
        print(f'Содержимое дериктории {os.getcwd()}:')
        print(os.listdir(os.getcwd()))
        input('Для продолжения нажмите любую клавишу ...')
    if choice == '5':
        pass
    if choice == '6':
        pass
    if choice == '7':
        print('Разработчик программного продукта "Консольный файловый менеджер": ', CREATOR)
        input('Для продолжения нажмите любую клавишу ...')
    if choice == '8':
        pass
    if choice == '9':
        pass
    if choice == '10':
        pass
    # выход из программы
    if choice == '11':
        exit()