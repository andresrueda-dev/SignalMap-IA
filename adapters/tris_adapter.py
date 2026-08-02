import pandas as pd

from .base_adapter import BaseAdapter


class TrisAdapter(BaseAdapter):

    name = "tris"

    universe = 10

    picks = 5

    has_extra = False

    historical_file = "tris.csv"


    def validate(self, df: pd.DataFrame):

        required = [

            "P1",

            "P2",

            "P3",

            "P4",

            "P5"

        ]

        return all(

            c in df.columns

            for c in required

        )
