import json
import os
from http.client import responses

import requests
from dotenv import load_dotenv


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
    """
    Принмает транзакцию, возвращает ее сумму
    """
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return transaction['operationAmount']['amount']

    elif transaction['operationAmount']['currency']['code'] != 'RUB':
        conv_currency = convert_amount(transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['code'])

        return conv_currency

def convert_amount(amount, currency):
    """
    Принимает сумму и валюту, возвращает сумму в Руб
    """

    load_dotenv()

    api_key = os.getenv("API_KEY")
    headdiers = {"api_key": api_key}

    payload = {}
    url =
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()["result"]
    return result