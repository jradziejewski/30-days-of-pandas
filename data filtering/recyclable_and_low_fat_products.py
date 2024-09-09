import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    condition = (products["low_fats"] == "Y") & (products["recyclable"] == "Y")

    return products[condition]["product_id"].to_frame()
