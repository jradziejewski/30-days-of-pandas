import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    joined = customers.merge(orders, how="left", left_on="id", right_on="customerId")

    return joined[joined["customerId"].isnull()]["name"].rename("Customers").to_frame()
