import secrets
import string


def generate_password(length, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_symbols=True):
    if length < 1:
        raise ValueError("length must be a positive integer")

    char_sets = []
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        return None

    if length < len(char_sets):
        raise ValueError(
            f"length ({length}) must be at least the number of selected "
            f"character sets ({len(char_sets)})"
        )

    # Guarantee at least one character from each selected set.
    mandatory = [secrets.choice(cs) for cs in char_sets]
    all_chars = ''.join(char_sets)
    remainder = [secrets.choice(all_chars) for _ in range(length - len(mandatory))]
    password_chars = mandatory + remainder
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)
