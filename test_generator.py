import generator
import pytest

def test_increment() -> bool:
    assert generator.increment(2) == 3


def test_create_UUID() -> bool:
    assert len(generator.create_UUID()) > 0


def test_create_UUID_is_unique() -> bool:
    new_uuid: str = generator.create_UUID()
    assert generator.create_UUID() != new_uuid