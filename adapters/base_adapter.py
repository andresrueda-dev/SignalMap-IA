from abc import ABC, abstractmethod
import pandas as pd


class BaseAdapter(ABC):

    name = ""

    universe = 0

    picks = 0

    has_extra = False

    historical_file = ""


    @abstractmethod
    def validate(self, df: pd.DataFrame):
        pass


    def metadata(self):

        return {

            "game": self.name,

            "universe": self.universe,

            "picks": self.picks,

            "extra": self.has_extra,

            "historical": self.historical_file

        }
