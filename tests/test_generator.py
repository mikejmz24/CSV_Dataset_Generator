import generator
import pytest
import customer
import uuid
import datetime


@pytest.fixture
def init_customer_list() -> list[customer.Customer]:
    customer_list: list[customer.Customer] = generator.read_csv_into_customer_object(
        'marketing_campaign.csv')
    yield customer_list


@pytest.fixture
def education_list() -> list[str]:
    result: list[str] = ['2n cycle', 'Basic', 'Graduation', 'Master', 'PhD']
    yield result


@pytest.fixture
def marital_status_list() -> list[str]:
    result: list[str] = ['Absurd', 'Alone', 'Divorced',
                         'Married', 'Single', 'Together', 'Widow', 'YOLO']
    yield result


def create_customer(items: list[customer.Customer], element: int = 0) -> customer.Customer:
    return customer.Customer(items[element].id, items[element].year_birth, items[element].education, items[element].marital_status,
                             items[element].income, items[element].kidhome, items[
        element].teenhome, items[element].dt_customer,
        items[element].recency, items[element].mnt_wines, items[
        element].mnt_fruits, items[element].mnt_meat_products,
        items[element].mnt_fish_products, items[
        element].mnt_sweet_products, items[element].mnt_gold_prods,
        items[element].num_deals_purchases, items[
        element].num_web_purchases, items[element].num_catalog_purchases,
        items[element].num_store_purchases, items[
        element].num_web_visits_month, items[element].accepted_cmp3,
        items[element].accepted_cmp4, items[
        element].accepted_cmp5, items[element].accepted_cmp1,
        items[element].accepted_cmp2, items[
        element].complain, items[element].z_cost_contact,
        items[element].z_revenue, items[element].response)


def test_create_UUID() -> None:
    assert isinstance(generator.create_UUID(), uuid.UUID)


def test_create_UUID_is_unique() -> None:
    new_uuid: str = generator.create_UUID()
    assert generator.create_UUID() != new_uuid


def test_read_csv_record_is_not_empty() -> list:
    assert len(generator.read_csv_into_customer_object(
        'marketing_campaign.csv')) > 0


def test_record_is_assigned_a_uuid(init_customer_list) -> None:
    init_customer_list = generator.create_customer_list_with_uuid(
        init_customer_list)
    example_customer: customer.Customer = create_customer(init_customer_list)
    assert isinstance(example_customer.id, uuid.UUID)


def test_record_is_assigned_a_random_datetime(init_customer_list) -> None:
    init_customer_list = generator.create_customer_list_with_random_dates(
        init_customer_list)
    example_customer: customer.Customer = create_customer(
        init_customer_list, 2)
    assert isinstance(example_customer.dt_customer, datetime.datetime)


def test_add_2_records_with_uuid() -> None:
    # n: int = 2
    # result: list[customer.Customer] = []
    pass


def test_random_int_2() -> None:
    result: int = generator.random_int(2000, 2)
    assert result >= 1998 and result <= 2002


def test_random_int_returns_positive() -> None:
    for x in range(50):
        result: int = generator.random_int(1)
        assert result >= 0


def test_random_education(education_list) -> None:
    options: list[str] = ['2n cycle', 'Basic', 'Graduation', 'Master', 'PhD']
    result = generator.random_item_from_list(education_list)
    assert result[0] in options
    # assert result in options


def test_random_marital_status(marital_status_list) -> None:
    options: list[str] = ['Absurd', 'Alone', 'Divorced',
                          'Married', 'Single', 'Together', 'Widow', 'YOLO']
    result = generator.random_item_from_list(marital_status_list)
    assert result[0] in options
    # assert result in options


def test_random_income_per_education_and_marital_status_2ndcycle_Absurd() -> None:
    education: str = '2n cycle'
    marital_status: str = 'Absurd'
    result: int = generator.random_income_per_education_and_marital_status(
        education, marital_status)
    assert result < 3500


def test_random_income_per_education_and_marital_status_PhD_Married() -> None:
    education: str = 'PhD'
    marital_status: str = 'Married'
    result: int = generator.random_income_per_education_and_marital_status(
        education, marital_status)
    assert result > 4023 and result < 160803


def test_date_parse_slash_format() -> None:
    parsed_date: datetime.date = generator.date_parser('4/9/12')
    assert parsed_date == datetime.datetime(2012, 9, 4)


def test_date_parse_hyphen_format() -> None:
    parsed_date: datetime.date = generator.date_parser('13-03-2014')
    assert parsed_date == datetime.datetime(2014, 3, 13)


def test_random_boolean() -> None:
    assert isinstance(generator.random_bool(), bool)
