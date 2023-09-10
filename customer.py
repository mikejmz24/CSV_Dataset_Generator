from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast
import uuid


T = TypeVar("T")

def from_uuid(uuid: Any) -> uuid:
    assert isinstance(uuid, uuid) and not isinstance(uuid, bool)
    return uuid


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class CustomerElement:
    id: uuid
    year_birth: int
    education: str
    marital_status: str
    income: int
    kidhome: int
    teenhome: int
    dt_customer: str
    recency: int
    mnt_wines: int
    mnt_fruits: int
    mnt_meat_products: int
    mnt_fish_products: int
    mnt_sweet_products: int
    mnt_gold_prods: int
    num_deals_purchases: int
    num_web_purchases: int
    num_catalog_purchases: int
    num_store_purchases: int
    num_web_visits_month: int
    accepted_cmp3: int
    accepted_cmp4: int
    accepted_cmp5: int
    accepted_cmp1: int
    accepted_cmp2: int
    complain: int
    z_cost_contact: int
    z_revenue: int
    response: int

    @staticmethod
    def from_dict(obj: Any) -> 'CustomerElement':
        assert isinstance(obj, dict)
        id = from_uuid(obj.get("ID"))
        year_birth = from_int(obj.get("Year_Birth"))
        education = from_str(obj.get("Education"))
        marital_status = from_str(obj.get("Marital_Status"))
        income = from_int(obj.get("Income"))
        kidhome = from_int(obj.get("Kidhome"))
        teenhome = from_int(obj.get("Teenhome"))
        dt_customer = from_str(obj.get("Dt_Customer"))
        recency = from_int(obj.get("Recency"))
        mnt_wines = from_int(obj.get("MntWines"))
        mnt_fruits = from_int(obj.get("MntFruits"))
        mnt_meat_products = from_int(obj.get("MntMeatProducts"))
        mnt_fish_products = from_int(obj.get("MntFishProducts"))
        mnt_sweet_products = from_int(obj.get("MntSweetProducts"))
        mnt_gold_prods = from_int(obj.get("MntGoldProds"))
        num_deals_purchases = from_int(obj.get("NumDealsPurchases"))
        num_web_purchases = from_int(obj.get("NumWebPurchases"))
        num_catalog_purchases = from_int(obj.get("NumCatalogPurchases"))
        num_store_purchases = from_int(obj.get("NumStorePurchases"))
        num_web_visits_month = from_int(obj.get("NumWebVisitsMonth"))
        accepted_cmp3 = from_int(obj.get("AcceptedCmp3"))
        accepted_cmp4 = from_int(obj.get("AcceptedCmp4"))
        accepted_cmp5 = from_int(obj.get("AcceptedCmp5"))
        accepted_cmp1 = from_int(obj.get("AcceptedCmp1"))
        accepted_cmp2 = from_int(obj.get("AcceptedCmp2"))
        complain = from_int(obj.get("Complain"))
        z_cost_contact = from_int(obj.get("Z_CostContact"))
        z_revenue = from_int(obj.get("Z_Revenue"))
        response = from_int(obj.get("Response"))
        return CustomerElement(id, year_birth, education, marital_status, income, kidhome, teenhome, dt_customer, recency, mnt_wines, mnt_fruits, mnt_meat_products, mnt_fish_products, mnt_sweet_products, mnt_gold_prods, num_deals_purchases, num_web_purchases, num_catalog_purchases, num_store_purchases, num_web_visits_month, accepted_cmp3, accepted_cmp4, accepted_cmp5, accepted_cmp1, accepted_cmp2, complain, z_cost_contact, z_revenue, response)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID"] = from_uuid(self.id)
        result["Year_Birth"] = from_int(self.year_birth)
        result["Education"] = from_str(self.education)
        result["Marital_Status"] = from_str(self.marital_status)
        result["Income"] = from_int(self.income)
        result["Kidhome"] = from_int(self.kidhome)
        result["Teenhome"] = from_int(self.teenhome)
        result["Dt_Customer"] = from_str(self.dt_customer)
        result["Recency"] = from_int(self.recency)
        result["MntWines"] = from_int(self.mnt_wines)
        result["MntFruits"] = from_int(self.mnt_fruits)
        result["MntMeatProducts"] = from_int(self.mnt_meat_products)
        result["MntFishProducts"] = from_int(self.mnt_fish_products)
        result["MntSweetProducts"] = from_int(self.mnt_sweet_products)
        result["MntGoldProds"] = from_int(self.mnt_gold_prods)
        result["NumDealsPurchases"] = from_int(self.num_deals_purchases)
        result["NumWebPurchases"] = from_int(self.num_web_purchases)
        result["NumCatalogPurchases"] = from_int(self.num_catalog_purchases)
        result["NumStorePurchases"] = from_int(self.num_store_purchases)
        result["NumWebVisitsMonth"] = from_int(self.num_web_visits_month)
        result["AcceptedCmp3"] = from_int(self.accepted_cmp3)
        result["AcceptedCmp4"] = from_int(self.accepted_cmp4)
        result["AcceptedCmp5"] = from_int(self.accepted_cmp5)
        result["AcceptedCmp1"] = from_int(self.accepted_cmp1)
        result["AcceptedCmp2"] = from_int(self.accepted_cmp2)
        result["Complain"] = from_int(self.complain)
        result["Z_CostContact"] = from_int(self.z_cost_contact)
        result["Z_Revenue"] = from_int(self.z_revenue)
        result["Response"] = from_int(self.response)
        return result


def customer_from_dict(s: Any) -> List[CustomerElement]:
    return from_list(CustomerElement.from_dict, s)


def customer_to_dict(x: List[CustomerElement]) -> Any:
    return from_list(lambda x: to_class(CustomerElement, x), x)
