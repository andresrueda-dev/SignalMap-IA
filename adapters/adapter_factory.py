from .melate_adapter import MelateAdapter
from .retro_adapter import RetroAdapter
from .chispazo_adapter import ChispazoAdapter
from .revanchita_adapter import RevanchitaAdapter
from .tris_adapter import TrisAdapter


class AdapterFactory:

    _registry = {

        "melate": MelateAdapter,

        "retro": RetroAdapter,

        "chispazo": ChispazoAdapter,

        "revanchita": RevanchitaAdapter,

        "tris": TrisAdapter

    }


    @classmethod

    def create(cls, game: str):

        key = game.lower()

        if key not in cls._registry:

            raise ValueError(

                f"Juego no soportado: {game}"

            )

        return cls._registry[key]()
