import generator
import pytest
import customer
import uuid

customer_list: list[customer.Customer] = generator.read_csv_into_customer_object(
    'marketing_campaign.csv')


def test_create_UUID() -> None:
    assert isinstance(generator.create_UUID(), uuid.UUID)


def test_create_UUID_is_unique() -> None:
    new_uuid: str = generator.create_UUID()
    assert generator.create_UUID() != new_uuid


def test_read_csv_record_is_not_empty() -> list:
    assert len(generator.read_csv_into_customer_object(
        'marketing_campaign.csv')) > 0


def test_record_is_assigned_a_uuid() -> None:
    customer_list = generator.create_record_with_uuid(customer_list[0:1])
    example_customer: customer.Customer = customer.Customer(customer_list[0].id, customer_list[0].year_birth, customer_list[0].education, customer_list[0].marital_status,
                                                            customer_list[0].income, customer_list[0].kidhome, customer_list[
                                                                0].teenhome, customer_list[0].dt_customer,
                                                            customer_list[0].recency, customer_list[0].mnt_wines, customer_list[
                                                                0].mnt_fruits, customer_list[0].mnt_meat_products,
                                                            customer_list[0].mnt_fish_products, customer_list[
                                                                0].mnt_sweet_products, customer_list[0].mnt_gold_prods,
                                                            customer_list[0].num_deals_purchases, customer_list[
                                                                0].num_web_purchases, customer_list[0].num_catalog_purchases,
                                                            customer_list[0].num_store_purchases, customer_list[
                                                                0].num_web_visits_month, customer_list[0].accepted_cmp3,
                                                            customer_list[0].accepted_cmp4, customer_list[
                                                                0].accepted_cmp5, customer_list[0].accepted_cmp1,
                                                            customer_list[0].accepted_cmp2, customer_list[
                                                                0].complain, customer_list[0].z_cost_contact,
                                                            customer_list[0].z_revenue, customer_list[0].response)
    assert isinstance(example_customer.id, uuid.UUID)


def test_add_2_records_with_uuid() -> None:
    n: int = 2
    result: list[customer.Customer] = []
    
        
