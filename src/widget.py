from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_inf: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    if "Счет" in card_inf:  # Проверка по типу карта/счет
        return card_inf.replace(
            card_inf[-20:], get_mask_account(card_inf[-16:])
        )  # Возвращает счет с подменой последних 16 значений
    else:
        return card_inf.replace(
            card_inf[-16:], get_mask_card_number(card_inf[-16:])
        )  # Возвращает счет с подменой последних 16 значений


def get_date(data_inf: str) -> str:
    """Возвращает информацию о дате в формате число.месяц.год"""
    return f"{data_inf[8:10]}.{data_inf[5:7]}.{data_inf[0:4]}"
