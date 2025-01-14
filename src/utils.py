import json



def json_read(file_):
    """
    Принимает на вход путь до JSON-файла, возврщает данные о финансовых транзакциях
    """
    operations_list = []

    with open(file_, 'r', encoding='utf8') as f:
        data = json.load(f)
    return








def conversion_value():
    pass


