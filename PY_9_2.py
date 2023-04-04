class divzero(Exception):
    pass
try:
    dividend = int(input("делимое: "))
    divisor = int(input("делитель: "))
    if divisor == 0:
        raise divzero("делить на 0 нельзя")
    result = dividend / divisor
    print(f"результат деления: {result}")
except ValueError:
    print("прием, мы делим числа ")
except divzero as e:
    print(f"ошибка {e}")
