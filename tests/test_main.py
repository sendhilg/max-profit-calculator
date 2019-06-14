from io import StringIO

import pytest

from max_profit.__main__ import main


def test_main_for_valid_values_entered(monkeypatch, capsys):
    user_input = StringIO('2 3 4 5\n')
    monkeypatch.setattr('sys.stdin', user_input)
    main()
    captured = capsys.readouterr()
    assert 'Max profit: 3.0 (Buying for $2.0 and Selling for $5.0)' in captured.out


def test_main_for_no_values_entered(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))
    main()
    captured = capsys.readouterr()
    assert 'Error: Price values cannot be empty. Enter prices.' in captured.out


@pytest.mark.parametrize(
    'user_input', [
        ('I,N,V,A,L,I,D,F,O,R,M,A,T\n'),
        ('2 3 INVALID\n')
    ]
)
def test_main_for_invalid_values_entered(monkeypatch, capsys, user_input):
    input_str = StringIO(user_input)
    monkeypatch.setattr('sys.stdin', input_str)
    main()
    captured = capsys.readouterr()
    assert 'Error: Invalid price values. Enter numeric values for prices.' in captured.out
