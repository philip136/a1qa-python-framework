import random
import string

CYRILLIC_MIN_CODE = 1040  # 'А'
CYRILLIC_MAX_CODE = 1103  # 'я'
SPECIAL_CHARS = "!@#$%&*"
DEFAULT_STRING_LENGTH = 10

DOMAINS = ("other", ".org", ".co.uk", ".net", ".gov", ".de", ".fr", ".nl", ".com", ".be", ".jpg")


def get_random_int(bound: int) -> int:
    """
    Returns a random integer between 0 (inclusive) and bound (exclusive).

    :param bound: Upper bound, exclusive.
    :return: Random integer.
    """
    return random.randrange(bound)


def generate_random_alphabetic_string(length: int = DEFAULT_STRING_LENGTH) -> str:
    """
    Generates a random string built from latin letters only.

    :param length: Number of characters to generate.
    :return: Random alphabetic string.
    """
    return "".join(random.choices(string.ascii_letters, k=length))


def generate_password(length: int = DEFAULT_STRING_LENGTH, email: str = "") -> str:
    """
    Generates a password satisfying the sign up form rules: it contains a capital
    letter, a lower case letter, a numeral, a special character, a cyrillic character
    and at least one letter taken from the given email.

    :param length: Total password length.
    :param email: Email the password must share a letter with.
    :return: Generated password.
    :raises ValueError: If the requested length cannot fit all the required characters.
    """
    required_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(SPECIAL_CHARS),
        chr(random.randint(CYRILLIC_MIN_CODE, CYRILLIC_MAX_CODE)),
    ]

    email_letters = [char for char in email if char.isalpha()]
    if email_letters:
        required_chars.append(random.choice(email_letters))

    if length < len(required_chars):
        raise ValueError(f"Password must be at least {len(required_chars)} characters long")

    password_chars = required_chars + list(generate_random_alphabetic_string(length - len(required_chars)))
    random.shuffle(password_chars)
    return "".join(password_chars)


def get_random_domain() -> str:
    """
    Returns a random domain postfix supported by the sign up form.

    :return: Domain postfix, e.g. '.com'.
    """
    return random.choice(DOMAINS)
