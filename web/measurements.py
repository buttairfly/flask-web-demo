from datetime import datetime
import random, string

def get_timestamp() -> str:
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def get_value() -> str:
    return f"{random.random():.3f}"

def randomword(length: int) -> str:
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))

def generate_measurement() -> dict[str,str]:
    return dict({
        "name": randomword(10),
        "value": get_value(),
        "timestamp": get_timestamp(),
    })

def generate_set(length: int) -> list[dict[str,str]]:
    return list([generate_measurement() for _ in range(length)])

def read_all():
    return generate_set(20)
