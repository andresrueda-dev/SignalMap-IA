from dataclasses import dataclass
from typing import Dict
import pandas as pd


@dataclass(slots=True)
class LotteryState:

    game: str

    universe: int

    picks: int

    historical: pd.DataFrame

    metadata: Dict

    frequencies: pd.DataFrame | None = None

    recency: pd.DataFrame | None = None

    cooccurrence: pd.DataFrame | None = None
