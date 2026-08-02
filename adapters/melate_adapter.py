import pandas as pd

from .base_adapter import BaseAdapter


class MelateAdapter(BaseAdapter):

    name = "melate"

    universe = 56

    picks = 6

    has_extra = True

    historical_file = "melate.csv"


    def validate(self, df: pd.DataFrame):

        required = [

            "F1",

            "F2",

            "F3",

            "F4",

            "F5",

            "F6"

        ]

        missing = [

            c

            for c in required

            if c not in df.columns

        ]

        if missing:

            raise ValueError(

                f"Columnas faltantes {missing}"

            )

        return True
