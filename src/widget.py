from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_info: str) -> str:
    """Функция обработки информации о картах и о счетах"""
    if account_info.startswith("Счет"):
        # Маскировка счета
        parts = account_info.split()
        return f"Счет {get_mask_account(parts[-1])}"
    else:
        parts = account_info.rsplit(' ', 1)  # Разделяем по последнему пробелу
        return f"{parts[0]} {get_mask_card_number(parts[1])}"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата '2024-03-11T02:26:18.671407' в '11.03.2024'"""
    date_part = date_str[:10]  # "2024-03-11"
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"