from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по currency."""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Генерато описания транзакций"""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генерирует числа из заданного диапазона"""

    if 0 < start < stop <= 9999999999999999:
        for number in range(start, stop + 1):
            str_number = str(number)
            while len(str_number) != 16:
                str_number = "0" + str_number
            yield f"{str_number[0:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:16]}"
