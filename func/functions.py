import os
import shutil
from tqdm import tqdm
from time import sleep

def get_info_about_function(function):
    def inner(*args, **kwargs):
        for i in tqdm(range(30), function.__doc__):
            sleep(.01)
        result = function(*args, **kwargs)
        return result
    return inner


def get_info_about_function_lite(function):
    def inner(*args, **kwargs):
        print(function.__doc__)
        result = function(*args, **kwargs)
        return result
    return inner

# функция вывода меню в консоли
def get_menu():
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
    print('-' * 30)


# функция проверияет наличие символов, т.к если они есть то на windows нарушается логика работы программы
def check_name_folder_or_file(name):
    return True if ('/' in name) or ('\\' in name) else False


# функция создания папки
@get_info_about_function
def create_folder(folder_name):
    """процедура создания папки ... """
    try:
        if check_name_folder_or_file(folder_name):
            raise OSError('Указаны неверные символы в названии папки')
        else:
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                return f'Создана папка {os.path.join(os.getcwd(), folder_name)}'
            else:
                return f'Папка с именем {folder_name} уже существует'
    except OSError as er:
        return f'Вы ввели неправильное имя папки, папка с именем {folder_name} не создана\n{er}'


# Функция ожидания ввода пользователем для продолжения выполнения программы
def wait_input():
    input('Для продолжения нажмите любую клавишу ...')


# функция удаления папки или файла
@get_info_about_function
def delete_file_folder(rm_folder_or_file):
    """процедура удаления папки или файла ..."""
    if check_name_folder_or_file(rm_folder_or_file):
        return 'Указаны неверные символы в названии папки'
    else:
        if os.path.exists(rm_folder_or_file):
            try:
                if os.path.isfile(rm_folder_or_file):
                    os.remove(rm_folder_or_file)
                    return f'Файл с именем {rm_folder_or_file} был удален'
                else:
                    os.rmdir(rm_folder_or_file)
                    return f'Папка с именем {rm_folder_or_file} была удалена'
            except OSError as er:
                return f'Удалить {rm_folder_or_file} не удалось, ошибка \n{er}'
        else:
            return f'Указанного файла/папки не существует'


# функция копироваия файла или папки
@get_info_about_function_lite
def copy_file_folder():
    """процедура копирования папки или файла ..."""
    result = 'Указаны неверные символы в названии'
    folder_or_file_old = input('Введите старое название папки или файла: ')
    if check_name_folder_or_file(folder_or_file_old):
        return result
    if os.path.exists(folder_or_file_old):
        try:
            if os.path.isfile(folder_or_file_old):
                folder_or_file_new = input('Введите новое название файла: ')
                if check_name_folder_or_file(folder_or_file_new):
                    return result
                shutil.copy(folder_or_file_old, folder_or_file_new)
                return f'Была создана копия файла {folder_or_file_old} на {folder_or_file_new}'
            else:
                folder_or_file_new = input('Введите новое название папки: ')
                if check_name_folder_or_file(folder_or_file_new):
                    return result
                shutil.copytree(folder_or_file_old, folder_or_file_new)
                return f'Была создана копия папки {folder_or_file_old} на {folder_or_file_new}'
        except OSError as er:
            return f'Указаны неверные символы в названии, \n{er}'
    else:
        return result


# функция отображения только папок
@get_info_about_function_lite
def look_only_folder():
    """процедура отображения только папок ..."""
    paths = [path for path in list(os.walk(os.getcwd()))[:1]]
    _, folders, _ = paths[0]
    return folders


# функция отображения только файлов
@get_info_about_function_lite
def look_only_files():
    """процедура отображения только файлов ..."""
    paths = [path for path in list(os.walk(os.getcwd()))[:1]]
    _, _, files = paths[0]
    return files


# функция сохр содержимого рабочей директории в файл listdir.txt
@get_info_about_function
def create_list_dir():
    """процедура сохр. содержимого рабочей директории в файл listdir.txt ..."""
    paths = [path for path in list(os.walk(os.getcwd()))[:1]]
    _, folders, files = paths[0]
    folders_str = 'dir: ' + ', '.join(folders) + '\n'
    files_str = 'files: ' + ', '.join(files) + '\n'

    with open(os.path.join('games', 'data', 'listdir.txt'), 'w') as f:
        f.write(files_str)
        f.write(folders_str)
    return 'Содержимое рабочей директории сохранено', os.path.join('games', 'data', 'listdir.txt')
