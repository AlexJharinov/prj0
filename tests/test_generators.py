from locale import currency

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return (
    [
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
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
    ]
)

@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
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
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {
                        "amount": "43318.34",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        },
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160"
                },

            ],
        ),
    ],
)



def test_filter_by_currency(transactions, currency, expected):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected

def test_filter_by_currency_empty_list():
    result = list(filter_by_currency(transactions = [], currency = "USD"))
    assert result == []

def test_filter_by_currency_no_matching():
    transactions_no_match = [
                   {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "JPY",
                        "code": "JPY"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
    ]
    result = list(filter_by_currency(transactions_no_match, currency = "USD"))
    assert result == []



def test_transaction_descriptions(transactions):
    operation = transaction_descriptions(transactions)
    assert next(operation) == "Перевод организации"
    assert next(operation) == "Перевод со счета на счет"

@pytest.mark.parametrize('start, stop, number', [
    (1, 5, [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]),
    (9999999999999994, 9999999999999999, [
        '9999 9999 9999 9994',
        '9999 9999 9999 9995',
        '9999 9999 9999 9996',
        '9999 9999 9999 9997',
        '9999 9999 9999 9998',
        '9999 9999 9999 9999',
    ]),
    (5, 1, [])
]
)
def test_card_number_generator(start, stop, number):
    num = list(x for x in card_number_generator(start, stop))
    assert num == number