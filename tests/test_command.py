from unittest.mock import patch

import pytest

from max_profit.command import (Command, InvalidPriceValuesException,
                                NoPriceValuesException)


@pytest.mark.parametrize(
    'user_input, input_to_parse', [
        ('2 3 4 5', [2.0, 3.0, 4.0, 5.0]),
        ('2.5 3.65 4.123 5.0', [2.5, 3.65, 4.123, 5.0])
    ]
)
@patch('max_profit.buy_sell.BuySell.max_profit_buy_sell_once', autospec=True)
def test_command_parse_for_valid_values_entered(mock_max_profit, user_input, input_to_parse):
    command = Command()
    command.parse(user_input)
    mock_max_profit.assert_called_once_with(command.buysell, input_to_parse)


@pytest.mark.parametrize(
    'user_input', [
        ('I,N,V,A,L,I,D,F,O,R,M,A,T'),
        ('2 3 INVALID')
    ]
)
@patch('max_profit.buy_sell.BuySell.max_profit_buy_sell_once', autospec=True)
def test_command_parse_for_invalid_values_entered(mock_max_profit, user_input):
    with pytest.raises(InvalidPriceValuesException):
        command = Command()
        command.parse(user_input)
    mock_max_profit.assert_not_called()


@patch('max_profit.buy_sell.BuySell.max_profit_buy_sell_once', autospec=True)
def test_command_parse_for_no_values_entered(mock_max_profit):
    with pytest.raises(NoPriceValuesException):
        command = Command()
        command.parse('')
    mock_max_profit.assert_not_called()
