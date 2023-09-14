import generator
import pytest
import customer
import uuid


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
    example_customer: customer.Customer = customer.Customer(init_customer_list[0].id, init_customer_list[0].year_birth, init_customer_list[0].education, init_customer_list[0].marital_status,
                                                            init_customer_list[0].income, init_customer_list[0].kidhome, init_customer_list[
                                                                0].teenhome, init_customer_list[0].dt_customer,
                                                            init_customer_list[0].recency, init_customer_list[0].mnt_wines, init_customer_list[
                                                                0].mnt_fruits, init_customer_list[0].mnt_meat_products,
                                                            init_customer_list[0].mnt_fish_products, init_customer_list[
                                                                0].mnt_sweet_products, init_customer_list[0].mnt_gold_prods,
                                                            init_customer_list[0].num_deals_purchases, init_customer_list[
                                                                0].num_web_purchases, init_customer_list[0].num_catalog_purchases,
                                                            init_customer_list[0].num_store_purchases, init_customer_list[
                                                                0].num_web_visits_month, init_customer_list[0].accepted_cmp3,
                                                            init_customer_list[0].accepted_cmp4, init_customer_list[
                                                                0].accepted_cmp5, init_customer_list[0].accepted_cmp1,
                                                            init_customer_list[0].accepted_cmp2, init_customer_list[
                                                                0].complain, init_customer_list[0].z_cost_contact,
                                                            init_customer_list[0].z_revenue, init_customer_list[0].response)
    assert isinstance(example_customer.id, uuid.UUID)


def test_add_2_records_with_uuid() -> None:
    # n: int = 2
    # result: list[customer.Customer] = []
    pass


def test_random_year_2() -> None:
    result: int = generator.random_year(2000, 2)
    assert result >= 1998 and result <= 2002


def test_random_education(education_list) -> str:
    options: list[str] = ['2n cycle', 'Basic', 'Graduation', 'Master', 'PhD']
    result = generator.random_item_from_list(education_list)
    assert result[0] in options
    # assert result in options


def test_random_marital_status(marital_status_list) -> str:
    options: list[str] = ['Absurd', 'Alone', 'Divorced',
                          'Married', 'Single', 'Together', 'Widow', 'YOLO']
    result = generator.random_item_from_list(marital_status_list)
    assert result[0] in options
    # assert result in options


def test_random_income_per_education_and_marital_status_2ndcycle_Absurd() -> int:
    education: str = '2n cycle'
    marital_status: str = 'Absurd'
    result: int = generator.random_income_per_education_and_marital_status(
        education, marital_status)
    assert result < 3500


def test_random_income_per_education_and_marital_status_PhD_Married() -> int:
    education: str = 'PhD'
    marital_status: str = 'Married'
    result: int = generator.random_income_per_education_and_marital_status(
        education, marital_status)
    assert result > 4023 and result < 160803
