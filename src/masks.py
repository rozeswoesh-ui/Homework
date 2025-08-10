def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
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
    """Функция для маскировки номера счета"""
    cleaned_number = account_number.replace(" ", "")
    if not cleaned_number.isdigit():
        raise ValueError("Номер счёта должен состоять только из цифр")

    if len(cleaned_number) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    masked_account = f"**{cleaned_number[-4:]}"
    return masked_account
