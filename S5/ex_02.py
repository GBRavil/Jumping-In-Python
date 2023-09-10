# Написать функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def get_tuple(path):
    *path_el, name_ext = path.split('/')
    name, extension = name_ext.split('.')
    return '/'.join(path_el) + '/', name, extension

all_path = '/Users/Равиль/Downloads/ex_02.py'

print(get_tuple(all_path))
