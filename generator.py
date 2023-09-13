import uuid
import csv
import customer

customer_list: list[customer.Customer] = []


def create_UUID() -> uuid:
    return uuid.uuid4()


def read_csv_file_into_dict(file: str) -> dict:
    csv_dict: dict = {}
    with open('marketing_campaign.xls', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def read_csv_into_customer_object(file: str) -> list:
    result: list = []
    with open(file, 'r') as f:
        reader: csv.reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index > 0:
                result.append(customer.Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13],
                                                row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28]))
    return result


def create_customer_list_with_uuid(records: list[customer.Customer]) -> list[customer.Customer]:
    result: list[customer.Customer] = []
    for record in records:
        record.id = create_UUID()
        result.append(record)
    return result

# TODO: Add logic to create n records per list record
def create_multiple_records(record: list[customer.Customer], multiple: int) -> list[customer.Customer]:
    result: list[customer.Customer] = []
    for i in range(multiple):
        for row in record:
            result.append(row)
    return result


customer_list = read_csv_into_customer_object('marketing_campaign.csv')
customer_records: list[customer.Customer] = create_multiple_records(
    customer_list, 134)
print(len(customer_records))
