import pandas as pd

class DataAgent:
    def __init__(self, path: str):
        self.path = path

    def load_data(self):
        # Attempt to parse date column if exists
        try:
            df = pd.read_csv(self.path, parse_dates=['date'])
        except Exception:
            df = pd.read_csv(self.path)
        # Normalize column names
        df.columns = [c.strip() for c in df.columns]
        return df
