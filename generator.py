import uuid
import csv
import customer

customer_list: list = []


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


def create_record_with_uuid(record: list[customer.Customer]) -> list:
    for row in record:
        new_uuid: str = create_UUID()
        row.id = new_uuid
    return list

customer_list = read_csv_into_customer_object('marketing_campaign.csv')
customr_list = create_record_with_uuid(customer_list)
print(customer_list[0:1])
