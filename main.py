# бесконечный цикл
# выход по нажатию кнопки
import os
import shutil

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
    # Создать папку
    if choice == '1':
        print(f'Содержимое дериктории {os.getcwd()}:')
        folder_name = input('Введине название папки: ')
        if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
            os.mkdir(folder_name)
            print(f'Создана папка {os.path.join(os.getcwd(), folder_name)}')
        else:
            print(f'Папка с именем {folder_name} уже существует')
        input('Для продолжения нажмите любую клавишу ...')
    # Удалить (файл/папку)
    if choice == '2':
        rm_folder_or_file = input('Введите название папки или файла: ')
        if os.path.exists(rm_folder_or_file):
            if '.' in rm_folder_or_file:
                os.remove(rm_folder_or_file)
                print(f'Файл с именем {rm_folder_or_file} был удален')
            else:
                os.rmdir(rm_folder_or_file)
                print(f'Папка с именем {rm_folder_or_file} была удалена')
        else:
            print(f'Указанной Вами файла/папки не существует')
        input('Для продолжения нажмите любую клавишу ...')
    # Копировать (файл/папку)
    if choice == '3':
        folder_or_file_old = input('Введите старое название папки или файла: ')
        if os.path.exists(folder_or_file_old):
            if '.' in folder_or_file_old:
                folder_or_file_new = input('Введите новое название файла: ')
                shutil.copy(folder_or_file_old, folder_or_file_new)
                print(f'Была создана копия файла {folder_or_file_old} на {folder_or_file_new}')
            else:
                folder_or_file_new = input('Введите новое название папки: ')
                shutil.copytree(folder_or_file_old, folder_or_file_new)
                print(f'Была создана копия папки {folder_or_file_old} на {folder_or_file_new}')
        else:
            print(f'Указанной Вами файла/папки не существует')
        input('Для продолжения нажмите любую клавишу ...')
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