def farengeit(x):
    solution = (x * 9/5) + 32
    return f'{x} градусов цельсия в фаренгейтах = {round(solution)}'


def celsia(y):
    solution_2 = (y - 32) * 5/9
    return f'из {y} фаренгейтов в цельсия = {round(solution_2)}'