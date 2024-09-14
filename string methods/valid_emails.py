import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[
        users["mail"].str.contains(r"^[a-zA-Z][\w\.-]*@leetcode\.com$", regex=True)
    ]
