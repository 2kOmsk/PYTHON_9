class NeNumber(Exception):
    pass
try:
    your_numbers = []
    while True:
        value = input("вводи числа, стоп слово 'ladyli'): ")
        if value == "ladyli":
            break
        if not value.isdigit():
            raise NeNumber("в списке мастхев онли намберс")
        your_numbers.append(int(value))
    print(f"список чисел: {your_numbers}")
except NeNumber as e:
    print(f"ошибка {e}")
