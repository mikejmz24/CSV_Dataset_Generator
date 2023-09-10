import uuid

def increment(x: int) -> int:
    return x + 1

def create_UUID() -> str:
    return str(uuid.uuid4())