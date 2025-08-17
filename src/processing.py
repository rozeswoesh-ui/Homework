from datetime import datetime


def filter_by_state(list_not_filtered: list, state: str = "EXECUTED") -> list:
    """
    Функция которая фильтрует списки
    словарей по нужному параметру
    """
    list_filtered = []
    for dict_item in list_not_filtered:
        for item in dict_item.values():
            if item == state:
                list_filtered.append(dict_item)
    return list_filtered


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция которая принимает список словарей
    и необязательный параметр, задающий порядок сортировки.
    Функция должны возвращать новый список отсортированный по дате(date).
    """
    return sorted(
        data,
        key=lambda item: datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )
