import sys

from .command import (Command, InvalidPriceValuesException,
                      NoPriceValuesException)


def main():
    command = Command()

    print(
        '\nEnter stock prices (values seperated by space e.g. 10 20.5 30.25 5 7)',
        'to get the max profit:\n'
    )

    for line in sys.stdin:
        try:
            max_profit, message = command.parse(line.strip('\n'))
            print(f'\nMax profit: {max_profit} {message}\n')
        except (InvalidPriceValuesException, NoPriceValuesException) as e:
            print(f'\nError: {e}\n')


if __name__ == "__main__":
    main()
