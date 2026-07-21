"""
SignalMap AI v1.0
Validator

Responsabilidad:
- Validar que el histórico tenga las columnas necesarias.
- Detectar archivos vacíos.
- Detectar valores nulos.

No modifica datos.
No calcula estadísticas.
"""


class Validator:

    @staticmethod
    def validate_columns(df, required_columns):
        missing = [c for c in required_columns if c not in df.columns]

        if missing:
            raise ValueError(
                f"Faltan columnas: {missing}"
            )

        return True

    @staticmethod
    def validate_empty(df):
        if df.empty:
            raise ValueError("El DataFrame está vacío.")

        return True

    @staticmethod
    def validate_nulls(df):
        if df.isnull().sum().sum() > 0:
            raise ValueError(
                "Existen valores nulos."
            )

        return True
