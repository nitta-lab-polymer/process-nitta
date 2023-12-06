import pandas as pd
from src.process_nitta.csv_config import CSVConfig


def test_csv_config_instron():
    csv_config = CSVConfig().Instron().to_dict()
    try:
        pd.read_csv("./process-nitta/test/csv/instron.csv", **csv_config)
    except Exception as e:
        print(e)
        assert False
