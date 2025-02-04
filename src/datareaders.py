import csv

import pandas as pd

from src.logging_set import logger

def get_open_csv_file(file_):
    """Принимает на вход csv файл, возвращает данные о финансовых транзакциях"""

    logger.info(f'{file_}: opening attemp.')
    list_transaction = []

    try:
        with open(file_, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            logger.info(f'{file_}: ok.')
            for row in reader:
                list_transaction.append(row)
            logger.info('Operation is completed')
            return list_transaction

    except Exception:
        logger.error('File cannot be opened.')
        return list_transaction


def get_open_xlsx_file(_file_):
    """Принимает на вход xlsx файл, возвращает данные о финансовых транзакциях"""

    logger.info(f'{_file_}: opening attemp.')

    try:
        reader = pd.read_excel(_file_)
        list_transaction = reader.to_dict(orient='records')
        logger.info(f'{_file_}: ok.')
        logger.info('Operation is completed.')
        return list_transaction

    except Exception:
        logger.error('File cannot be opened.')
        return []
