"""
SignalMap AI v1.0
Data Service

Responsabilidad:
- Leer archivos históricos.
- Validar columnas.
- Ordenar los sorteos.
- Devolver un DataFrame limpio.

NO realiza cálculos.
NO genera predicciones.
"""

from pathlib import Path
import pandas as pd


class DataService:
    """Servicio para cargar históricos de loterías."""

    def __init__(self, data_folder="data"):
        self.data_folder = Path(data_folder)

    def load_csv(self, filename):
        """
        Carga un archivo CSV desde la carpeta data.

        Parámetros:
            filename (str)

        Retorna:
            pandas.DataFrame
        """

        file_path = self.data_folder / filename

        if not file_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {file_path}")

        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("El archivo está vacío.")

        return df

    def sort_by_draw(self, df, column="CONCURSO"):
        """
        Ordena el histórico por número de concurso.
        """

        if column not in df.columns:
            raise ValueError(
                f"No existe la columna '{column}'"
            )

        return df.sort_values(column).reset_index(drop=True)
