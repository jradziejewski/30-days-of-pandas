import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients["conditions"] = patients["conditions"].astype(str).str.strip()
    return patients[
        patients["conditions"].str.contains(r"(^DIAB1| DIAB1)", regex=True, case=False)
    ]
