from unittest.mock import mock_open, patch

from src.utils import conversion_values, json_read


@patch("builtins.open", new_callable=mock_open, read_data='{"test_mock": {"mock": "ok", "open": "yes"}}')
def test_json_read(mock_file):
    expected_result = {'test_mock': {'mock': 'ok', 'open': 'yes'}}
    result = json_read('test_file')
    assert result == expected_result


def test_error_json_read():
    file = "/test_error/not_found"
    assert json_read(file) == []
    assert json_read(None) == []


@patch('requests.request')

def test_conversion_values(mock_get):
    mock_get.return_value.json.return_value = {
        "query": {"amount": 100, "from": "USD", "to": "RUB"},
        "result": 3642.723,
    }
    assert conversion_values(
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ) == 3642.723