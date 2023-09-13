import pytest

from sys import argv


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date() -> bool:
    str_date = input("Введите дату: ")
    day, mon, yaer = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= yaer <= 9999):
        return False

    if mon in (4, 6, 9, 11) and day > 30:
        return False

    if mon == 2 and day > 29:
        return False

    if mon == 2 and if_leap(yaer) and day > 29:
        return False

    if mon == 2 and not if_leap(yaer) and day > 28:
        return False

    return True

def test_if_leap():
    assert if_leap(2024), False

if __name__ == '__main__':
    pytest.main(['-v'])
