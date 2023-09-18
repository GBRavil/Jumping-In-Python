# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

_LONG = [1, 3, 5, 7, 8, 10, 12]
_SHORT = [4, 6, 9, 11]
_FEB = 2

def _leap_year(a: int):
    if ((a % 400 == 0) or (a % 100 != 0) and (a% 4 == 0)): return True
    else: return False

def correct_date(date: str):
    final_date = []
    for n in date.split("."):
        final_date.append(int(n))
    if 1 <= final_date[2] <= 9999:
        if final_date[1] in _LONG:
            if 1 <= final_date[0] <= 31:
                return True
            else: return False
        elif final_date[1] in _SHORT:
            if 1 <= final_date[0] <= 30:
                return True
            else: return False    
        elif final_date[1] == _FEB:
            if _leap_year(final_date[2]) == True:
                if 1 <= final_date[0] <= 29:
                    return True
                else: return False
            else: 
                if 1 <= final_date[0] <= 28:
                    return True
                else: return False
        else: return False
    else: return False


print(_leap_year(2012))
print(correct_date("29.02.2012"))
