import json

from src.external_api import convert_amount
from src.logging_set import logger


def json_read(file_):
    """
    Принимает на вход путь до JSON-файла, возврщает данные о финансовых транзакциях
    """
    logger.info(f'{file_}: opening attempt.')
    operations_list = []
    try:
        with open(file_, 'r', encoding='utf8') as f:
            data = json.load(f)
            logger.info(f'{file_}: ok.')
        logger.info('Operation is completed.')
        return data

    except Exception:
        logger.error('File cannot be opened.')
        return operations_list


def conversion_values(transaction):
    """
    Принмает транзакцию, возвращает ее сумму
    """

    logger.info('Data transmission.')

    if transaction['operationAmount']['currency']['code'] == 'RUB':
        logger.info('No conversion is required. Calculation.')
        logger.info('Operation is completed.')
        return transaction['operationAmount']['amount']

    elif transaction['operationAmount']['currency']['code'] != 'RUB':
        logger.info('Conversion required.')
        conv_currency = convert_amount(
            transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['code']
        )
        logger.info('Calculation.')
        logger.info('Operation is completed.')
        return conv_currency

