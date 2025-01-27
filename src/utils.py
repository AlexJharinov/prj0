import json

from src.external_api import convert_amount



def json_read(file_):
    """
    Принимает на вход путь до JSON-файла, возврщает данные о финансовых транзакциях
    """
    operations_list = []
    try:
        with open(file_, 'r', encoding='utf8') as f:
            data = json.load(f)
        return data

    except Exception:
        return operations_list


def conversion_values(transaction):
    """
    Принмает транзакцию, возвращает ее сумму
    """
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return transaction['operationAmount']['amount']

    elif transaction['operationAmount']['currency']['code'] != 'RUB':
        conv_currency = convert_amount(
            transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['code']
        )

        return conv_currency

