import datetime
import uuid
import csv
import random
import customer
import enum

customer_list: list[customer.Customer] = []


class Education(enum.Enum):
    SECOND_CYCLE = '2n Cycle'
    BASIC = 'Basic'
    GRADUATION = 'Graduation'
    MASTER = 'Master'
    PHD = 'PhD'


class Marital_Status(enum.Enum):
    ABSURD = 'Absurd'
    ALONE = 'Alone'
    DIVORCED = 'Divorced'
    MARRIED = 'Married'
    SINGLE = 'Single'
    TOGETHER = 'Together'
    WIDOW = 'Widow'
    YOLO = 'YOLO'


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


def create_customer_list_with_random_dates(records: list[customer.Customer]) -> list[customer.Customer]:
    result: list[customer.Customer] = []
    for record in records:
        parsed_date: datetime.datetime = date_parser(record.dt_customer)
        record.dt_customer = random_date(parsed_date)
        result.append(record)
    return result


def create_customer_list_complete(records: list[customer.Customer]) -> list[customer.Customer]:
    result: list[customer.Customer] = []
    for record in records:
        result.append(row_creation(record))
    return result


def create_customer_embedded_list(records: list[customer.Customer]) -> list[list[str]]:
    result: list[list[str]] = []
    for record in records:
        inner_result: list[str] = []
        inner_result.append(record.id)
        inner_result.append(record.year_birth)
        inner_result.append(record.education[0])
        inner_result.append(record.marital_status[0])
        inner_result.append(record.income)
        inner_result.append(record.kidhome[0])
        inner_result.append(record.teenhome[0])
        inner_result.append(record.dt_customer.date())
        inner_result.append(record.recency)
        inner_result.append(record.mnt_wines)
        inner_result.append(record.mnt_fruits)
        inner_result.append(record.mnt_meat_products)
        inner_result.append(record.mnt_fish_products)
        inner_result.append(record.mnt_sweet_products)
        inner_result.append(record.mnt_gold_prods)
        inner_result.append(record.num_deals_purchases)
        inner_result.append(record.num_web_purchases)
        inner_result.append(record.num_catalog_purchases)
        inner_result.append(record.num_store_purchases)
        inner_result.append(record.num_web_visits_month)
        inner_result.append(int(record.accepted_cmp3))
        inner_result.append(int(record.accepted_cmp4))
        inner_result.append(int(record.accepted_cmp5))
        inner_result.append(int(record.accepted_cmp1))
        inner_result.append(int(record.accepted_cmp2))
        inner_result.append(record.complain)
        inner_result.append(record.z_cost_contact)
        inner_result.append(record.z_revenue)
        inner_result.append(int(record.response))
        result.append(inner_result)
    return result


def random_int(number: int, random_diff: int = 5) -> int:
    number_min: int = number - random_diff
    number_max: int = number + random_diff
    result: int = random.randrange(number_min, number_max)
    if result < 0:
        result = abs(result)
    return result


def random_item_from_list(options: list[str]) -> str:
    # weights = ()
    weights = []
    if len(options) == 5:
        # weights = (9, 2, 50, 17, 22)
        weights = [9, 2, 50, 17, 22]
    else:
        # weights = (1, 1, 10, 38, 21, 25, 3, 1)
        weights = [1, 1, 10, 38, 21, 25, 3, 1]
    return random.choices(options, weights, k=1)
    # return random.choice(options)


def create_multiple_records(record: list[customer.Customer], multiple: int) -> list[customer.Customer]:
    result: list[customer.Customer] = []

    for i in range(multiple):
        for row in record:
            result.append(row_creation(row))
    return result


def row_creation(customer_record: customer.Customer) -> customer.Customer:
    education_options: list[str] = ['2n Cycle',
                                    'Basic', 'Graduation', 'Master', 'PhD']
    marital_options: list[str] = ['Absurd', 'Alone', 'Divorced',
                                  'Married', 'Single', 'Together', 'Widow', 'YOLO']
    return customer.Customer(
        create_UUID(),
        random_int(int(customer_record.year_birth)),
        random_item_from_list(education_options),
        random_item_from_list(marital_options),
        random_income_per_education_and_marital_status(
            customer_record.education, customer_record.marital_status),
        random_kid_home_per_education_and_marital_status(
            customer_record.education, customer_record.marital_status),
        random_teen_home_per_education_and_marital_status(
            customer_record.education, customer_record.marital_status),
        random_date(date_parser(customer_record.dt_customer)),
        random_int(int(customer_record.recency)),
        random_int(int(customer_record.mnt_wines), 50),
        random_int(int(customer_record.mnt_fruits)),
        random_int(int(customer_record.mnt_meat_products), 7),
        random_int(
            int(customer_record.mnt_fish_products), 20),
        random_int(
            int(customer_record.mnt_sweet_products), 10),
        random_int(int(customer_record.mnt_gold_prods), 7),
        random_int(
            int(customer_record.num_deals_purchases), 3),
        random_int(int(customer_record.num_web_purchases), 3),
        random_int(
            int(customer_record.num_catalog_purchases), 3),
        random_int(
            int(customer_record.num_store_purchases), 3),
        random_int(
            int(customer_record.num_web_visits_month), 3),
        random_bool(),
        random_bool(),
        random_bool(),
        random_bool(),
        random_bool(),
        customer_record.complain,
        customer_record.z_cost_contact,
        customer_record.z_revenue,
        random_bool()
    )


def home_childs(weights: list[int]) -> int:
    return random.choices([0, 1, 2], weights, k=1)


def random_income_per_education_and_marital_status(education: str, marital_status: str) -> int:
    if education == Education.SECOND_CYCLE.value:
        if marital_status == Marital_Status.DIVORCED.value:
            return random.randrange(11448, 87305)
        elif marital_status == Marital_Status.MARRIED.value:
            return random.randrange(7500, 96547)
        elif marital_status == Marital_Status.SINGLE.value:
            return random.randrange(23331, 89572)
        elif marital_status == Marital_Status.TOGETHER.value:
            return random.randrange(7500, 92556)
        elif marital_status == Marital_Status.WIDOW:
            return random.randrange(28457, 74859)
        else:
            return random.randrange(1000, 3500)
    elif education == Education.BASIC.value:
        if marital_status == Marital_Status.DIVORCED.value:
            return random.randrange(9548, 9600)
        elif marital_status == Marital_Status.MARRIED.value:
            return random.randrange(7500, 34445)
        elif marital_status == Marital_Status.SINGLE.value:
            return random.randrange(7500, 26868)
        elif marital_status == Marital_Status.TOGETHER.value:
            return random.randrange(9772, 28389)
        elif marital_status == Marital_Status.WIDOW:
            return random.randrange(22123, 23000)
        else:
            return random.randrange(1000, 3500)
    elif education == Education.GRADUATION.value:
        if marital_status == Marital_Status.ABSURD.value:
            return random.randrange(79244, 80000)
        elif marital_status == Marital_Status.ALONE.value:
            return random.randrange(34176, 35000)
        elif marital_status == Marital_Status.DIVORCED.value:
            return random.randrange(1730, 153924)
        elif marital_status == Marital_Status.SINGLE.value:
            return random.randrange(3502, 101970)
        elif marital_status == Marital_Status.TOGETHER.value:
            return random.randrange(13672, 666666)
        elif marital_status == Marital_Status.WIDOW:
            return random.randrange(27038, 85620)
        else:
            return random.randrange(1000, 3500)
    elif education == Education.MASTER.value:
        if marital_status == Marital_Status.ABSURD.value:
            return random.randrange(65487, 66000)
        elif marital_status == Marital_Status.ALONE.value:
            return random.randrange(61331, 62000)
        elif marital_status == Marital_Status.DIVORCED.value:
            return random.randrange(10979, 81380)
        elif marital_status == Marital_Status.SINGLE.value:
            return random.randrange(6560, 98777)
        elif marital_status == Marital_Status.TOGETHER.value:
            return random.randrange(14661, 157733)
        elif marital_status == Marital_Status.WIDOW:
            return random.randrange(33051, 84953)
        else:
            return random.randrange(1000, 3500)
    elif education == Education.PHD.value:
        if marital_status == Marital_Status.ALONE.value:
            return random.randrange(35860, 36000)
        elif marital_status == Marital_Status.DIVORCED.value:
            return random.randrange(14849, 90687)
        elif marital_status == Marital_Status.MARRIED.value:
            return random.randrange(4023, 160803)
        elif marital_status == Marital_Status.SINGLE.value:
            return random.randrange(7144, 113734)
        elif marital_status == Marital_Status.TOGETHER.value:
            return random.randrange(5648, 162397)
        elif marital_status == Marital_Status.WIDOW:
            return random.randrange(25358, 82571)
        elif marital_status == Marital_Status.YOLO.value:
            return random.randrange(48432, 49000)
        else:
            return random.randrange(1000, 3500)
    else:
        return random.randrange(1000, 3500)


def random_kid_home_per_education_and_marital_status(education: str, marital: str) -> int:
    if education == Education.SECOND_CYCLE.value:
        if marital == Marital_Status.DIVORCED.value:
            return home_childs([61, 39, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([53, 44, 2])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([54, 43, 3])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([49, 51, 0])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([80, 20, 0])
        else:
            return 0
    elif education == Education.BASIC.value:
        if marital == Marital_Status.DIVORCED.value:
            return home_childs([0, 100, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([50, 50, 0])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([17, 83, 0])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([42, 57, 0])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([100, 0, 0])
        else:
            return 0
    elif education == Education.GRADUATION.value:
        if marital == Marital_Status.ABSURD.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.ALONE.value:
            return home_childs([0, 100, 0])
        elif marital == Marital_Status.DIVORCED.value:
            return home_childs([63, 34, 3])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([57, 41, 2])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([57, 42, 1])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([56, 41, 3])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([69, 31, 0])
        else:
            return 0
    elif education == Education.MASTER.value:
        if marital == Marital_Status.ABSURD.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.ALONE.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.DIVORCED.value:
            return home_childs([54, 46, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([55, 42, 3])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([55, 39, 7])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([59, 41, 0])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([83, 17, 0])
        else:
            return 0
    elif education == Education.PHD.value:
        if marital == Marital_Status.ALONE.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.DIVORCED.value:
            return home_childs([60, 40, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([61, 36, 3])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([61, 36, 3])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([62, 34, 3])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([83, 17, 0])
        elif marital == Marital_Status.YOLO.value:
            return home_childs([100, 0, 0])
        else:
            return 0
    else:
        return 0


def random_teen_home_per_education_and_marital_status(education: str, marital: str) -> int:
    if education == Education.SECOND_CYCLE.value:
        if marital == Marital_Status.DIVORCED.value:
            return home_childs([52, 48, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([63, 36, 1])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([59, 41, 0])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([60, 40, 0])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([40, 60, 0])
        else:
            return 0
    elif education == Education.BASIC.value:
        if marital == Marital_Status.DIVORCED.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([95, 5, 0])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([83, 17, 0])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([93, 7, 0])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([100, 0, 0])
        else:
            return 0
    elif education == Education.GRADUATION.value:
        if marital == Marital_Status.ABSURD.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.ALONE.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.DIVORCED.value:
            return home_childs([44, 55, 2])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([52, 45, 3])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([62, 37, 2])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([50, 48, 2])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([40, 60, 0])
        else:
            return 0
    elif education == Education.MASTER.value:
        if marital == Marital_Status.ABSURD.value:
            return home_childs([100, 0, 0])
        elif marital == Marital_Status.ALONE.value:
            return home_childs([0, 100, 0])
        elif marital == Marital_Status.DIVORCED.value:
            return home_childs([49, 51, 0])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([46, 50, 4])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([64, 35, 1])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([43, 56, 1])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([42, 50, 8])
        else:
            return 0
    elif education == Education.PHD.value:
        if marital == Marital_Status.ALONE.value:
            return home_childs([0, 100, 0])
        elif marital == Marital_Status.DIVORCED.value:
            return home_childs([35, 58, 8])
        elif marital == Marital_Status.MARRIED.value:
            return home_childs([44, 54, 2])
        elif marital == Marital_Status.SINGLE.value:
            return home_childs([55, 40, 5])
        elif marital == Marital_Status.TOGETHER.value:
            return home_childs([44, 51, 5])
        elif marital == Marital_Status.WIDOW.value:
            return home_childs([29, 71, 0])
        elif marital == Marital_Status.YOLO.value:
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


def random_date(start: datetime.datetime) -> datetime.datetime:
    end: datetime.datetime = datetime.datetime.today()
    delta: datetime.timedelta = end - start
    int_delta: int = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second: int = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def random_bool() -> bool:
    return random.choice([True, False])


def write_to_csv(records: list[list[customer.Customer]]) -> None:
    header = ['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 'Kidhome', 'Teenhome', 'Dt_Customer', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases',
              'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Z_CostContact', 'Z_Revenue', 'Response']
    with open('new_marketing_campaign.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(records)


customer_list = read_csv_into_customer_object('marketing_campaign.csv')
customer_records: list[customer.Customer] = create_multiple_records(
    customer_list, 150)

modified_results: list[customer.Customer] = create_customer_list_complete(
    customer_list)
# write_to_csv(create_customer_embedded_list(modified_results))
write_to_csv(create_customer_embedded_list(customer_records))
