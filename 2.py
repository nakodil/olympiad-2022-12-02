import time


def double_reverse(num:int) -> int:
    """
    Если в числе справа есть ноль, то оно не дает остатка от деления на 10
    Зависнет с 0, но по условию задачи начинает с 1
    """
    while not num % 10:
        num //= 10
    return num


def test():
    tests = (
        8,
        19,
        72,
        445,
        648_772,  # 320666169 за 0.15744900703430176 секунд
        623_690_081,  # 836140895 за 157.10830116271973 секунд
        54_433_933_447,
        713_016_476_190_629,
        919_845_426_262_703_497,
        585_335_723_211_047_202
    )
    for num in tests:
        start_time = time.time()
        counter = 0
        for i in range(1, num + 1):
            counter += double_reverse(i)
        result = counter % (10 ** 9 + 7)
        total_time = time.time() - start_time
        print("Сумма", result, "для N =", num, "посчитана за", total_time, "секунд")
        

test()
