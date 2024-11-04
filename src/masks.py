def get_mask_card_number(card_number: str) -> str:
    """Функция макскирует номера принимаемых карт"""
    return f"{card_number[0:4]} {card_number[4:6]}  ** {card_number[12:16]}"


def get_mask_account(card_number: str) -> str:
    """Функция возвращает последние 4 числа в формате (**ХХХХ-где Х это число)"""
    return f"**{card_number[12:16]}"
