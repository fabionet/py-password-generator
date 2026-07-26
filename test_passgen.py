import string
from passgen_core import generate_password


def test_default_length():
    password = generate_password(12)
    assert len(password) == 12


def test_custom_length():
    for length in (8, 16, 32):
        assert len(generate_password(length)) == length


def test_uppercase_only():
    password = generate_password(50, use_uppercase=True, use_lowercase=False,
                                 use_digits=False, use_symbols=False)
    assert all(c in string.ascii_uppercase for c in password)


def test_lowercase_only():
    password = generate_password(50, use_uppercase=False, use_lowercase=True,
                                 use_digits=False, use_symbols=False)
    assert all(c in string.ascii_lowercase for c in password)


def test_digits_only():
    password = generate_password(50, use_uppercase=False, use_lowercase=False,
                                 use_digits=True, use_symbols=False)
    assert all(c in string.digits for c in password)


def test_symbols_only():
    password = generate_password(50, use_uppercase=False, use_lowercase=False,
                                 use_digits=False, use_symbols=True)
    assert all(c in string.punctuation for c in password)


def test_no_charset_returns_none():
    result = generate_password(12, use_uppercase=False, use_lowercase=False,
                               use_digits=False, use_symbols=False)
    assert result is None


def test_all_charsets():
    password = generate_password(100)
    all_chars = (string.ascii_uppercase + string.ascii_lowercase
                 + string.digits + string.punctuation)
    assert all(c in all_chars for c in password)


def test_returns_string():
    password = generate_password(10)
    assert isinstance(password, str)
