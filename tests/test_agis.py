import pandas as pd
from process_nitta import AGISSample


def test_agis():
    sample = AGISSample(
        file_path="./process-nitta/sample_data/agis.csv",
        name="sample",
    )
    result_df = sample.get_stress_strain_df()
    answer_df = pd.read_csv("./process-nitta/tests/answer_data/agis.csv", index_col=0)
    pd.testing.assert_frame_equal(result_df, answer_df)
