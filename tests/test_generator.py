import generator
import pytest


def test_create_UUID() -> None:
    assert len(generator.create_UUID()) > 0


def test_create_UUID_is_unique() -> None:
    new_uuid: str = generator.create_UUID()
    assert generator.create_UUID() != new_uuid


def test_read_csv_record_is_not_empty() -> list:
    assert len(generator.read_csv_into_customer_object('marketing_campaign.csv')) > 0


def test_record_is_assigned_a_uuid() -> None:
    pass