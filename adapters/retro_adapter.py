import pandas as pd

from .base_adapter import BaseAdapter


class RetroAdapter(BaseAdapter):

    name = "retro"

    universe = 39

    picks = 6

    has_extra = False

    historical_file = "retro.csv"


    def validate(self, df):

        required = [

            "F1",

            "F2",

            "F3",

            "F4",

            "F5",

            "F6"

        ]

        return all(

            c in df.columns

            for c in required

        )
