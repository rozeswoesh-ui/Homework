from datetime import datetime


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция которая фильтрует списки
    словарей по нужному параметру
    """
    return [item for item in data if item.get("state") == state]


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
