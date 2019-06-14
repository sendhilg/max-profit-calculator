import pytest

from max_profit.buy_sell import BuySell


@pytest.mark.parametrize(
    'price_list, expected_max_profit, expected_message', [
        ([], 0.0, ''),
        ([1], 0.0, ''),
        ([1, 2], 1.0, '(Buying for $1 and Selling for $2)'),
        ([2, 1], 0.0, ''),
        ([2, 2], 0.0, ''),
        ([1, 2, 3], 2.0, '(Buying for $1 and Selling for $3)'),
        ([3, 2, 1], 0.0, ''),
        ([1, 3, 1, 1, 4], 3.0, '(Buying for $1 and Selling for $4)'),
        ([1, 5, 7, 3, 4], 6.0, '(Buying for $1 and Selling for $7)'),
        ([1, 5, 7.5, 3, 4], 6.5, '(Buying for $1 and Selling for $7.5)'),
    ]
)
def test_max_profit(price_list, expected_max_profit, expected_message):
    buysell = BuySell()
    max_profit, message = buysell.max_profit_buy_sell_once(price_list)
    assert max_profit == expected_max_profit
    assert message == expected_message
