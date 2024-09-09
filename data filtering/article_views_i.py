import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return (
        views[views["author_id"] == views["viewer_id"]]["author_id"]
        .rename("id")
        .to_frame()
        .drop_duplicates()
        .sort_values(by="id")
    )
