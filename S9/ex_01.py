# Написать следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой
# тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл

import csv
import json
import os.path
from random import randint as ri
from typing import Callable

__all__ = ['deco_run_find_roots', 'gen_rand_nums2csv', 'find_quadratic_equation_roots',
           'add_param_to_json']

MIN_LINES_QTY = 100
MAX_LINES_QTY = 1000
COEFS_QTY = 3
MIN_NUM = -100
MAX_NUM = 100

path_csv = './ex_01_coefs.scv'
path_json = './ex_01_solutions.json'


def deco_run_find_roots(func: Callable) -> Callable:
    """Декоратор, запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла.
    """
    gen_rand_nums2csv()

    def wrapper(_csv=path_csv):
        with open(_csv, 'r', encoding='utf-8') as f_read:
            csv_reader = csv.reader(f_read)
            for row in csv_reader:
                a, b, c = map(int, row)
                if (a, b, c) and a != 0:
                    func(a, b, c)
    return wrapper


def gen_rand_nums2csv(_csv=path_csv, min_qty=MIN_LINES_QTY, max_qty=MAX_LINES_QTY,
                      coefs=COEFS_QTY, start_num=MIN_NUM, end_num=MAX_NUM):
    """Генерация csv файла с тремя случайными числами в каждой строке."""
    with open(_csv, 'w', encoding='utf-8', newline='') as f_csv:
        csv_writer = csv.writer(f_csv, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for row in range(ri(min_qty, max_qty + 1)):
            csv_writer.writerow([ri(start_num, end_num + 1)
                                 for _ in range(coefs)])


def add_param_to_json(func: Callable) -> Callable:
    """Декоратор, сохраняющий переданные параметры и
    результаты работы функции в json файл.
    """
    results = []
    if os.path.exists(path_json):
        with open(path_json, 'r', encoding='utf-8') as f_json:
            results = json.load(f_json)

    def wrapper(*args):
        result = func(*args)
        solution_dict = {'args': args, 'result': result}
        results.append(solution_dict)

        with open(path_json, 'w', encoding='utf-8') as f_write:
            json.dump(results, f_write, indent=2, ensure_ascii=False)
        return result
    return wrapper


@deco_run_find_roots
@add_param_to_json
def find_quadratic_equation_roots(a: int, b: int, c: int) -> \
        tuple[float, float] | float | str:
    """Нахождение корней квадратного уравнения"""
    d = b ** 2 - 4 * a * c
    if d < 0:
        result = 'Действительных корней нет'
    elif d == 0:
        result = round(-b / (2 * a))
    else:
        result = round(((-b + d ** 0.5) / (2 * a)), 2), \
                 round(((-b - d ** 0.5) / (2 * a)), 2)
    return result


if __name__ == '__main__':
    find_quadratic_equation_roots()
