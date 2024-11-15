from typing import Any

def filter_by_state(data: list[dict[str, Any]], state: str="EXECUTED") -> list[dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'"""
    list_sort = []
    for i in data:
      if i['state'] == state:
        list_sort.append(i)
    return list_sort

def sort_by_date(data: list[dict[str, Any]], reverse: bool=True) -> list[dict[str, Any]]:
    """Сортирует список словарей по значению ключа 'date' """

    return sorted(data, key=lambda x: x["date"], reverse=reverse)