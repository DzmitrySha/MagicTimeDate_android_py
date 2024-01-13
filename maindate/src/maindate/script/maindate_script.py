"""
Main program logic functions
"""
import datetime as dt


def calculate_numerology(fulldate):
    """
    :param fulldate: полная дата datetime (год, месяц, день)
    :return: сумма цифр даты сложенная по правилам нумерологии
    """
    num = 0
    for i in fulldate:
        num += int(i)
    return num


def get_next_year(year):
    """
    :param year: год рождения
    :return: список 9 кризисных лет (в виде кортежа)
    """
    list_year = []
    for i in range(0, 9):
        num = calculate_numerology(str(year))
        year += num
        list_year.append(str(year))
    return ', '.join(tuple(list_year))


def get_main_years(year, month, day):
    while True:
        year = int(year)
        month = int(month)
        day = int(day)

        try:
            dt.date(year, month, day)
            break
        except (ValueError, TypeError):
            print("\nТакой даты не существует, введите правильную дату:\n")
            continue

    """ расчет """
    date_birth = dt.date(year, month, day)
    today = dt.date.today()
    fulldate = str(year) + str(month) + str(day)
    first_year = year + calculate_numerology(fulldate)
    next_year = get_next_year(first_year)

    """ вывод результата на экран в зависимости от даты рождения (в прошлом или в будущем) """
    if date_birth > today:
        return f'Скорее всего вы ещё не родились...\n\nКризисные годы для данной даты:\n{first_year}, {next_year}'
    else:
        return f'Вы родились {date_birth}.\n\nВаши кризисные годы: {first_year}, {next_year}'

