from django.db import models
import string

allowed_symbols = (
    string.ascii_letters
    + "".join([str(symbol) for symbol in list(range(10))])
    + ".-_!@#"
)

# Create your models here.
def is_input_verified(input_: string) -> bool:
    for symbol in input_:
        if symbol not in allowed_symbols:
            return False

    return True


class SanitizationError(Exception):
    pass


def input_verificator(input_):

    if not is_input_verified(input_=input_):
        raise SanitizationError(f"not allowed input {input_}")
