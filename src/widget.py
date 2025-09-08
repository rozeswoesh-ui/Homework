from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция обработки информации о картах и о счетах"""
    # Проверка на пустую строку и некорректные данные ДО любой обработки
    if not account_info or not isinstance(account_info, str) or account_info.strip() == "":
        return "Информация неверна"

    if account_info.startswith("Счет"):
        # Маскировка счета
        parts = account_info.split()
        # Проверяем длину ДО обращения к элементам
        if len(parts) < 2:
            return "Информация неверна"
        try:
            return f"Счет {get_mask_account(parts[-1])}"
        except ValueError:
            return "Информация неверна"
    else:
        # Маскировка карты
        parts = account_info.rsplit(" ", 1)
        # Проверяем длину ДО обращения к elements[1]
        if len(parts) < 2:
            return "Информация неверна"
        try:
            return f"{parts[0]} {get_mask_card_number(parts[1])}"
        except ValueError:
            return "Информация неверна"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата '2024-03-11T02:26:18.671407' в '11.03.2024'"""
    date_part = date_str[:10]
    year, month, day = date_part.split('-')
    return f'{day}.{month}.{year}'
