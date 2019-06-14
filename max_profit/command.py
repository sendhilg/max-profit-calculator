from .buy_sell import BuySell


class NoPriceValuesException(Exception):
    pass


class InvalidPriceValuesException(Exception):
    pass


class Command(object):
    def __init__(self):
        self.buysell = BuySell()

    def parse(self, line):
        try:
            prices = list(
                map(float, line.split())
            )
        except ValueError:
            raise InvalidPriceValuesException(
                'Invalid price values. Enter numeric values for prices.'
            )
        else:
            if not prices:
                raise NoPriceValuesException(
                    'Price values cannot be empty. Enter prices.'
                )

        return self.buysell.max_profit_buy_sell_once(prices)
