from basic_multplication import Multiplication
from basic_division import Division

multiplication = Multiplication(3)
division = Division(4)


def print_packages():
    print(multiplication.multiply(10))
    print(division.divide(20))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_packages()

