import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    condition = (world["population"] >= 25000000) | (world["area"] >= 3000000)
    result = world[condition]

    return result[["name", "population", "area"]]
