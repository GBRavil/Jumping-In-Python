import os

def add_dir_with_files(files_list: list) -> list:
    
    os.mkdir('Homeworks/HW_7/files')
    os.chdir('Homeworks/HW_7/files')

    for item in files_list: 
        with open(item, 'w', encoding='utf-8') as f:
            pass
    
    dir_list = os.listdir()
    return dir_list

if __name__ == '__main__':
    files_list = ['testqwerty.txt', 'dataqwerty.txt', 'exampleqwerty.pdf']

    print(add_dir_with_files(files_list))

