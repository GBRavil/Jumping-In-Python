import os
import sys
from pprint import pprint
import json
import csv
import pickle


def size_of_dir (dir_path: str) -> int:
    total_size = 0
    for path, _, files in os.walk(dir_path):
        for file in files:
            total_size += sys.getsizeof(os.path.join(path, file))
    return total_size

def json_writer(current_path: str, source: dict[str, dict]):
    name = os.path.join(current_path, "result.json")
    with open(name, 'w', encoding='UTF-8') as data:
        json.dump(source, data, indent=4, ensure_ascii=False)

def csv_writer(current_path: str, source: dict[str, dict]):
    name = os.path.join(current_path, "result.csv")
    file = [['Full_path', 'name', 'parent_dir', 'type', "size"]]
    for key, item in source.items():
        file.append([key, *item.values()])
    with open(name, 'w', encoding='UTF-8') as data:
        write_csv = csv.writer(data, dialect='excel', delimiter=';')
        write_csv.writerows(file)



def pickle_writer(current_path: str, source: dict[str, dict]):
    name = os.path.join(current_path, "result.bin")
    with open(name, 'wb') as data:
        pickle.dump(source, data)



def dir_walker(full_path: str = os.getcwd()):
    result = {}
    for path, dir_list, file_list in os.walk(full_path):
        for cur_dir in dir_list:
            result[os.path.join(path, cur_dir)] = {'name': cur_dir,
                                                    'path': path,
                                                    'type': 'DIR',
                                                    'size': size_of_dir(os.path.join(path, cur_dir))}
        for cur_file in file_list:
            result[os.path.join(path, cur_file)] = {'name': cur_file,
                                                    'path': path,
                                                    'type': 'FILE',
                                                    'size': sys.getsizeof(os.path.join(path, cur_file))}
    json_writer(full_path, result)
    pickle_writer(full_path, result)
    csv_writer(full_path, result)
    return result

pprint(dir_walker('E:\General'))
