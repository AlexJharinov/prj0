import json



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



def conversion_value(transaction):
    if transaction['operationAmount']['currency']['code'] == ('RUB')
        return transaction['operationAmount']['amount']
    pass


