from src.logging_set import  logger

def get_mask_card_number(card_number: str) -> str:
    """Функция макскирует номера принимаемых карт"""
    logger.info('Masking the card number started.')
    logger.info('Operation is completed.')
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def get_mask_account(card_number: str) -> str:
    logger.info('Masking the account number started.')
    """Функция возвращает последние 4 числа в формате (**ХХХХ-где Х это число)"""
    logger.info('Operation is completed.')
    return f"**{card_number[16:20]}"
