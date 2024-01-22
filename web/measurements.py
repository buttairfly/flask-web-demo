import random
import string
from datetime import datetime


def _get_timestamp() -> str:
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def _get_value() -> str:
    return f"{random.random():.3f}"


def _get_random_name(length: int) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def _generate_measurement() -> dict[str, str]:
    return {
        "name": _get_random_name(10),
        "value": _get_value(),
        "timestamp": _get_timestamp(),
    }


def _generate_set(length: int) -> list[dict[str, str]]:
    return [_generate_measurement() for _ in range(length)]


def read_all() -> list[dict[str, str]]:
    return _generate_set(2)
