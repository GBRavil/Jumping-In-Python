import os

def rename_file_name(files_list: list, final_name: str, count: int, orig_extension: str, final_extension: str, orig_name_range: list):
    num = 0 
    for obj in files_list:
        exten = obj.split(".")
        if exten[1] == orig_extension:

            part_name = obj[orig_name_range[0]-1 : orig_name_range[1]-1]

            num += 1
            temp = len(str(num))
            number = ''
            for j in range(count-temp):
                number += '0'
            number += str(num) 

            new_name = f'{part_name}{final_name}{number}.{final_extension}' 
            print(f'{obj= }')
            print(f'{new_name= }')
            os.rename(f'{obj}', f'{new_name}')

            print('--------------')
        else: 
            print(f'{obj= }')


if __name__ == '__main__':
    files_list = ['testqwerty.txt', 'dataqwerty.txt', 'exampleqwerty.pdf']
    rename_file_name(files_list, "_TEST_", 3, "txt", "md", [1, 4])




