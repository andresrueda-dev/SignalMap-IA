import pandas as pd

from .base_adapter import BaseAdapter


class ChispazoAdapter(BaseAdapter):

    name = "chispazo"

    universe = 28

    picks = 5

    has_extra = False

    historical_file = "chispazo.csv"


    def validate(self, df):

        required = [

            "F1",

            "F2",

            "F3",

            "F4",

            "F5"

        ]

        return all(

            c in df.columns

            for c in required

        )
