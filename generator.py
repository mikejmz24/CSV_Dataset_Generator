import datetime
import uuid
import csv
import random
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


def random_year(year: int, random_diff: int = 5) -> int:
    year_min: int = year - random_diff
    year_max: int = year + random_diff
    return random.randrange(year_min, year_max)


def random_item_from_list(options: list[str]) -> str:
    # weights = ()
    weights = []
    print(len(options))
    if len(options) == 5:
        # weights = (9, 2, 50, 17, 22)
        weights = [9, 2, 50, 17, 22]
    else:
        # weights = (1, 1, 10, 38, 21, 25, 3, 1)
        weights = [1, 1, 10, 38, 21, 25, 3, 1]
    return random.choices(options, weights, k=1)
    # return random.choice(options)


# TODO: Add logic to create n records per list record
def create_multiple_records(record: list[customer.Customer], multiple: int) -> list[customer.Customer]:
    result: list[customer.Customer] = []
    for i in range(multiple):
        for row in record:
            row.id = create_UUID()
            result.append(row)
    return result


def home_childs(weights: list[int]) -> int:
    return random.choices([0, 1, 2], weights, k=1)


def random_income_per_education_and_marital_status(education: str, marital_status: str) -> int:
    if education == '2n Cycle':
        if marital_status == 'Divorced':
            return random.randrange(11448, 87305)
        elif marital_status == 'Married':
            return random.randrange(7500, 96547)
        elif marital_status == 'Single':
            return random.randrange(23331, 89572)
        elif marital_status == 'Together':
            return random.randrange(7500, 92556)
        elif marital_status == 'Widow':
            return random.randrange(28457, 74859)
        else:
            return random.randrange(1000, 3500)
    elif education == 'Basic':
        if marital_status == 'Divorced':
            return random.randrange(9548, 9600)
        elif marital_status == 'Married':
            return random.randrange(7500, 34445)
        elif marital_status == 'Single':
            return random.randrange(7500, 26868)
        elif marital_status == 'Together':
            return random.randrange(9772, 28389)
        elif marital_status == 'Widow':
            return random.randrange(22123, 23000)
        else:
            return random.randrange(1000, 3500)
    elif education == 'Graduation':
        if marital_status == 'Absurd':
            return random.randrange(79244, 80000)
        elif marital_status == 'Alone':
            return random.randrange(34176, 35000)
        elif marital_status == 'Divorced':
            return random.randrange(1730, 153924)
        elif marital_status == 'Single':
            return random.randrange(3502, 101970)
        elif marital_status == 'Together':
            return random.randrange(13672, 666666)
        elif marital_status == 'Widow':
            return random.randrange(27038, 85620)
        else:
            return random.randrange(1000, 3500)
    elif education == 'Master':
        if marital_status == 'Absurd':
            return random.randrange(65487, 66000)
        elif marital_status == 'Alone':
            return random.randrange(61331, 62000)
        elif marital_status == 'Divorced':
            return random.randrange(10979, 81380)
        elif marital_status == 'Single':
            return random.randrange(6560, 98777)
        elif marital_status == 'Together':
            return random.randrange(14661, 157733)
        elif marital_status == 'Widow':
            return random.randrange(33051, 84953)
        else:
            return random.randrange(1000, 3500)
    elif education == 'PhD':
        if marital_status == 'Alone':
            return random.randrange(35860, 36000)
        elif marital_status == 'Divorced':
            return random.randrange(14849, 90687)
        elif marital_status == 'Married':
            return random.randrange(4023, 160803)
        elif marital_status == 'Single':
            return random.randrange(7144, 113734)
        elif marital_status == 'Together':
            return random.randrange(5648, 162397)
        elif marital_status == 'Widow':
            return random.randrange(25358, 82571)
        elif marital_status == 'YOLO':
            return random.randrange(48432, 49000)
        else:
            return random.randrange(1000, 3500)
    else:
        return random.randrange(1000, 3500)


def random_kid_home_per_education_and_marital_status(education: str, marital: str) -> int:
    if education == '2n Cycle':
        if marital == 'Divorced':
            return home_childs([61, 39, 0])
        elif marital == 'Married':
            return home_childs([53, 44, 2])
        elif marital == 'Single':
            return home_childs([54, 43, 3])
        elif marital == 'Together':
            return home_childs([49, 51, 0])
        elif marital == 'Widow':
            return home_childs([80, 20, 0])
        else:
            return 0
    elif education == 'Basic':
        if marital == 'Divorced':
            return home_childs([0, 100, 0])
        elif marital == 'Married':
            return home_childs([50, 50, 0])
        elif marital == 'Single':
            return home_childs([17, 83, 0])
        elif marital == 'Together':
            return home_childs([42, 57, 0])
        elif marital == 'Widow':
            return home_childs([100, 0, 0])
        else:
            return 0
    elif education == 'Graduation':
        if marital == 'Absurd':
            return home_childs([100, 0, 0])
        elif marital == 'Alone':
            return home_childs([0, 100, 0])
        elif marital == 'Divorced':
            return home_childs([63, 34, 3])
        elif marital == 'Married':
            return home_childs([57, 41, 2])
        elif marital == 'Single':
            return home_childs([57, 42, 1])
        elif marital == 'Together':
            return home_childs([56, 41, 3])
        elif marital == 'Widow':
            return home_childs([69, 31, 0])
        else:
            return 0
    elif education == 'Master':
        if marital == 'Absurd':
            return home_childs([100, 0, 0])
        elif marital == 'Alone':
            return home_childs([100, 0, 0])
        elif marital == 'Divorced':
            return home_childs([54, 46, 0])
        elif marital == 'Married':
            return home_childs([55, 42, 3])
        elif marital == 'Single':
            return home_childs([55, 39, 7])
        elif marital == 'Together':
            return home_childs([59, 41, 0])
        elif marital == 'Widow':
            return home_childs([83, 17, 0])
        else:
            return 0
    elif education == 'PhD':
        if marital == 'Alone':
            return home_childs([100, 0, 0])
        elif marital == 'Divorced':
            return home_childs([60, 40, 0])
        elif marital == 'Married':
            return home_childs([61, 36, 3])
        elif marital == 'Single':
            return home_childs([61, 36, 3])
        elif marital == 'Together':
            return home_childs([62, 34, 3])
        elif marital == 'Widow':
            return home_childs([83, 17, 0])
        elif marital == 'YOLO':
            return home_childs([100, 0, 0])
        else:
            return 0
    else:
        return 0


def random_teen_home_per_education_and_marital_status(education: str, marital: str) -> int:
    if education == '2n Cycle':
        if marital == 'Divorced':
            return home_childs([52, 48, 0])
        elif marital == 'Married':
            return home_childs([63, 36, 1])
        elif marital == 'Single':
            return home_childs([59, 41, 0])
        elif marital == 'Together':
            return home_childs([60, 40, 0])
        elif marital == 'Widow':
            return home_childs([40, 60, 0])
        else:
            return 0
    elif education == 'Basic':
        if marital == 'Divorced':
            return home_childs([100, 0, 0])
        elif marital == 'Married':
            return home_childs([95, 5, 0])
        elif marital == 'Single':
            return home_childs([83, 17, 0])
        elif marital == 'Together':
            return home_childs([93, 7, 0])
        elif marital == 'Widow':
            return home_childs([100, 0, 0])
        else:
            return 0
    elif education == 'Graduation':
        if marital == 'Absurd':
            return home_childs([100, 0, 0])
        elif marital == 'Alone':
            return home_childs([100, 0, 0])
        elif marital == 'Divorced':
            return home_childs([44, 55, 2])
        elif marital == 'Married':
            return home_childs([52, 45, 3])
        elif marital == 'Single':
            return home_childs([62, 37, 2])
        elif marital == 'Together':
            return home_childs([50, 48, 2])
        elif marital == 'Widow':
            return home_childs([40, 60, 0])
        else:
            return 0
    elif education == 'Master':
        if marital == 'Absurd':
            return home_childs([100, 0, 0])
        elif marital == 'Alone':
            return home_childs([0, 100, 0])
        elif marital == 'Divorced':
            return home_childs([49, 51, 0])
        elif marital == 'Married':
            return home_childs([46, 50, 4])
        elif marital == 'Single':
            return home_childs([64, 35, 1])
        elif marital == 'Together':
            return home_childs([43, 56, 1])
        elif marital == 'Widow':
            return home_childs([42, 50, 8])
        else:
            return 0
    elif education == 'PhD':
        if marital == 'Alone':
            return home_childs([0, 100, 0])
        elif marital == 'Divorced':
            return home_childs([35, 58, 8])
        elif marital == 'Married':
            return home_childs([44, 54, 2])
        elif marital == 'Single':
            return home_childs([55, 40, 5])
        elif marital == 'Together':
            return home_childs([44, 51, 5])
        elif marital == 'Widow':
            return home_childs([29, 71, 0])
        elif marital == 'YOLO':
            return home_childs([0, 100, 0])
        else:
            return 0
    else:
        return 0


def date_parser(date_string: str) -> datetime.date:
    format: str = '%d/%m/%y'
    if '-' in date_string:
        format: str = '%d-%m-%Y'
    return datetime.datetime.strptime(date_string, format)


customer_list = read_csv_into_customer_object('marketing_campaign.csv')
customer_records: list[customer.Customer] = create_multiple_records(
    customer_list, 1)


# def print_record(records: list[customer.Customer]) -> None:
#     for record in records:
#         print(f'{record.id}')

# print(random_income_per_education_and_marital_status('2n cycle', 'Absurd'))

def random_date(start: datetime.datetime, end: datetime.datetime) -> datetime.datetime:
    delta: datetime.timedelta = end - start
    int_delta: int = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second: int = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


print(random_date(datetime.datetime(2012, 9, 4), datetime.datetime.today()))
