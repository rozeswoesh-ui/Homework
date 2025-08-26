def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    # Преобразуем в строку, если передано число
    if isinstance(card_number, int):
        card_number = str(card_number)

    cleaned_number = card_number.replace(" ", "")
    if not cleaned_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")

    if len(cleaned_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    first_part = cleaned_number[:4]
    second_part = cleaned_number[4:6]
    last_part = cleaned_number[-4:]

    masked_number = f"{first_part} {second_part}** **** {last_part}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Возвращает маску номера аккаунта в формате **XXXX
    """
    account_number_str = str(account_number)

    if len(account_number_str) != 20:
        raise ValueError("Неверная длина номера")

    mask_account = "**" + account_number_str[-4:]
    return mask_account
