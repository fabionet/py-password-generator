import secrets
import string


def generate_password(length, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_symbols=True):
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

    all_chars = ''.join(char_sets)
    return ''.join(secrets.choice(all_chars) for _ in range(length))
