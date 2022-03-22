import os
import shutil

# функция создания папки
def create_folder():
    print(f'Содержимое дериктории {os.getcwd()}:')
    folder_name = input('Введине название папки: ')
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        os.mkdir(folder_name)
        print(f'Создана папка {os.path.join(os.getcwd(), folder_name)}')
    else:
        print(f'Папка с именем {folder_name} уже существует')

# Функция ожидания ввода пользователем для продолжения выполнения программы
def wait_input():
    input('Для продолжения нажмите любую клавишу ...')


# функция удаления папки
def delete_file_folder():
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


# функция копироваия файла или папки
def copy_file_folder():
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

# функция отображения только папок
def look_only_folder():
    print(f'Содержимое папок дериктории {os.getcwd()}:')
    paths = [path for path in list(os.walk(os.getcwd()))[:1]]
    _, folders, _ = paths[0]
    return folders

# функция отображения только файлов
def look_only_files():
    print(f'Содержимое файлов дериктории {os.getcwd()}:')
    paths = [path for path in list(os.walk(os.getcwd()))[:1]]
    _, _, files = paths[0]
    return files